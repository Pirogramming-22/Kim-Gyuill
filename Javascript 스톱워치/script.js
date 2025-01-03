const timerDisplay = document.querySelector('.timer-nums span');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const checkButton = document.getElementById('check-button');
const checkImage = document.getElementById('check');
const deleteButton = document.getElementById('delete-button');
const recordList = document.getElementById('record-list');

let timerInterval; // 타이머를 저장할 변수
let elapsedTime = 0; // 경과 시간 (0.01초 단위)
let isHeaderChecked = false; // 헤더 체크 상태 추적

// 시간 계산
function formatTime(time) {
    const seconds = Math.floor(time / 100);
    const milliseconds = time % 100;
    return `${String(seconds).padStart(2, '0')}:${String(milliseconds).padStart(2, '0')}`;
}

// 타이머 시작
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
    saveRecord(); // 기록 저장
}

// 타이머 리셋
function resetTimer() {
    clearInterval(timerInterval);
    timerInterval = null; // 타이머 초기화
    elapsedTime = 0; // 시간 초기화
    timerDisplay.textContent = formatTime(elapsedTime);
}

// 기록 저장
function saveRecord() {
    const recordContainer = document.createElement('div');
    recordContainer.classList.add('record-container');

    // 개별 체크박스
    const checkboxImg = document.createElement('img');
    checkboxImg.src = './checkbox-blank.png';
    checkboxImg.alt = 'checkbox';
    checkboxImg.classList.add('record-checkbox');

    // 체크박스 클릭 이벤트
    checkboxImg.addEventListener('click', () => {
        if (checkboxImg.src.includes('checkbox-blank.png')) {
            checkboxImg.src = './checkbox-checked.png';
        } else {
            checkboxImg.src = './checkbox-blank.png';
        }
        updateHeaderCheckbox(); // 헤더 체크박스 상태 업데이트
    });

    // 기록 시간
    const recordTime = document.createElement('div');
    recordTime.classList.add('record');
    recordTime.textContent = formatTime(elapsedTime);

    recordContainer.appendChild(checkboxImg);
    recordContainer.appendChild(recordTime);
    recordList.appendChild(recordContainer);
}

// 헤더 체크박스 버튼 클릭 이벤트
checkButton.addEventListener('click', () => {

    // 기록이 없으면 클릭 안되게
    const recordCheckboxes = document.querySelectorAll('.record-checkbox');
    if (recordCheckboxes.length === 0) {
        return; 
    }

    isHeaderChecked = !isHeaderChecked; // 상태 토글
    checkImage.src = isHeaderChecked ? './checkbox-checked.png' : './checkbox-blank.png';

    // 기록 체크박스 상태 변경
    recordCheckboxes.forEach(checkbox => {
        checkbox.src = isHeaderChecked ? './checkbox-checked.png' : './checkbox-blank.png';
    });
});

// 헤더 체크박스 상태 업데이트
function updateHeaderCheckbox() {
    const recordCheckboxes = document.querySelectorAll('.record-checkbox');
    if (recordCheckboxes.length === 0) {
        isHeaderChecked = false; // 기록이 없으면 체크 해제
        checkImage.src = './checkbox-blank.png';
        return;
    }

    const allChecked = Array.from(recordCheckboxes).every(checkbox =>
        checkbox.src.includes('checkbox-checked.png')
    );

    isHeaderChecked = allChecked; // 헤더 상태 동기화
    checkImage.src = isHeaderChecked ? './checkbox-checked.png' : './checkbox-blank.png';
}

// 기록 삭제 버튼 이벤트
deleteButton.addEventListener('click', () => {
    const recordContainers = document.querySelectorAll('.record-container');
    recordContainers.forEach(container => {
        const checkbox = container.querySelector('.record-checkbox');
        if (checkbox.src.includes('checkbox-checked.png')) {
            container.remove(); // 체크된 기록만 삭제
        }
    });
    updateHeaderCheckbox(); // 헤더 체크박스 상태 업데이트
});

// 버튼 이벤트 리스너 추가
startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);
