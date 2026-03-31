from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from services.quiz_service import generate_questions, get_mode_config
from services.db_service import insert_quiz_result
from db.oci import get_connection
from schemas.quiz import QuizResult

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )

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

@router.get("/test-db")
def test_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT SYSDATE FROM dual")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "status": "success",
            "sysdate": str(result[0])
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }