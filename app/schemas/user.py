from pydantic import BaseModel, EmailStr
from datetime import date

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    birth_date: date