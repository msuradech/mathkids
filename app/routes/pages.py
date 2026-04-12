from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from services.db_service import get_all_user, get_result_history_by_user

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@router.get("/login", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

@router.get("/change-password", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="change-password.html",
        context={}
    )

@router.get("/quiz", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={}
    )

@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )

@router.get("/result-history", response_class=HTMLResponse)
def result_hitsory_page(request: Request):
    role = request.session.get("role")

    if role != "ADMIN":
        return RedirectResponse(url="/", status_code=303)  # ไป index.html

    users = get_all_user()

    return templates.TemplateResponse(
        request=request,
        name="result-history.html",
        context={
            "users": users
        }
    )

@router.get("/result-history/{user_id}")
def result_history_api(user_id: int):
    data = get_result_history_by_user(user_id)
    return {"data": data}