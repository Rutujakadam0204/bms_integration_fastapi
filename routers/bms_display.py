from fastapi import APIRouter, Form, Request, Depends
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from databases import get_database_session
from sqlalchemy.orm import Session
import schema
import models

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@router.get("/product")
def product_display(request: Request):
    return templates.TemplateResponse("bms/product.html", {"request": request})

@router.get("/invoice")
def registration(request: Request):
    return templates.TemplateResponse("bms/invoice.html", {"request": request})

@router.get("/company")
def product_display(request: Request):
    return templates.TemplateResponse("bms/product.html", {"request": request})

@router.get("/customer_details")
def registration(request: Request):
    return templates.TemplateResponse("bms/invoice.html", {"request": request})

@router.get("/payment_details")
def registration(request: Request):
    return templates.TemplateResponse("bms/invoice.html", {"request": request})
