from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.quiz_service import generate_questions, get_mode_config

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@router.get("/quiz01/{mode}", response_class=HTMLResponse)
def quiz(request: Request, mode: str):
    total = get_mode_config(mode)
    questions = generate_questions(total)

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "questions": questions,
        "mode": mode
    }
)
