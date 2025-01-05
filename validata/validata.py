from pydantic import BaseModel
from typing import List
class Admin(BaseModel):
    id: int
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    password: str
    
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    stock: int

class Order(BaseModel):
    id: str
    customer_id: str
    items: List[dict]
    status: str = "pending"
