document.addEventListener('DOMContentLoaded', function() {
    document.querySelector(".submitButton").addEventListener("click", async function(event) {
        event.preventDefault();

        try {
            const formInputs = document.querySelectorAll('.form_row input');
            const formData = {
                gender: formInputs[0].value || formInputs[0].placeholder,
                name: formInputs[1].value || formInputs[1].placeholder,
                major: formInputs[2].value || formInputs[2].placeholder,
                age: formInputs[3].value || formInputs[3].placeholder,
                mbti: formInputs[4].value || formInputs[4].placeholder,
                hobby: formInputs[5].value || formInputs[5].placeholder,
                contact: formInputs[6].value || formInputs[6].placeholder
            };

            console.log('Sending data:', formData); // 디버깅용

            const response = await fetch('/card/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            console.log('Response status:', response.status); // 디버깅용

            const result = await response.json();

            if (response.ok) {
                alert('프로필이 성공적으로 저장되었습니다!');
                window.location.href = '/card/drawing';
            } else {
                throw new Error(result.message || '서버 응답이 실패했습니다.');
            }

        } catch (error) {
            console.error('Error:', error);
            alert('제출 중 오류가 발생했습니다: ' + error.message);
        }
    });
});