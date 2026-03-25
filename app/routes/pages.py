from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.quiz_service import generate_questions

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_level_config(level: str):
    config = {
        "easy": 10,
        "normal": 20,
        "hard": 50
    }
    return config.get(level, 10)


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@router.get("/quiz/{level}", response_class=HTMLResponse)
def quiz(request: Request, level: str):
    total = get_level_config(level)
    questions = generate_questions(total)

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "questions": questions,
        "level": level
    }
)
