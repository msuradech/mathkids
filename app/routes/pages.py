from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from services.quiz_service import generate_questions, get_mode_config
from db.oci import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class QuizResult(BaseModel):
    level: str
    totalQuestions: int
    score: int
    totalTime: int
    avgTime: float

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@router.post("/quiz/record")
def receive_quiz_result(data: QuizResult):
    print("=== Quiz Result ===")
    print(data)

    return {
        "status": "ok",
        "message": "received"
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