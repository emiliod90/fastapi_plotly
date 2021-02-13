from fastapi import FastAPI
from .views import index, api
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Emilio FastAPI Demo")
app.mount(
    "/static",
    StaticFiles(directory="fastapi_plotly/static"),
    name="static"
    )
app.include_router(index.router)
app.include_router(api.router)
