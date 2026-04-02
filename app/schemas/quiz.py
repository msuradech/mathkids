from pydantic import BaseModel

class QuizResult(BaseModel):
    quiz_level: str
    total_questions: int
    score: int
    total_time_sec: int