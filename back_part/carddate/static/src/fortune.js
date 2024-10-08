'use strict';

document.addEventListener("DOMContentLoaded", function() {
    const fortunes = [
        document.querySelector('.start__fortune__content1'),
        document.querySelector('.start__fortune__content2'),
        document.querySelector('.start__fortune__content3'),
        document.querySelector('.start__fortune__content4'),
        document.querySelector('.start__fortune__content5')
    ];

    const button = document.querySelector('.start__fortune__button');

    // 처음에는 content1만 보이도록
    fortunes.forEach((fortune, index) => {
        if (index !== 0) {
            fortune.style.display = 'none';
        }
    });

    button.addEventListener('click', function() {
        // 모든 내용을 숨기고
        fortunes.forEach(fortune => fortune.style.display = 'none');
        
        // 랜덤으로 하나의 포춘 내용만 보이게 함
        const randomIndex = Math.floor(Math.random() * fortunes.length);
        fortunes[randomIndex].style.display = 'block';
    });
});
