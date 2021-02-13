from fastapi import FastAPI
from .routers import index

app = FastAPI(title="Emilio FastAPI Demo")
app.include_router(index.router)
