from datetime import date
from pydantic import BaseModel


class UserCreate(BaseModel):
    email : str
    password : str

class ProductDisplay(BaseModel):
    product_name : str


