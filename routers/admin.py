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

