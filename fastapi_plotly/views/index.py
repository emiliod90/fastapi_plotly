from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="fastapi_plotly/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, title="Hello"):
    return templates.TemplateResponse("index.html", {"request": request, "title": title})
