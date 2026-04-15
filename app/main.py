from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from middleware.session import add_session_middleware
from routes import pages, auth, quiz, score, utils
from prometheus_fastapi_instrumentator import Instrumentator

def create_app():
    app = FastAPI()
    add_session_middleware(app)

    # static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # include routers
    app.include_router(pages.router)
    app.include_router(auth.router)
    app.include_router(quiz.router)
    app.include_router(score.router)
    app.include_router(utils.router)

    return app


app = create_app()
Instrumentator().instrument(app).expose(app)
