from fastapi import FastAPI, Request, Form, Response, status
import mysql.connector
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette_session import SessionMiddleware
from urllib.parse import urlencode
app = FastAPI()  # fastapi object

app.add_middleware(SessionMiddleware, secret_key="your-secret-key", cookie_name="session")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if username is None or password is None:
        error_message = urlencode({"message": "請輸入帳號、密碼"})
        return RedirectResponse(url=f"/error?{error_message}", status_code=status.HTTP_302_FOUND)
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            # port:8000,解決reload問題！很重要
            user="root",
            password="98zcya7e88",
            database="website",
            charset = "utf8",
        )
        cursor = db.cursor()

        query = "SELECT * FROM member WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            request.session["id"] = str(user[0])  # 將 user[0] 轉換為字符串類型
            request.session["name"] = str(user[1])  # 將 user[1] 轉換為字符串類型
            request.session["username"] = str(user[2])  # 將 user[2] 轉換為字符串類型
            request.session["signed_in"] = True
            return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
        else:
            error_message = urlencode({"message": "Username or password is not correct"})
            return RedirectResponse(url=f"/error?{error_message}", status_code=status.HTTP_302_FOUND)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


@app.get("/member")
async def member(request: Request):
    if not request.session.get("signed_in"):
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    name = request.session.get("name")
    
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="98zcya7e88",
            database="website",
            charset="utf8",
        )
        cursor = db.cursor()

        query = "SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id = member.id ORDER BY message.id DESC"
        cursor.execute(query)
        messages = cursor.fetchall()

        return templates.TemplateResponse("member.html", {"request": request, "name": name, "messages": messages})
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

@app.get("/error")
async def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.post("/signup")
async def signup(request: Request, name: str = Form(None), username: str = Form(None), password: str = Form(None)):
    if name is None or username is None or password is None:
        error_message = urlencode({"message": "請輸入姓名、帳號和密碼"})
        return RedirectResponse(url=f"/error?{error_message}", status_code=status.HTTP_302_FOUND)
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            # port=8000, 解決reload問題！很重要
            user="root",
            password="98zcya7e88",
            database="website",
            charset = "utf8",
        )
        cursor = db.cursor()

    # 檢查用戶名是否已存在
        query = "SELECT * FROM member WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        existing_user = cursor.fetchone()

        if existing_user:
            error_message = urlencode({"message": "Repeated username"})
            return RedirectResponse(url=f"/error?{error_message}", status_code=status.HTTP_302_FOUND)
        else:
            # 插入新用戶
            query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            values = (name, username, password)
            cursor.execute(query, values)
            db.commit()
            return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

@app.post("/createMessage")
async def create_message(request: Request, content: str = Form(...)):
    member_id = request.session.get("id")
    
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="98zcya7e88",
            database="website",
            charset="utf8",
        )
        cursor = db.cursor()

        query = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
        values = (member_id, content)
        cursor.execute(query, values)
        db.commit()

        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

#Member Query
@app.get("/api/member")
async def member_query(request: Request, username: str):
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="98zcya7e88",
            database="website",
            charset="utf8",
        )
        cursor = db.cursor()

        query = "SELECT id, name, username FROM member WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            return {"data": {"id": user[0], "name": user[1], "username": user[2]}}
        else:
            return {"data": None}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

# 實現姓名更新邏輯
@app.patch("/api/member")
async def update_name(request: Request):
    data = await request.json()
    new_name = data.get("name")
    member_id = request.session.get("id")

    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="98zcya7e88",
            database="website",
            charset="utf8",
        )
        cursor = db.cursor()

        query = "UPDATE member SET name = %s WHERE id = %s"
        values = (new_name, member_id)
        cursor.execute(query, values)
        db.commit()

        if cursor.rowcount > 0:
            request.session["name"] = new_name  # 將新的姓名存到session中解決reload頁面名字問題
            return {"ok": True}
        else:
            return {"error": True}
    except mysql.connector.Error as error:
        print(f"Failed to update name: {error}")
        return {"error": True}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()