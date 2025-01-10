from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from jose import JWSError,jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext


DATABASE_URL = "sqlite:///./supermarket.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer,ForeignKey("products.quantity"))
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

Base.metadata.create_all(bind=engine)