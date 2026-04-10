from pydantic import BaseModel, EmailStr
from datetime import date

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    birth_date: date

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str