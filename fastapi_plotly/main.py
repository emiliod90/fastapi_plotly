from fastapi import FastAPI
from .routers import index

def init_app():
    app = FastAPI(title="Emilio FastAPI Demo")
    app.include_router(index.router)
    return app



