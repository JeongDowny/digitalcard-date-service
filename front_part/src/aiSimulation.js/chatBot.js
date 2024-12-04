'use strict';

const apiKey = ""; // ChatGPT API 키
const model = "gpt-3.5-turbo";

let selectedCharacter = null;
let confirmedCard = null; // 확정된 카드 정보 저장
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const modalDescription = document.getElementById("modal-description");
const startChatButton = document.getElementById("start-chat-button");
const chatBox = document.getElementById("chat-box");
const messages = document.getElementById("messages");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const personCard = document.querySelector(".character-card[data-character='']");
const characterSettings = {
  "방민정": `You are 방민정, a 20-year-old cheerful and bright individual with an ENFP personality. You like taking walks. In this online blind date, respond casually or politely based on the user's tone.`,
  "임가현": `You are 임가현, a 25-year-old calm and reserved individual with an INTJ personality. You enjoy watching OTT shows. Respond naturally, matching the user's tone.`,
  "공민혁": `You are 공민혁, a 22-year-old passionate and friendly individual with an ENFJ personality. You love playing soccer and admire Son Heung-min.`,
  "차현우": `You are 차현우, a 24-year-old confident and disciplined individual with an ESTJ personality. You love fitness and gym activities.`,
  "김하늘": `You are 김하늘, a 23-year-old sweet and reserved individual with an INFP personality. You enjoy reading books and intellectual conversations.`,
  "이지나": `You are 이지나, a 21-year-old bold and artistic individual with an ENTJ personality. You love painting and creative projects.`,
  "최성현": `You are 최성현, a 27-year-old intellectual and diligent individual with an ISTJ personality. You enjoy coding and problem-solving.`,
};

// sessionStorage에서 저장된 카드 데이터를 가져와 person 카드에 반영
document.addEventListener("DOMContentLoaded", () => {
    const storedCard = JSON.parse(sessionStorage.getItem("confirmedCard"));

    if (storedCard) {
        setConfirmedCard(storedCard);
    } else {
        console.error("확정된 카드 데이터가 없습니다.");
    }
});

function setConfirmedCard(card) {
    confirmedCard = card; // 확정된 카드 저장

    // person 카드 업데이트
    personCard.querySelector("img").src = card.image;
    personCard.querySelector(".character-name").textContent = card.name;
    personCard.dataset.character = card.name;
    personCard.dataset.description = `${card.age}살, ${card.mbti} 성격. ${card.hobbies}를 좋아합니다.`;

    // characterSettings에 추가
    characterSettings[card.name] = `You are ${card.name}, a ${card.age}-year-old individual with a ${card.mbti} personality. You enjoy ${card.hobbies}. Match the user's tone and respond naturally, avoiding overly formal expressions.`;
}
