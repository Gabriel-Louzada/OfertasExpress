from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/combustivel")
templates = Jinja2Templates(directory = "templates")

@router.get("/gasolina_comum", response_class=HTMLResponse)
async def get_raiz(request: Request):
    return templates.TemplateResponse("/combustivel/combustivel_gas_comum.html", {"request": request})


@router.get("/gasolina_adtivada", response_class=HTMLResponse)
async def get_raiz(request: Request):
    return templates.TemplateResponse("/combustivel/combustivel_gas_adtivada.html", {"request": request})

@router.get("/combustivel_etanol", response_class=HTMLResponse)
async def get_raiz(request: Request):
    return templates.TemplateResponse("/combustivel/combustivel_etanol.html", {"request": request})

@router.get("/combustivel_diesels10", response_class=HTMLResponse)
async def get_raiz(request: Request):
    return templates.TemplateResponse("/combustivel/combustivel_diesels10.html", {"request": request})

@router.get("/combustivel_diesels500", response_class=HTMLResponse)
async def get_raiz(request: Request):
    return templates.TemplateResponse("/combustivel/combustivel_diesels500.html", {"request": request})


