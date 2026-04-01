from fastapi import Request, HTTPException
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def register_user(data, conn):

    # 1. check username
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM mathkids.USERS WHERE USERNAME = :username",
        {"username": data.username}
    )
    
    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # 2. check email
    cursor.execute(
        "SELECT 1 FROM mathkids.USERS WHERE EMAIL = :email",
        {"email": data.email}
    ).fetchone()

    existing_email = cursor.fetchone()

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    # 3. hash password
    password_hash = hash_password(data.password)

    # 4. insert
    cursor.execute("""
        INSERT INTO mathkids.USERS (
            USER_ID,
            USERNAME,
            PASSWORD_HASH,
            EMAIL,
            ROLE,
            ACCOUNT_STATUS,
            BIRTH_DATE,
            CREATED_AT,
            UPDATED_AT
        )
        VALUES (
            mathkids.USER_SEQ.NEXTVAL,
            :username,
            :password_hash,
            :email,
            'USER',
            'ACTIVE',
            :birth_date,
            :created_at,
            :updated_at
        )
    """, {
        "username": data.username,
        "password_hash": password_hash,
        "email": data.email,
        "birth_date": data.birth_date,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    })

    conn.commit()

    return {"message": "User registered successfully"}

def login_user(conn, username: str, password: str):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, username, password_hash, role
        FROM mathkids.users
        WHERE username = :username
    """, {"username": username})

    user = cursor.fetchone()

    if not user:
        return None

    user_id, db_username, db_password_hash, role = user

    if not pwd_context.verify(password, db_password_hash):
        return None

    return {
        "id": user_id,
        "username": db_username,
        "role": role
    }

def get_current_user(request: Request):
    user_id = request.session.get("user_id")
    role = request.session.get("role")

    if not user_id:
        return None  # guest

    return {
        "user_id": user_id,
        "role": role
    }