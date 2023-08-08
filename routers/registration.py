from fastapi import APIRouter, Form, Request, Depends
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from databases import get_database_session
from sqlalchemy.orm import Session
import schema
from models import User as ModelUser
from routers.login import oauth2_scheme, get_current_user
from pydantic import BaseModel, Field

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@router.get("/")
def registration(request: Request):
    return templates.TemplateResponse("overview.html", {"request": request})

@router.get("/registration")
def registration(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

from routers.login import Hasher

@router.post("/registration")
def read_user_me(request: Request, email: str=Form(...), password: str=Form(...), db: Session = Depends(get_database_session)):
    existing_user = db.query(models.User).filter_by(email=email).first()
    if existing_user:
        errors = "Email already registered"
        return templates.TemplateResponse("auth/register.html", {"request": request, "errors": errors})
    else:
        password_hash = Hasher.get_password_hash(password)
        db_user = models.User(email=email, password=password_hash)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return RedirectResponse(url="/login", status_code=303)


@router.get("/login")
def read_root(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.get("/profile")
def read_profile(request:Request):

    return templates.TemplateResponse('auth/profile.html', {'request':request})

class ApiCreate(BaseModel):
    secret_key : str = Field(
        index=True,
        nullable=False,
    )
@router.post("/profile")
# api_key: ApiCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), current_user: User=Depends(get_current_user)
def post_profile(secret_key: ApiCreate,token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    filters = {"id": current_user.id}
    api = db.query(ModelUser).filter_by(**filters).first()

    api.secret_key = secret_key.secret_key
    db.add(api)
    db.commit()
    db.refresh(api)

    return {'message':'success'}
