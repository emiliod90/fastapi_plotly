from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="fastapi_plotly/templates")


@router.get("/api", response_class=HTMLResponse)
async def api(request: Request):
    return templates.TemplateResponse("api.html", {"request": request})
