# from fastapi import FastAPI, Request,Form
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import RedirectResponse
# # from fastapi.middleware.sessions import SessionMiddleware
# app = FastAPI() #fastapi　object

# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="home.html"
#     )
#######
#
# @app.post("/signin")
# async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
#     if not username or not password:
#         return RedirectResponse(url="/error?message=請輸入使用者名稱和密碼", status_code=303)
    
#     if username == "test" and password == "test":
#         return RedirectResponse(url="/member", status_code=303)
#     else:
#         return RedirectResponse(url="/error?message=帳號、或密碼輸入錯誤", status_code=303)

# @app.get("/member")
# async def member(request: Request):
#     return templates.TemplateResponse("member.html", {"request": request})

# @app.get("/error")
# async def error(request: Request, message: str):
#     return templates.TemplateResponse("error.html", {"request": request, "message": message})

# @app.get("/signout")
# async def signout(request: Request):
#     request.session["signed_in"] = False
#     return RedirectResponse(url="/")


#####
# from fastapi import FastAPI, Request, Form, HTTPException
# from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.sessions import SessionMiddleware

# app = FastAPI()

# app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

# @app.post("/signin")
# async def signin(request: Request, username: str = Form(...), password: str = Form(...), checkbox: bool = Form(...)):
#     if not checkbox:
#         return templates.TemplateResponse("error.html", {"request": request, "message": "Please check the checkbox first"})
#     if username == "test" and password == "test":
#         request.session["signed_in"] = True
#         return RedirectResponse(url="/member")
#     else:
#         return templates.TemplateResponse("error.html", {"request": request, "message": "Username or password is not correct"})

# @app.get("/member")
# async def member(request: Request):
#     if "signed_in" not in request.session or not request.session["signed_in"]:
#         return RedirectResponse(url="/")
#     return templates.TemplateResponse("member.html", {"request": request})

# @app.get("/signout")
# async def signout(request: Request):
#     request.session["signed_in"] = False
#     return RedirectResponse(url="/")

# @app.get("/error")
# async def error(request: Request, message: str):
#     return templates.TemplateResponse("error.html", {"request": request, "message": message})
####
# @app.post("/signin")
# async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
#     if not username or not password:
#         return templates.TemplateResponse("error.html", {"request": request, "message": "請輸入使用者名稱和密碼"})
    
#     if username == "test" and password == "test":
#         return templates.TemplateResponse("member.html", {"request": request})
#     else:
#         return templates.TemplateResponse("error.html", {"request": request, "message": "帳號、或密碼輸入錯誤"})
###

from fastapi import FastAPI, Request, Form, Response, status
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
    

    if username == "test" and password == "test":
        request.session["signed_in"] = True
        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
    else:
        error_message = urlencode({"message": "帳號、或密碼輸入錯誤"})
        return RedirectResponse(url=f"/error?{error_message}", status_code=status.HTTP_302_FOUND)

@app.get("/member")
async def member(request: Request):
    if not request.session.get("signed_in"):
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/error")
async def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.get("/signout")
async def signout(request: Request):
    request.session["signed_in"] = False
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)