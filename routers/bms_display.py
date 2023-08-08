from fastapi import APIRouter, Form, Request, Depends
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from databases import get_database_session
from sqlalchemy.orm import Session
import schema
import models
import requests
from models import User as ModelUser
from routers.login import oauth2_scheme, get_current_user

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@router.get("/product")
def product_display(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    response_data = requests.get('https://awstest.sperentes.com/ws/rutuja/product-access', data={'secret_key':current_user.secret_key})
    return templates.TemplateResponse("bms/product.html", {"request": request, "product":response_data.json()})

@router.get("/invoice")
def invoice_display(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    response_data = requests.get('https://awstest.sperentes.com/ws/rutuja/invoice-access',
                                 data={'secret_key': current_user.secret_key})
    return templates.TemplateResponse("bms/invoice.html", {"request": request, "invoice":response_data.json()})

@router.get("/company")
def company_display(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    response_data = requests.get('https://awstest.sperentes.com/ws/rutuja/company-access',
                                 data={'secret_key': current_user.secret_key})
    return templates.TemplateResponse("bms/company.html", {"request": request, "company":response_data.json()})

@router.get("/customer_details")
def customer_display(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    response_data = requests.get('https://awstest.sperentes.com/ws/rutuja/customer-access',
                                 data={'secret_key': current_user.secret_key})
    return templates.TemplateResponse("bms/customer_details.html", {"request": request, "customer":response_data.json()})

@router.get("/payment_details")
def payment_display(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    response_data = requests.get('https://awstest.sperentes.com/ws/rutuja/payment-access',
                                 data={'secret_key': current_user.secret_key})
    return templates.TemplateResponse("bms/payment_paid.html", {"request": request, "payment":response_data.json()})
