document.addEventListener("DOMContentLoaded", () => {
    const onClickLike = async (id, type) => {
        const url = "/like_post/";
        const csrfToken = document.getElementById("csrf-token").value;

        try {
            const response = await axios.post(
                url,
                { id, type },
                {
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken,
                    },
                }
            );

            if (response.status === 200) {
                likeHandleResponse(response.data.id, response.data.type);
            } else {
                console.error("서버 응답 오류:", response);
            }
        } catch (error) {
            console.error("좋아요 요청 중 오류 발생:", error);
        }
    };

    const likeHandleResponse = (id, type) => {
        const element = document.querySelector(`.like-button[data-post-id="${id}"] .like-count`);
        if (element) {
            const currentCount = Number(element.innerText);
            element.innerText = currentCount + 1;
        }
    };

    // 좋아요 버튼 이벤트 핸들러 등록
    document.querySelectorAll(".like-button").forEach(button => {
        const postId = button.getAttribute("data-post-id");
        button.addEventListener("click", () => onClickLike(postId, "like"));
    });
});
