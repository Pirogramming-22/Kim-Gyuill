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

// 숫자 입력 확인
function check_numbers() {
    const number1 = document.getElementById('number1').value;
    const number2 = document.getElementById('number2').value;
    const number3 = document.getElementById('number3').value;

    if (number1 === "" || number2 === "" || number3 === "") {
        return;
    }

    // 입력 값 확인
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `입력한 숫자: ${number1}, ${number2}, ${number3}`;

        // 입력 초기화
        document.getElementById('number1').value = "";
        document.getElementById('number2').value = "";
        document.getElementById('number3').value = "";
    
        // 다시 포커스
        document.getElementById('number1').focus();
}

// 입력시 포커스 이동
function handleFocus(event) {
    const currentInput = event.target;
    if (currentInput.id === 'number1') {
        document.getElementById('number2').focus();
    } else if (currentInput.id === 'number2') {
        document.getElementById('number3').focus();
    }
}

// 입력 필드 이벤트 리스너 추가
document.getElementById('number1').addEventListener('input', handleFocus);
document.getElementById('number2').addEventListener('input', handleFocus);
document.getElementById('number3').addEventListener('input', handleFocus);

// 엔터 감지
document.getElementById('number3').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        check_numbers();
    }
});

// 버튼 클릭 이벤트 리스너
const submitButton = document.querySelector('.submit-button');
submitButton.addEventListener('click', check_numbers);
