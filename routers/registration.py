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

@router.get("/")
def registration(request: Request):
    return templates.TemplateResponse("overview.html", {"request": request})

@router.get("/registration")
def registration(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})


@router.post("/registration")
def read_user_me(request: Request, email: str=Form(...), password: str=Form(...), db: Session = Depends(get_database_session)):
    existing_user = db.query(models.User).filter_by(email=email).first()
    if existing_user:
        errors = "Email already registered"
        return templates.TemplateResponse("auth/register.html", {"request": request, "errors": errors})
    else:
        db_user = models.User(email=email, password=password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return RedirectResponse(url="/login", status_code=303)


@router.get("/login")
def read_root(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})
