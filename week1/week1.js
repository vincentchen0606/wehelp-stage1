//可以用點擊切換圖片，然後出現的x圖片zindex比較大就好 然後圖片原本要放在navbar那邊
document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.querySelector(".menu-icon");
  const navbar = document.querySelector(".navbar");

  menuIcon.addEventListener("click", () => {
    menuIcon.classList.toggle("active");
    navbar.classList.toggle("active");
  });
});
