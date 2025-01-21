const searchInput = document.getElementById('searchInput');
const postsContainer = document.querySelector('.posts__contents');

searchInput.addEventListener('input', function () {
    const query = searchInput.value;

    axios
        .get(`/search_posts/`, {
            params: { q: query }, // GET 요청의 쿼리 파라미터
        })
        .then((response) => {
            const results = response.data.results;

            // 결과가 있는지 확인
            if (results && results.length > 0) {
                // 기존 게시물 제거
                postsContainer.innerHTML = '';

                // 새 게시물 추가
                results.forEach((post) => {
                    const postDiv = document.createElement('div');
                    postDiv.classList.add('posts__photo');

                    const link = document.createElement('a');
                    link.href = `/detail/${post.id}`;

                    const img = document.createElement('img');
                    img.src = post.image || "{% static 'assets/images/defaultImage.png' %}";
                    img.alt = '게시물 이미지';

                    link.appendChild(img);
                    postDiv.appendChild(link);
                    postsContainer.appendChild(postDiv);
                });
            } else if (query.length > 0) {
                postsContainer.innerHTML = '<p>검색 결과가 없습니다.</p>';
            } else {
                window.location.reload();
            }
        })
        .catch((error) => {
            // 오류 발생 시 메시지만 출력
        });
});
