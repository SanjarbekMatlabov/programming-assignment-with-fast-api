from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from  auth import *
from crud import *
import crud,models,auth,schemas,database
from  models import *
from schemas import *
from database import SessionLocal, engine
from typing import List
import auth
from fastapi import APIRouter
router = APIRouter(
    prefix="/newera/admin",
    tags = ['Admin']
    )
@router.post("/products", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    return crud.create_product(db=db, product=product)
@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    return crud.update_product(db=db, product_id=product_id, product=product)
@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    crud.delete_product(db=db, product_id=product_id)
    return {"message": "Product deleted"}
@router.get("/orders/{customer_id}", response_model=List[schemas.Order])
def read_customer_orders(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.id != customer_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin uchun")
    return crud.get_user_orders(db=db, user_id=customer_id)

@router.get("/orders/{order_id}/status")
def read_order_status(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    order = crud.get_order(db=db, order_id=order_id)
    if order.customer_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin uchun")
    return {"status": order.status}
# @router.post("/signup/admin", response_model=schemas.User)
# def create_admin(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     current_user: models.User = Depends(get_current_admin_user)
#     if db_user:
#         raise HTTPException(
#             status_code=400,
#             detail="Email allaqachon ro'yxatdan o'tgan"
#         )
#     return crud.create_admin(db=db, user=user)