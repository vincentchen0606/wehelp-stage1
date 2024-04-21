//可以用點擊切換圖片，然後出現的x圖片zindex比較大就好 然後圖片原本要放在navbar那邊
// DOMcontentloaded確保html先載入
document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.querySelector(".menu-icon");
  const navbar = document.querySelector(".navbar");

  menuIcon.addEventListener("click", () => {
    menuIcon.classList.toggle("active");
    navbar.classList.toggle("active");
  });
});

// 發送 HTTP 請求並獲取資料
fetch(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
)
  .then((response) => response.json())
  .then((data) => {
    // 獲取圖片網址和景點標題
    const attractionData = data.data.results.map((attraction) => {
      const filelist = attraction.filelist;
      let imageUrl = null;
      if (filelist) {
        const fileArray = filelist.split("https://");
        const jpgFile = fileArray.find((file) =>
          file.toLowerCase().endsWith(".jpg")
        );
        if (jpgFile) {
          imageUrl = `https://${jpgFile}`;
        }
      }
      return {
        imageUrl: imageUrl,
        stitle: attraction.stitle,
      };
    });

    // 獲取所有需要替換圖片的 <img> 元素
    const imgElements = [
      document.querySelector(".promotion1 img"),
      document.querySelector(".promotion2 img"),
      document.querySelector(".promotion3 img"),
      document.querySelector(".title1 img"),
      document.querySelector(".title2 img"),
      document.querySelector(".title3 img"),
      document.querySelector(".title4 img"),
      document.querySelector(".title5 img"),
      document.querySelector(".title6 img"),
      document.querySelector(".title7 img"),
      document.querySelector(".title8 img"),
      document.querySelector(".title9 img"),
      document.querySelector(".title10 img"),
    ];

    // 獲取所有需要替換內容的 <h3> 元素
    const h3Elements = [
      document.querySelector(".promotion1 h3"),
      document.querySelector(".promotion2 h3"),
      document.querySelector(".promotion3 h3"),
      document.querySelector(".title1 h3"),
      document.querySelector(".title2 h3"),
      document.querySelector(".title3 h3"),
      document.querySelector(".title4 h3"),
      document.querySelector(".title5 h3"),
      document.querySelector(".title6 h3"),
      document.querySelector(".title7 h3"),
      document.querySelector(".title8 h3"),
      document.querySelector(".title9 h3"),
      document.querySelector(".title10 h3"),
    ];

    // 迭代每個景點資料,替換圖片網址和標題內容
    attractionData.forEach((attraction, index) => {
      if (index < imgElements.length) {
        const imgElement = imgElements[index];
        const h3Element = h3Elements[index];

        if (attraction.imageUrl) {
          imgElement.src = attraction.imageUrl;
        }

        if (attraction.stitle) {
          h3Element.textContent = attraction.stitle;
        }
      }
    });
  })
  .catch((error) => {
    console.log("Error:", error);
  });

// 獲取 JSON 數據
document.addEventListener("DOMContentLoaded", function () {
  const apiUrl =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
  const promotionElements = document.querySelectorAll(
    ".promotion1, .promotion2, .promotion3"
  );
  const titleElements = document.querySelectorAll(
    ".title1, .title2, .title3, .title4, .title5, .title6, .title7, .title8, .title9, .title10"
  );
  const loadMoreBtn = document.getElementById("loadMoreBtn");
  let attractionData = [];
  let currentIndex = 0;

  // 獲取資料並渲染初始內容
  fetchData();

  // 點擊 Load More 按鈕時渲染額外的內容
  loadMoreBtn.addEventListener("click", renderExtraContent);

  function fetchData() {
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        attractionData = data.result.results;
        renderPromotionContent();
        renderTitleContent();
      })
      .catch((error) => {
        console.log("Error:", error);
      });
  }

  function renderPromotionContent() {
    promotionElements.forEach((element, index) => {
      const attraction = attractionData[index];
      const imageUrl = getImageUrl(attraction.file || attraction.filelist);
      const title = attraction.stitle;

      const imgElement = element.querySelector("img");
      const h3Element = element.querySelector("h3");

      imgElement.src = imageUrl;
      h3Element.textContent = title;
    });
  }

  function renderTitleContent() {
    titleElements.forEach((element, index) => {
      const attraction = attractionData[index + promotionElements.length];
      const imageUrl = getImageUrl(attraction.file || attraction.filelist);
      const title = attraction.stitle;

      const imgElement = element.querySelector("img");
      const h3Element = element.querySelector("h3");

      imgElement.src = imageUrl;
      h3Element.textContent = title;
    });

    currentIndex = titleElements.length + promotionElements.length;
  }

  function renderExtraContent() {
    const extraContent = document.createDocumentFragment();

    for (let i = 0; i < 10; i++) {
      if (currentIndex >= attractionData.length) {
        loadMoreBtn.disabled = true; // 當所有圖片都已經顯示完畢時,將按鈕設置為不可點擊狀態
        break;
      }

      const attraction = attractionData[currentIndex];
      const imageUrl = getImageUrl(attraction.file || attraction.filelist);
      const title = attraction.stitle;

      const divElement = document.createElement("div");
      divElement.classList.add(`title${(currentIndex % 10) + 1}`);

      const imgElement = document.createElement("img");
      imgElement.src = imageUrl;

      const h3Element = document.createElement("h3");
      h3Element.textContent = title;

      const starIconElement = document.createElement("div");
      starIconElement.classList.add("star-icon");
      const starIconText = document.createTextNode("★");
      starIconElement.appendChild(starIconText);

      divElement.appendChild(imgElement);
      divElement.appendChild(h3Element);
      divElement.appendChild(starIconElement);

      extraContent.appendChild(divElement);

      currentIndex++;
    }

    document.querySelector(".big_box").appendChild(extraContent);
  }

  function getImageUrl(filelist) {
    if (!filelist) {
      return "";
    }

    const fileArray = filelist.split("https://");
    const jpgFile = fileArray.find((file) =>
      file.toLowerCase().endsWith(".jpg")
    );

    return jpgFile ? `https://${jpgFile}` : "";
  }
});
