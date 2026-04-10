from fastapi import Request, HTTPException
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

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

def change_user_password(conn, username: str, current_password: str, new_password: str):

    cursor = conn.cursor()

    # get current hash
    cursor.execute("""
        SELECT password_hash
        FROM mathkids.users
        WHERE username = :username
    """, {"username": username})

    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    stored_hash = row[0]

    # verify current password
    if not verify_password(current_password, stored_hash):
        raise HTTPException(status_code=400, detail="Current password is incorrect")

    # prevent reuse
    if verify_password(new_password, stored_hash):
        raise HTTPException(status_code=400, detail="New password must be different")

    # validate
    if len(new_password) < 6:
        raise HTTPException(status_code=400, detail="Password too short")

    # hash new password
    new_hash = hash_password(new_password)

    # update
    cursor.execute("""
        UPDATE mathkids.users
        SET password_hash = :new_hash
        WHERE username = :username
    """, {
        "new_hash": new_hash,
        "username": username
    })

    conn.commit()

def get_current_user(request: Request):
    user_id = request.session.get("user_id")
    role = request.session.get("role")

    if not user_id:
        return None  # guest

    return {
        "user_id": user_id,
        "role": role
    }