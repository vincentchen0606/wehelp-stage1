document.addEventListener("DOMContentLoaded", function () {
  let form = document.querySelector("#signinForm"); // 確保這裡選擇的是正確的表單
  // 為查詢按鈕添加點擊事件監聽器
  document.getElementById("queryButton").addEventListener("click", queryMember);
  document.getElementById("updateButton").addEventListener("click", updateName);
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
// queryMember 函數，使用 fetch 函數呼叫後端的會員查詢 API：
// 在此函數中，我們獲取輸入框中的 username 值，並使用 fetch 函數向後端發送 GET 請求。然後根據響應的資料，顯示匹配的會員資料或 "No Data"。
// 這樣就完成了在前端呼叫會員查詢 API 的功能，並且不會導致頁面重新整理或重定向。
async function queryMember() {
  const username = document.getElementById("usernameInput").value;
  const response = await fetch(`/api/member?username=${username}`);
  const data = await response.json();

  const nameResult = document.getElementById("nameResult");
  const usernameResult = document.getElementById("usernameResult");

  if (data.data) {
    nameResult.textContent = `${data.data.name}`;
    usernameResult.textContent = `(${data.data.username})`;
  } else {
    nameResult.textContent = "No Data";
    usernameResult.textContent = "";
  }
}

// 更新姓名

async function updateName() {
  const newName = document.getElementById("nameInput").value;
  const response = await fetch("/api/member", {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: newName }),
  });
  const data = await response.json();

  if (data.ok) {
    document.getElementById("updateResult").textContent = "Updated";
    document.querySelector("h2").textContent = `${newName},歡迎登入系統`;
  } else {
    document.getElementById("updateResult").textContent = "Failed to Update";
  }
}
