document.querySelector(".submitButton").addEventListener("click", function(event) {
    event.preventDefault(); // 기본 폼 제출 동작 방지

    // 제출 확인 대화 상자 표시
    const isConfirmed = confirm("정말로 제출하시겠습니까?");
    if (!isConfirmed) {
        return; // '아니오'를 선택하면 함수 종료
    }

    // 폼 데이터 가져오기
    const formData = new FormData(document.querySelector(".form-container"));

    // FormData를 JSON 객체로 변환
    const formObj = {};
    formData.forEach((value, key) => {
        formObj[key] = value;
    });

    // 데이터를 백엔드로 전송하기 (POST 요청)
    fetch('백엔드 API URL', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formObj),
    })
    .then(response => response.json())  // 응답을 JSON으로 파싱
    .then(data => {
        // 서버로부터의 응답 처리
        console.log('서버 응답:', data);
        alert('제출이 완료되었습니다!');
    })
    .catch(error => {
        // 에러 처리
        console.error('Error:', error);
        alert('서버로 데이터를 전송하는데 문제가 발생했습니다.');
    });
});
