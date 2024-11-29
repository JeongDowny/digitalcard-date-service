document.addEventListener('DOMContentLoaded', () => {
    const toggleCardButton = document.getElementById('toggleCardButton');
    const confirmButton = document.getElementById('confirmButton');
    const animalImage = document.querySelector('.animal-image');
    const cardBack = document.querySelector('.start_card-back');
    const infoRows = document.querySelectorAll('.info-row.hidden');

    const cardInfo = {
        id: document.querySelector('.id'),
        gender: document.querySelector('.gender'),
        name: document.querySelector('.name'),
        age: document.querySelector('.age'),
        major: document.querySelector('.major'),
        mbti: document.querySelector('.mbti'),
        hobby: document.querySelector('.hobby'),
        contact: document.querySelector('.contact'),
    };

    window.cardData = []; // 서버에서 받은 카드 데이터를 저장
    let currentCardIndex = 0; // 현재 표시 중인 카드의 인덱스

    // 서버에서 카드 데이터를 가져오는 함수
    async function fetchCardData() {
        try {
            const response = await fetch('/random/open'); // 실제 API URL
            if (!response.ok) {
                throw new Error('Failed to fetch card data');
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching card data:', error);
            alert('카드 데이터를 불러오는 데 실패했습니다.');
        }
    }

    // 카드 UI 업데이트 함수
    function updateCardUI(data) {
        if (!data) return;

        // 현재 표시할 카드 데이터
        const currentCard = data[currentCardIndex];
        console.log(currentCard);

        // 카드 UI 업데이트
        cardInfo.id = currentCard.id;
        cardInfo.gender.textContent = currentCard.gender;
        cardInfo.name.textContent = currentCard.name;
        cardInfo.major.textContent = currentCard.major;
        cardInfo.age.textContent = currentCard.age;
        cardInfo.mbti.textContent = currentCard.mbti;
        cardInfo.hobby.textContent = currentCard.hobby;
        cardInfo.contact.textContent = currentCard.contact;

        console.log('Displaying card:', currentCard);
    }

    // 카드 전환 및 초기 데이터 로드
    toggleCardButton.addEventListener('click', async () => {
        if (cardData.length === 0) {
            // 데이터를 처음 가져오는 경우
            const fetchedData = await fetchCardData();
            if (fetchedData) {
                cardData = fetchedData; // 카드 데이터 저장
                currentCardIndex = 0; // 첫 번째 카드부터 표시
                updateCardUI(cardData);
                confirmButton.disabled = false; // 확인 버튼 활성화
            }
        } else {
            // 데이터가 이미 있는 경우, 다음 카드로 전환
            currentCardIndex = (currentCardIndex + 1) % cardData.length; // 순환 처리
            updateCardUI(cardData);
        }
    });


    // 확인 버튼 클릭 이벤트
    confirmButton.addEventListener('click', async () => {
    const confirmAction = confirm("해당 카드를 확정하시겠습니까?");
    if (confirmAction) {
        infoRows.forEach(row => row.querySelector('.value').style.visibility = 'visible');
        toggleCardButton.disabled = true;
        confirmButton.disabled = true;

        // 현재 카드의 ID를 플라스크에 보내는 POST 요청
        const currentCardId = cardData[currentCardIndex].id;
        try {
            const response = await fetch('/random/confirm', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ id: currentCardId }),
            });

            if (response.status === 200) {
                const result = await response.json();
                console.log('Confirmation result:', result);
                alert('카드가 성공적으로 확정되었습니다!');
            } else if (response.status === 500) {
                throw new Error('서버 에러: 카드를 확정할 수 없습니다.');
            } else {
                throw new Error('예기치 않은 오류가 발생했습니다.');
            }
        } catch (error) {
            console.error('Error confirming card:', error);
            alert(error.message);
            }
        }
    });
});
