document.addEventListener("DOMContentLoaded", function () {
  let form = document.querySelector("#signinForm"); // 確保這裡選擇的是正確的表單
});
function validateSignupForm(event) {
  let name = document.getElementById("signup-name").value;
  let username = document.getElementById("signup-username").value;
  let password = document.getElementById("signup-password").value;

  if (name === "" || username === "" || password === "") {
    event.preventDefault();
    alert("請填寫註冊表單的所有欄位");
  }
}

function validateSigninForm(event) {
  let username = document.getElementById("signin-username").value;
  let password = document.getElementById("signin-password").value;

  if (username === "" || password === "") {
    event.preventDefault();
    alert("請填寫登入表單的所有欄位");
  }
}
