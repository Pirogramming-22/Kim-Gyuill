// 숫자 랜덤 생성
function generateRandomNumbers() {
    const numbers = [];
    while (numbers.length < 3) {
        const randomNumber = Math.floor(Math.random() * 9) + 1;
        if (!numbers.includes(randomNumber)) {
            numbers.push(randomNumber); // 중복 방지
        }
    }
    return numbers;
}

const randomNumbers = generateRandomNumbers();
console.log(randomNumbers);

// 결과 계산 함수
function checkResults(userInputs, randomNumbers) {
    let strikes = 0;
    let balls = 0;

    userInputs.forEach((num, index) => {
        if (num === randomNumbers[index]) {
            strikes++; // 숫자와 위치 모두 일치
        } else if (randomNumbers.includes(num)) {
            balls++; // 숫자는 맞지만 위치가 다름
        }
    });
    return { strikes, balls };
}


let attempts = 9; // 도전 가능 횟수
let is_Running = true;
document.getElementById('attempts').innerText = attempts;

// 숫자 입력 확인
function check_numbers() {
    if(!is_Running) return; //기회 다 쓰면 비활성화

    const number1 = document.getElementById('number1').value;
    const number2 = document.getElementById('number2').value;
    const number3 = document.getElementById('number3').value;

    if (number1 === "" || number2 === "" || number3 === "") {
        return;
    }

    // 입력 값을 배열로 변환
    const userInputs = [parseInt(number1), parseInt(number2), parseInt(number3)];

    // 결과 계산
    const { strikes, balls } = checkResults(userInputs, randomNumbers);

    // 결과 출력
    const resultsDiv = document.getElementById('results');
    resultsDiv.style.width = "400px"; // 가로 크기 동기화

    if (strikes === 0 && balls === 0) { // 아웃
        resultsDiv.innerHTML += `
            <p class="check-result">
                <span style="flex: 1; text-align: left;">${number1} ${number2} ${number3}</span>
                <span style="flex: 0; text-align: center;">:</span>
                <span style="flex: 1; text-align: right;">
                <span class="out num-result">O</span>
                </span>
            </p>`;
    } else { // 스트라이크, 볼 존재
        resultsDiv.innerHTML += `
            <p class="check-result">
                <span style="flex: 1; text-align: left;">${number1} ${number2} ${number3}</span>
                <span style="flex: 0; text-align: center;">:</span>
                <span style="flex: 1; text-align: right;">
                    <span class="left">${strikes}</span><span class="strike num-result">S</span>
                    <span class="left">${balls}</span><span class="ball num-result">B</span>
                </span>
            </p>`;
    }

    // 도전 가능 횟수 감소
    attempts--;
    document.getElementById('attempts').innerText = attempts;

    // 성공, 실패 이미지 업데이트
    if (strikes === 3) {
        document.getElementById("game-result-img").src = "./success.png";
        is_Running = !is_Running;
    } else if (attempts < 1) {
        document.getElementById("game-result-img").src = "./fail.png";
        is_Running = !is_Running;
    }

    // 입력 초기화
    document.getElementById('number1').value = "";
    document.getElementById('number2').value = "";
    document.getElementById('number3').value = "";

    // 다시 포커스
    document.getElementById('number1').focus();
}

// 입력시 포커스 이동
function nextFocus(event) {
    const currentInput = event.target;
    if (currentInput.id === 'number1') {
        document.getElementById('number2').focus();
    } else if (currentInput.id === 'number2') {
        document.getElementById('number3').focus();
    }
}

// 입력 필드 이벤트 리스너 추가
document.getElementById('number1').addEventListener('input', nextFocus);
document.getElementById('number2').addEventListener('input', nextFocus);
document.getElementById('number3').addEventListener('input', nextFocus);


// 엔터 감지
document.getElementById('number3').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        check_numbers();
    }
});

// 버튼 클릭 이벤트 리스너
const submitButton = document.querySelector('.submit-button');
submitButton.addEventListener('click', check_numbers);

