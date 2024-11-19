'use strict';

const colors = document.querySelectorAll(".color");
const card = document.querySelector(".form-container");

colors.forEach((element) => {
    element.addEventListener("click", function(event){
        changeColor(event.target);
    });
});

function changeColor(clickedColor){
    const cardSrc = clickedColor.getAttribute("data-src"); 
    card.style.backgroundImage = `url(${cardSrc})`; 
}
