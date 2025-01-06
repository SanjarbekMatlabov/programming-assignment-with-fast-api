from pydantic import BaseModel
# from typing import List
class Admin(BaseModel):
    username: str
    password: str

class UserModel(BaseModel):
    username: str
    password: str
    
class ProductModel(BaseModel):
    name: str
    description: str
    quantity:int
    price: float

class OrderModel(BaseModel):
    user_id: str
    product_id: str
    quantity: int
    status: str = "pending"
