from starlette.middleware.sessions import SessionMiddleware
from core.config import SECRET_KEY

def add_session_middleware(app):
    app.add_middleware(
        SessionMiddleware,
        secret_key=SECRET_KEY
    )