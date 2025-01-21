document.addEventListener("DOMContentLoaded", () => {
    const navButtons = document.querySelectorAll("footer .navBar");

    navButtons.forEach(button => {
        button.addEventListener("click", () => {
            document.querySelectorAll("footer .navBar--selected").forEach(selected => {
                selected.classList.remove("navBar--selected");
                const img = selected.querySelector("img");
                img.src = img.getAttribute("data-default-src");
            });

            button.classList.add("navBar--selected");
            const img = button.querySelector("img");
            img.src = img.getAttribute("data-selected-src");
        });
    });
});
