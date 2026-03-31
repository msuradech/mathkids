from fastapi import APIRouter, Depends
from schemas.user import RegisterRequest
from services.auth_service import register_user
from db.oci import get_connection

router = APIRouter()

@router.post("/register")
def register(data: RegisterRequest, db=Depends(get_connection)):
    return register_user(data, db)