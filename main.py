from fastapi import FastAPI
from routers import admin, customer

app = FastAPI()

<<<<<<< HEAD
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/newera/products", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    return crud.create_product(db=db, product=product)

@app.get("/newera/products/{product_id}", response_model=schemas.Product)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_product(db=db, product_id=product_id)

@app.put("/newera/products/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    return crud.update_product(db=db, product_id=product_id, product=product)

@app.delete("/newera/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    crud.delete_product(db=db, product_id=product_id)
    return {"message": "Product deleted"}

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#              MIJOZ XUSUSIYATLARI

@app.get("/newera/products", response_model=List[schemas.Product])
def list_products(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_products(db=db)

@app.post("/newera/orders", response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_order(db=db, order=order, user_id=current_user.id)

@app.get("/newera/orders/{customer_id}", response_model=List[schemas.Order])
def read_customer_orders(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.id != customer_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Autentifikatsiyadan o'ting")
    return crud.get_user_orders(db=db, user_id=customer_id)

@app.get("/newera/orders/{order_id}/status")
def read_order_status(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    order = crud.get_order(db=db, order_id=order_id)
    if order.customer_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Autentifikatsiyadan o'ting")
    return {"status": order.status}

@app.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email allaqachon ro'yxatdan o'tgan"
        )
    return crud.create_user(db=db, user=user)

@app.post("/signup/admin", response_model=schemas.User)
def create_admin(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email allaqachon ro'yxatdan o'tgan"
        )
    return crud.create_admin(db=db, user=user)
=======
# Customer routerini ulash
app.include_router(customer.router)

# Admin routerini ulash
app.include_router(admin.router)
>>>>>>> b623c5e7d907f28bb9129cd6d4d6561d68256e0a
