from fastapi import FastAPI, Depends, Request, Form, HTTPException,status
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from databases import engine
from starlette.responses import RedirectResponse
import models
from schema import UserCreate
import requests
from routers import registration, bms_display

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(registration.router)
app.include_router(bms_display.router)
# app.include_router(login.router)


#
# @app.get("/product")
# def product(request: Request):
#     movie_data = requests.get("http://127.0.0.1:8001/ok/ok")
#     movie_data=movie_data.json()
#     # records = db.query(Movie).all()
#     return templates.TemplateResponse("overview.html", {"request": request, "movie_data": movie_data})
#
# @app.post("/product")
# def product_create(request: Request, name: str = Form(...), date: str = Form(...)):
#     print(date)
#     data = {'name':name, 'date':date}
#     resp = requests.post("http://127.0.0.1:8001/ok/ok",data)
#     print(resp)
#     response = RedirectResponse('/product', status_code=303)
#     return response
#
#
# # @app.post("/movie/")
# # async def create_movie(db: Session = Depends(get_database_session), name: Movie.name = Form(...), url: schema.Movie.url = Form(...), rate: schema.Movie.rating = Form(...), type: schema.Movie.type = Form(...), desc: schema.Movie.desc = Form(...)):
# #     movie = Movie(name=name, url=url, rating=rate, type=type, desc=desc)
# #     db.add(movie)
# #     db.commit()
# #     response = RedirectResponse('/', status_code=303)
# #     return response
#
#
#
#
#
#
# # @app.get("/movie/{name}", response_class=HTMLResponse)
# # def read_movie(request: Request, name: schema.Movie.name, db: Session = Depends(get_database_session)):
# #     item = db.query(Movie).filter(Movie.id==name).first()
# #     print(item)
# #     return templates.TemplateResponse("overview.html", {"request": request, "movie": item})
#
#
# @app.post("/register")
# def register_user(user: UserCreate, session: Session = Depends(get_database_session)):
#     existing_user = session.query(models.User).filter_by(email=user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#
#     encrypted_password =get_hashed_password(user.password)
#
#     new_user = models.User(username=user.username, email=user.email, password=encrypted_password )
#
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#
#     return {"message":"user created successfully"}
#
#
#
# # registration
#
# @app.get("/register")
# def register(request: Request):
#     return templates.TemplateResponse("auth/register.html",{"request":request})
#
# @app.post("/register")
# def register(request: Request, email: str = Form(...), password: str= Form(...), db: Session = Depends(get_database_session)):
#     print(Form(...))
#     errors = []
#     try:
#         user = UserCreate(email=email,password=password)
#         create_new_user(user=user, db=db)
#         return responses.RedirectResponse("/?alert=Successfully%20Registered",status_code=status.HTTP_302_FOUND)
#     except ValidationError as e:
#         errors_list = json.loads(e.json())
#         for item in errors_list:
#             errors.append(item.get("loc")[0]+ ": " + item.get("msg"))
#         return templates.TemplateResponse("auth/register.html",{"request":request,"errors":errors})
#
