'use strict';

const sectionIds = [
  '#home',
  '#ad',
  '#step1',
  '#step2', // step2, step3가 누락된 듯하여 추가했습니다.
  '#step3',
  '#start',
  '#contact',
];

// 각 섹션을 가져옵니다.
const sections = sectionIds.map((id) => document.querySelector(id));

// 각 내비게이션 아이템을 가져옵니다.
const navItems = sectionIds.map((id) => document.querySelector(`a[href="${id}"]`));

// 섹션이 보이는지를 추적하는 배열을 초기화합니다.
const visibleSections = sectionIds.map(() => false);

// 첫 번째 내비게이션 아이템을 활성화합니다.
let activeNavItem = navItems[0];

// 옵저버 옵션 설정 (섹션의 20%를 지나갈 때마다 감지)
const options = {
  rootMargin: '-20% 0px 0px 0px',
  threshold: [0, 0.98],
};

// IntersectionObserver를 생성하고 콜백 함수를 전달합니다.
const observer = new IntersectionObserver(observerCallback, options);

// 각 섹션을 옵저버로 감시합니다.
sections.forEach((section) => {
  if (section) { // 섹션이 null이 아닌지 확인
    observer.observe(section);
  }
});

// 옵저버 콜백 함수
function observerCallback(entries) {
  let selectLastOne = false;

  // 각 섹션에 대해 현재 화면에 보이는지 여부를 확인
  entries.forEach((entry) => {
    const index = sectionIds.indexOf(`#${entry.target.id}`);
    visibleSections[index] = entry.isIntersecting;

    // 마지막 섹션이 거의 다 보이면 해당 섹션을 활성화
    if (index === sectionIds.length - 1 && entry.isIntersecting && entry.intersectionRatio >= 0.95) {
      selectLastOne = true;
    }
  });

  // 마지막 섹션을 선택할지 아니면 가장 처음 보이는 섹션을 선택할지 결정
  const navIndex = selectLastOne
    ? sectionIds.length - 1
    : findFirstIntersecting(visibleSections);
    
  // 내비게이션 아이템을 선택
  selectNavItem(navIndex);
}

// 첫 번째로 보이는 섹션을 찾는 함수
function findFirstIntersecting(sections) {
  const index = sections.indexOf(true);
  return index >= 0 ? index : 0;
}

// 선택된 내비게이션 아이템을 활성화하는 함수
function selectNavItem(index) {
  const navItem = navItems[index];
  if (!navItem) return;

  // 기존 활성화된 아이템에서 active 클래스를 제거하고 새로운 아이템에 추가
  activeNavItem.classList.remove('nav__active');
  activeNavItem = navItem;
  activeNavItem.classList.add('nav__active');
}
