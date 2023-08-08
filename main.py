from fastapi import FastAPI,Request,Cookie
from databases import engine
import models
from routers import registration, bms_display, login

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(registration.router)
app.include_router(bms_display.router)
app.include_router(login.router)

