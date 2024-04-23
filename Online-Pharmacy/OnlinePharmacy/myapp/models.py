from django.db import models

# Create your models here.
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Orders(str, Enum):
    OrderId = ""
    OrderDate = ""
    OrderDetails = ""
    OrderTotal = ""


class Role(str, Enum):
    admin = "Admin"
    user = "User"
    pharmacist = "Pharmacist"


class Products(BaseModel):
    _id: Optional[str] = str(uuid4())
    ProductName: str
    ProductPrice: float
    ProductManufactorer: str
    ProductDescription: str
    ProductComposition: str
    ProductUse: str
    ProductBenefits: str
    ProductSideEffects: str


class Users(BaseModel):
    _id: Optional[UUID] = uuid4()
    UserEmail: str
    ContactNumber: str
    FName: str
    LName: str
    DateofBirth: str
    UserAddress: str
    UserCity: str
    UserState: str
    UserPincode: str
    Gender: Gender
    Orders: List[Orders]


class Pharmacists(BaseModel):
    _id: Optional[UUID] = uuid4()
    PhmEmail: str
    ContactNumber: str
    FName: str
    LName: str
    PharmacyStore: str
    PharmacyAddress: str
    PharmacyCity: str
    PharmacyState: str
    PharmacyPincode: str


class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    #gender: Optional[Gender]
    #roles: Optional[List[Role]]