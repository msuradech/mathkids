from fastapi import APIRouter, Depends, Request, Form, HTTPException
from schemas.user import RegisterRequest, ChangePasswordRequest
from services.auth_service import register_user, login_user, change_user_password
from db.oci import get_connection

router = APIRouter()

@router.post("/register")
def register(data: RegisterRequest, db=Depends(get_connection)):
    return register_user(data, db)

@router.get("/me")
def get_me(request: Request):
    user_id = request.session.get("user_id")

    if not user_id:
        return {"user": None}

    return {
        "user": {
            "user_id": user_id,
            "username": request.session.get("username"),
            "role": request.session.get("role")
        }
    }

@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    conn=Depends(get_connection)
):
    user = login_user(conn, username, password)

    if not user:
        return {"status": "error", "msg": "Invalid username or password"}

    # set session
    request.session["user_id"] = user["id"]
    request.session["username"] = user["username"]
    request.session["role"] = user["role"]

    return {"status": "ok"}

@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return {"status": "ok"}

@router.post("/change-password")
async def change_password(req: Request, body: ChangePasswordRequest):

    username = req.session.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Not logged in")

    conn = get_connection()

    change_user_password(
        conn=conn,
        username=username,
        current_password=body.current_password,
        new_password=body.new_password
    )

    return {"message": "Password updated successfully"}