from fastapi import FastAPI
from routers import admin, customer

app = FastAPI()

# Customer routerini ulash
app.include_router(customer.router)

# Admin routerini ulash
app.include_router(admin.router)
