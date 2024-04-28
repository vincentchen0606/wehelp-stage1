document.addEventListener("DOMContentLoaded", function () {
  var form = document.querySelector("#signinForm"); // 確保這裡選擇的是正確的表單
  var checkbox = document.querySelector("#myCheckbox"); // 更改ID以匹配HTML中的勾選框

  // 將回調函數提取到單獨的函數中
  function checkCheckbox(event) {
    if (!checkbox.checked) {
      event.preventDefault();
      alert("Please check the checkbox first");
    } else {
      form.submit(); // 如果複選框已被選中，手動提交表單
    }
  }

  form.addEventListener("submit", checkCheckbox);
});
