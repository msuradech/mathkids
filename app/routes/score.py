from fastapi import APIRouter
from services.score_service import get_score_daily_service, get_score_monthly_service

router = APIRouter()

@router.get("/score/daily/{user_id}")
def get_score_daily(user_id: int):
    data = get_score_daily_service(user_id)

    return {
        "status": "success",
        "data": data
    }

@router.get("/score/monthly/{user_id}")
def get_score_monthly(user_id: int):
    data = get_score_monthly_service(user_id)

    return {
        "status": "success",
        "data": data
    }
