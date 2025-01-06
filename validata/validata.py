from pydantic import BaseModel
from typing import List
class Admin(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    password: str
    
class ProductModel(BaseModel):
    name: str
    description: str
    price: float

class OrderModel(BaseModel):
    user_id: str
    product_id: str
    quantity: int
    status: str = "pending"
