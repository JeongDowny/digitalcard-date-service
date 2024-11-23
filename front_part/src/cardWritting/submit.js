
document.addEventListener("DOMContentLoaded", ()=>{
    const submitForm = document.querySelector("form");
    submitForm.document.addEventListener("submit", signup);
});

async function signup(event){
    const isConfirmed = confirm("정말로 제출하시겠습니까?");
    if (!isConfirmed) {
        return; 
    }

    event.preventDefault();
    const url = "백엔드 API URL 지정하는 곳";

    const formData = new FormData(document.querySelector(".form-container"));
    
    const formObj = {};
    formData.forEach((value, key)=>{
        formObj[key] = value;
    });

    const body = JSON.stringify(formObj);

    try{
        const response = await fetch(url, {
            method: "POST",
            headers : {"Content-type: application/json"},
            body: body
        });
    
        if(!response.ok){
            const errorMessage = `HTTP 에러 발생: ${response.status}`;
            console.error(errorMessage);
            throw new Error(errorMessage);   
        } else{
            const data = await response.json();
            console.log(`서버응답: ${data}`);
            alert("제출이 완료됐습니다.")
            window.location.href("../../cardDrawing.html");
        }     
    } catch(error){
        console.error('Error:', error);
        alert('서버로 데이터를 전송하는데 문제가 발생했습니다.');
    }   
   
}
