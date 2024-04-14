console.log("=================Task01==================");
function findAndPrint(messages, currentStation) {
  const mainLine = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
  ];
  const branchLine = ["Qizhang", "Xiaobitan"];

  let minDistance = Infinity; // JS正無限大
  let nearestFriends = [];

  for (const [friend, message] of Object.entries(messages)) {
    if (mainLine.some((station) => message.includes(station))) {
      // Check if any station in mainLine is in the message
      for (const station of mainLine) {
        if (message.includes(station)) {
          const distance = Math.abs(
            mainLine.indexOf(currentStation) - mainLine.indexOf(station)
          );
          if (distance < minDistance) {
            minDistance = distance; // 更新最短距離
            nearestFriends = [friend];
          }
          break;
        }
      }
    } else if (branchLine.some((station) => message.includes(station))) {
      // Check if any station in branchLine is in the message
      for (const station of branchLine) {
        if (message.includes(station)) {
          let distance;
          if (branchLine.includes(currentStation)) {
            distance = Math.abs(
              branchLine.indexOf(currentStation) - branchLine.indexOf(station)
            );
          } else {
            distance =
              Math.abs(
                mainLine.indexOf("Qizhang") - mainLine.indexOf(currentStation)
              ) + 1;
          }
          if (distance < minDistance) {
            minDistance = distance;
            nearestFriends = [friend];
          }
          break;
        }
      }
    }
  }

  if (nearestFriends.length > 0) {
    // Check if there are any nearest friends
    console.log(nearestFriends.join(", "));
  }
}

const messages = {
  Leslie: "I'm at home near Xiaobitan station.",
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Vivian: "I'm at Xindian station waiting for you.",
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

console.log("=================Task02==================");
let bookings = [];

function book(consultants, hour, duration, criteria) {
  const end_hour = hour + duration;

  // 篩有空的顧問
  let available_consultants = consultants.filter((consultant) => {
    return !bookings.some((booking) => {
      return (
        booking.name === consultant.name &&
        !(booking.end_hour <= hour || booking.start_hour >= end_hour)
      );
    });
  });

  // 顧問沒空則 print "No Service"
  if (available_consultants.length === 0) {
    console.log("No Service");
    return;
  }

  // 根據price or rate選
  let best_consultant;
  if (criteria === "price") {
    best_consultant = available_consultants.reduce((best, current) => {
      return best.price < current.price ? best : current;
    });
  } else if (criteria === "rate") {
    best_consultant = available_consultants.reduce((best, current) => {
      return best.rate > current.rate ? best : current;
    });
  }

  //
  bookings.push({
    name: best_consultant.name,
    start_hour: hour,
    end_hour: end_hour,
  });

  // 印適合的顧問名
  console.log(best_consultant.name);
}

const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

console.log("=================Task03==================");
function func(...data) {
  let middleNames = {};
  for (let name of data) {
    let middleName;
    if ([2, 3].includes(name.length)) {
      // 檢查名字長度為2 OR 3
      middleName = name[1]; // 取第二字
    } else if ([4, 5].includes(name.length)) {
      // 檢查名字長度為4 or5
      middleName = name[2]; // 取第三字
    } else {
      continue;
    }

    if (!middleNames[middleName]) {
      middleNames[middleName] = [name]; //如果middle name不在dic, 建立新的key-value pair
    } else {
      middleNames[middleName].push(name); // Add the name to the list of names with the same middle name
    }
  }

  let uniqueNames = [];
  for (let middleName in middleNames) {
    if (middleNames[middleName].length === 1) {
      uniqueNames.push(middleNames[middleName][0]);
    }
  }
  if (uniqueNames.length > 0) {
    console.log(...uniqueNames); // Unpacking the list of unique names
  } else {
    console.log("沒有");
  }
}

func("彭大牆", "陳王明雅", "吳明"); // Should print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // Should print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // Should print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // Should print 夏曼藍波安

console.log("=================Task04==================");
function getNumber(index) {
  let sequence = [0];
  for (let i = 1; i <= index; i++) {
    if (i % 3 === 1) {
      sequence.push(sequence[sequence.length - 1] + 4);
    } else if (i % 3 === 2) {
      sequence.push(sequence[sequence.length - 1] + 4);
    } else {
      sequence.push(sequence[sequence.length - 1] - 1);
    }
  }
  console.log(sequence[sequence.length - 1]);
  return sequence;
}

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
