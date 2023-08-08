from fastapi import Depends, APIRouter, HTTPException, status, Response, Request
from pydantic import BaseModel
from databases import get_database_session
from sqlalchemy.orm import Session
from models import User as ModelUser
from typing import Optional
from typing_extensions import Annotated
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from starlette.responses import RedirectResponse
from datetime import datetime,timedelta
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    email: str

def get_user(email:str,db: Session= Depends(get_database_session)):
    user = db.query(ModelUser).filter(ModelUser.email == email).first()
    return user

# get current user logged in
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(email=username, db=db)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


class Token(BaseModel):
    access_token: str
    token_type: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


class Settings:
    PROJECT_NAME:str = "Rutuja Kadam"
    PROJECT_VERSION: str = "1.0.0"
    SECRET_KEY :str = "SECRET_KEY"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
settings = Settings()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
        print("false")
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_database_session)):
    user = authenticate_user(form_data.username, form_data.password, db)
    print(form_data.username, form_data.password)
    if not user:
        # return {'message':"Incorrect username or password"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(
        data={"sub": user.email}
    )
    response.delete_cookie("access_token")
    response.set_cookie(key="access_token", value=access_token)
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_session), current_user: ModelUser=Depends(get_current_user)):
    print(current_user)
    return current_user

@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": 'deleted', "token_type": "bearer"}
