let timerDisplay = document.querySelector('.timer-nums span');
let startButton = document.getElementById('start');
let stopButton = document.getElementById('stop');
let resetButton = document.getElementById('reset');

let timerInterval; // 타이머를 저장할 변수
let elapsedTime = 0; // 경과 시간 (0.01초 단위)

// 시간 계산
function formatTime(time) {
    const seconds = Math.floor(time / 100);
    const milliseconds = time % 100;

    return `${String(seconds).padStart(2, '0')}:${String(milliseconds).padStart(2, '0')}`;
}

// 타이머 시작 함수
function startTimer() {
    if (!timerInterval) { // 타이머가 이미 실행 중이 아니면
        timerInterval = setInterval(() => {
            elapsedTime++;
            timerDisplay.textContent = formatTime(elapsedTime);
        }, 10); // 10ms마다 실행
    }
}

// 타이머 정지
function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null; // 타이머 초기화
}

// 타이머 리셋 함수
function resetTimer() {
    stopTimer();
    elapsedTime = 0; // 시간 초기화
    timerDisplay.textContent = formatTime(elapsedTime);
}

// 버튼 이벤트 리스너 추가
startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);
