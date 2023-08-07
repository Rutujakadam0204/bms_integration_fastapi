from fastapi import APIRouter, Form, Request, Depends
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from databases import get_database_session
from sqlalchemy.orm import Session
import schema
import models

@router.post("/product")
def product_display(request: Request):
    data = {'name': name, 'date': date}
    resp = requests.post("https://awstest.sperentes.com/ws/api_rutuja/product_post",data)
    print(resp)
    response = RedirectResponse('/product', status_code=303)
    return response
