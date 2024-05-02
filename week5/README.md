## TASK2:Create database and table in your MySQL server
● Create a new database named website.  
CREATE database website;
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task2_1.png)  
● Create a new table named member, in the website database, designed as below:  
CREATE TABLE member (  
  id BIGINT AUTO_INCREMENT PRIMARY KEY,  
  name VARCHAR(255) NOT NULL,   
  username VARCHAR(255) NOT NULL,  
  password VARCHAR(255) NOT NULL,  
  follower_count INT UNSIGNED NOT NULL DEFAULT 0,  
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP  
);
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task2_2.png)


## TASK3:
●  INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.   
INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_1-1.png)   
INSERT INTO member (name, username, password)   
VALUES   
('John Doe', 'johndoe', 'password123'),   
('Jane Smith','janesmith', 'qwerty'),   
('Mike Johnson', 'mikejohnson', 'abc123'),   
('Emily Brown', 'emilybrown', 'p@ssw0rd');  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_1-2.png)  
●  SELECT all rows from the member table.  
SELECT * FROM member;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_2.png)  
●  SELECT all rows from the member table, in descending order of time.   
SELECT * FROM member ORDER BY time DESC;     
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_3.png)  
●  SELECT total 3 rows, second to fourth, from the member table, in descending order  of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.   
SELECT * FROM member ORDER BY time DESC LIMIT 1, 3;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_4.png)  
●  SELECT rows where username equals to test.   
SELECT * FROM member WHERE username = 'test';  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_5.png)  
●  SELECT rows where name includes the es keyword.   
SELECT * FROM member WHERE name LIKE '%es%';  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_6.png)  
●  SELECT rows where both username and password equal to test.   
SELECT * FROM member WHERE username = 'test' AND password = 'test';  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_7.png)  
●  UPDATE data in name column to test2 where username equals to test.   
UPDATE member SET name = 'test2' WHERE username = 'test';   
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task3_8.png)  


## TASK4:
●  SELECT how many rows from the member table.   
SELECT COUNT(*) FROM member;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task4_1.png)  
●  SELECT the sum of follower_count of all the rows from the member table.   
SELECT SUM(follower_count) FROM member;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task4_2.png)  
●  SELECT the average of follower_count of all the rows from the member table.   
SELECT AVG(follower_count) FROM member;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task4_3.png)  
●  SELECT the average of follower_count of the first 2 rows, in descending order of  follower_count, from the member table.   
SELECT   
AVG(follower_count)   
FROM (  
SELECT follower_count  
FROM member  
ORDER BY follower_count DESC  
LIMIT 2  
) AS top_2_members;    
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task4_4.png)  
## TASK5:
● Create a new table named message, in the website database. designed as below:   
CREATE TABLE message (  
id BIGINT PRIMARY KEY AUTO_INCREMENT,  
member_id BIGINT NOT NULL,  
content VARCHAR(255) NOT NULL,  
like_count INT UNSIGNED NOT NULL DEFAULT 0,  
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,  
FOREIGN KEY (member_id) REFERENCES member(id)  
);  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task5_1.png)  
加入五筆測資：    
INSERT INTO message (member_id,content,like_count)  
VALUES  
(1,'good',2),  
(2,'hello',4),  
(3,'happy',6),  
(4,'yes',8),  
(5,'bad',10);  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task5_1-2.png)  
●  SELECT all messages, including sender names. We have to JOIN the member table to get that.   
SELECT  
    m.id,  
    m.content,  
    m.like_count,  
    m.time,  
    b.name AS sender_name  
FROM  
    message m  
    JOIN member b ON m.member_id = b.id;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task5_2.png)  
●  SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.   
SELECT  
    m.id,  
    m.content,  
    m.like_count,  
    m.time,  
    b.name AS sender_name  
FROM  
    message m  
    JOIN member b ON m.member_id = b.id  
WHERE  
    b.username = 'test';  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task5_3.png)  
●  Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.    
SELECT  
    AVG(m.like_count) AS avg_like_count  
FROM  
    message m  
    JOIN member b ON m.member_id = b.id  
WHERE  
    b.username = 'test';  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task5_4.png)  
●  Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.    
SELECT  
    b.username,  
    AVG(m.like_count) AS avg_like_count  
FROM  
    message m  
    JOIN member b ON m.member_id = b.id  
GROUP BY  
    b.username;  
![](https://github.com/vincentchen0606/wehelp-stage1/blob/main/week5/week5_images/week5_task5_5.png)
