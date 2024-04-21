import urllib.request as request
import json
import csv
src_1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src_2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

with request.urlopen(src_1) as response:# 讀取第一個網址的資料
    data_1=json.load(response)           #利用json模組　處理json資料格式
with request.urlopen(src_2) as response:# 讀取第二個網址的資料
    data_2 = json.load(response)
# 將第二個網址的資料轉換為以 SERIAL_NO 為key的字典
district_dic = {item["SERIAL_NO"]: item["address"].split()[1][0:3] for item in data_2["data"]}
with open("spot.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    # writer.writerow(["SpotTitle", "District", "Longitude", "Latitude", "ImageURL"])
    # 遍歷第一個網址的資料
    for item in data_1["data"]["results"]:
        serial_no = item["SERIAL_NO"]
        Spot_title = item["stitle"]
        Longitude = item["longitude"]
        Latitude = item["latitude"]
        ImageURL = item["filelist"].split("https:")[1]  # 取第一個圖片網址
        # 從第二個網址的資料中獲取對應的 district
        District = district_dic.get(serial_no, "")
        # 寫入一行資料到 CSV 檔案
        writer.writerow([Spot_title, District, Longitude, Latitude, ImageURL])




# 建立一個字典，用於存儲每個MRT對應的stitle列表
mrt_stitle_dict = {}

# 遍歷data2，獲取每個MRT和對應的SERIAL_NO
for item in data_2["data"]:
    mrt = item["MRT"]
    serial_no = item["SERIAL_NO"]
    
    if mrt not in mrt_stitle_dict:
        mrt_stitle_dict[mrt] = []
    
    # 在data1中查找對應的stitle
    for attraction in data_1["data"]["results"]:
        if attraction["SERIAL_NO"] == serial_no:
            mrt_stitle_dict[mrt].append(attraction["stitle"])
            break

# 將結果寫入CSV檔案
with open("mrt.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    for mrt, stitles in mrt_stitle_dict.items():
        row = [mrt] + stitles
        writer.writerow(row)