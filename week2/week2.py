print("=======================Task01==========================")
def find_and_print(messages, current_station):
    main_line = ["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian"]
    branch_line = ["Qizhang", "Xiaobitan"]

    min_distance = float('inf') #無限大
    nearest_friends = []

    for friend, message in messages.items():
        if any(station in message for station in main_line): #check message內的元素是否出現在main_line
            for station in main_line:
                if station in message:
                    distance = abs(main_line.index(current_station) - main_line.index(station))
                    if distance < min_distance:
                        min_distance = distance #替換最短距離
                        nearest_friends = [friend]
                    # elif distance == min_distance: #如果有兩個人都相同很近的話
                    #     nearest_friends.append(friend)
                    break
        elif any(station in message for station in branch_line): #check branch_line內的元素是否出現在message
            for station in branch_line:
                if station in message:
                    if current_station in branch_line:
                        distance = abs(branch_line.index(current_station) - branch_line.index(station))
                    else:
                        distance = abs(main_line.index("Qizhang") - main_line.index(current_station)) + 1
                    if distance < min_distance:
                        min_distance = distance
                        nearest_friends = [friend]
                    # elif distance == min_distance:
                    #     nearest_friends.append(friend)　#如果有兩個人都相同很近的話
                    break

    if nearest_friends: #only one friend,剛好可以去掉['']
        print(", ".join(nearest_friends))
    
messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian


print("=======================Task02==========================")

bookings = []

def book(consultants, hour, duration, criteria):
    global bookings #為了函式內修改全域變數
    end_hour = hour + duration #預定的結束時間
    
    #篩有空的顧問
    available_consultants = [consultant for consultant in consultants if not any(
        booking['name'] == consultant['name'] and 
        not (booking['end_hour'] <= hour or booking['start_hour'] >= end_hour)
        for booking in bookings
    )]
    
    # 如果沒有可用顧問 print "No Service"
    if not available_consultants:
        print("No Service")
        return
    
    # criteria篩選
    if criteria == "price":
        best_consultant = min(available_consultants, key=lambda x: x['price'])
    elif criteria == "rate":
        best_consultant = max(available_consultants, key=lambda x: x['rate'])
    
    # 加 booking to the bookings
    bookings.append({
        'name': best_consultant['name'],
        'start_hour': hour,
        'end_hour': end_hour
    })
    
    
    print(best_consultant['name'])


consultants=[
    {"name":"John", "rate":4.5, "price":1000}, 
    {"name":"Bob", "rate":3, "price":1200}, 
    {"name":"Jenny", "rate":3.8, "price":800}
]

book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate")   # John
book(consultants, 11, 1, "rate")   # Bob
book(consultants, 11, 2, "rate")   # No Service
book(consultants, 14, 3, "price") # John





print("=======================Task03==========================")
def func(*data):
    middle_names = {}
    for name in data:
        if len(name) in [2, 3]: #判斷名字長度2or3
            middle_name = name[1] #取第二字
        elif len(name) in [4, 5]: #判斷名字長度4or5
            middle_name = name[2] #取第三字
        else:
            continue
        
        if middle_name not in middle_names:
            middle_names[middle_name] = [name] #如果字不在dic則創新的key to value
        else:
            middle_names[middle_name].append(name) #把name加入key:middle_name的列表
    # print (middle_names)
        # print(middle_names.items())
        
    # unique_names = [names[0] for middle_name, names in middle_names.items() if len(names) == 1]
    unique_names = []
    for middle_name, names in middle_names.items():
        if len(names) == 1:
            unique_names.append(names[0])
    if unique_names:
        print(*unique_names) #unpacking list [' ']
    else:
        print("沒有")

func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安


print("=======================Task04==========================")
def get_number(index):
# your code here 
    sequence=[0]
    for i in range(1,index+1):

        if i%3==1:
            sequence.append(sequence[-1]+4)
        elif i%3==2:
            sequence.append(sequence[-1]+4)
        else:
            sequence.append(sequence[-1]-1)
    print(sequence[-1])
    return sequence
get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70




