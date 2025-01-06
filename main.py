# main.py
from fastapi import FastAPI
from validata.validata import *
from models.model import *
app = FastAPI()

@app.post('/api/products/create')

def create_product(product: ProductModel):
    db = session()
    new_product = Product(name = product.name, description = product.description, price = product.price,quantity = product.quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()
    return new_product

@app.get("/api/products/get")
def get_flights():
    db = session()
    data = db.query(Product).all()
    db.close()
    return list(data)

@app.put("/api/products/update/{id}")
def update_product(id: int, product: ProductModel):
    db = session()
    product_to_update = db.query(Product).filter(Product.id == id).first()
    if not product_to_update:
        return {"message": "Product not found"}
    product_to_update.name = product.name
    product_to_update.description = product.description
    product_to_update.price = product.price
    product_to_update.quantity = product.quantity
    db.commit()
    db.close()
    return "Succesfully update"

@app.delete("/api/products/delete/{id}")
def delete_product(id: int):
    db = session()
    product_to_delete = db.query(Product).filter(Product.id == id).first()
    if not product_to_delete:
        return {"message": "Product not found"}
    db.delete(product_to_delete)
    db.commit()
    db.close()
    return "Product deleted successfully"

@app.post("/api/orders/create")
def create_order(order: OrderModel):
    db = session()
    new_order = Order(user_id = order.user_id, product_id = order.product_id, quantity = order.quantity)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()
    return new_order

@app.get("/api/orders/get/{user_id}")
def get_orders(user_id: int):
    db = session()
    data = db.query(Order).filter(Order.user_id == user_id).all()
    db.close()
    return list(data)
@app.post("/api/user/")
def create_user(user: UserModel):
    db = session()
    new_user = User(login = user.username, password = user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user