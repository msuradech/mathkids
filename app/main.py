from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import pages


def create_app():
    app = FastAPI()

    # static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # include routers
    app.include_router(pages.router)

    return app


app = create_app()
