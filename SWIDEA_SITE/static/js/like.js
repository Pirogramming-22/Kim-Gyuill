document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function () {
        const ideaId = this.dataset.id;
        const starIcon = this.querySelector('.star-icon'); // 버튼 내부의 이미지

        fetch(`/like/${ideaId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_liked !== undefined) {
                if (starIcon) { // 이미지가 존재하는 경우
                    const newSrc = data.is_liked 
                        ? '/static/img/채워진 별.png' 
                        : '/static/img/빈 별.png';
                    starIcon.src = newSrc; // 이미지 변경
                    this.classList.toggle('is-liked', data.is_liked); // 클래스 토글
                } else {
                    console.warn(`이미지를 찾을 수 없습니다. 아이디어 ID: ${ideaId}`);
                }
            } else {
                console.error(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

// 관심도
document.querySelectorAll('.interest-up, .interest-down').forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        event.stopPropagation();

        const ideaId = this.dataset.id;
        const isUp = this.classList.contains('interest-up'); // up인지 down인지 확인
        const interestValueElement = document.getElementById(`interest-${ideaId}`);

        fetch(`/update-interest/${ideaId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ increment: isUp })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                interestValueElement.textContent = data.new_interest; // 새로운 관심도 업데이트
            } else {
                console.error(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});