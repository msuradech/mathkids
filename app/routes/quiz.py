from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.db_service import insert_quiz_result
from services.quiz_service import generate_questions, get_mode_config
from schemas.quiz import QuizResult

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/quiz/record")
def submit_quiz(req: QuizResult):
    user_id = insert_quiz_result(
        quiz_level=req.quiz_level,
        total_questions=req.total_questions,
        score=req.score,
        total_time_sec=req.total_time_sec
    )

    return {
        "status": "ok",
        "user_id": user_id
    }

@router.get("/quiz/01/{mode}", response_class=HTMLResponse)
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