document.addEventListener("DOMContentLoaded", () => {
    const card = document.querySelector(".card"); // 카드 요소 선택

    // 상태 변수로 뒤집힌 상태 저장
    let isFlipped = false;

    // 클릭 이벤트 리스너 추가
    card.addEventListener("click", () => {
        // `cardData`가 비어 있는 경우 뒤집기 차단
        console.log(window.cardData);
        if (window.cardData.length === 0) {
            alert("확인 버튼을 먼저 눌러주세요.");
            return;
        }
        else {
            isFlipped = !isFlipped; // 상태 반전
            card.style.transform = isFlipped ? "rotateY(180deg)" : "rotateY(0deg)";
        }
    });
});