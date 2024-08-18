from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/combustivel")
templates = Jinja2Templates(directory = "templates")
