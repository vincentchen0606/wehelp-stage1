// DOMContentLoaded 確保html先loading
document.addEventListener("DOMContentLoaded", function () {
  const hamMenu = document.querySelector(".ham-menu");

  const navbar = document.querySelector(".navbar");

  hamMenu.addEventListener("click", () => {
    hamMenu.classList.toggle("active");
    navbar.classList.toggle("active");
  });
});
