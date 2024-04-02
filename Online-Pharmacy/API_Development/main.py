from fastapi import FastAPI
from pymongo import MongoClient
from models import Products, Users, Pharmacists
import json
from uuid import UUID, uuid4

app = FastAPI()

DatabaseNname = "Online-Pharmacy"
ProdColName = "ProductDetails"
UserColName = "UserDetails"
PharmacistColName = "PharmacistDetails"


client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.5')

db = client[DatabaseNname]
ProdCollection = db[ProdColName]
UserCollection = db[UserColName]
PharmacistCollection = db[PharmacistColName]


# home
@app.get("/")
async def root():
    return {"Hello" : "Vishv"}


# get all data
@app.get("/products")
async def fetchProducts():
    data_cursor = ProdCollection.find()
    data_list = []

    for document in data_cursor:
        document["_id"] = str(document["_id"])
        data_list.append(document)

    return data_list


# add product data - only admin has access to this
@app.post("/products/add")
async def addProducts(product: Products):
    try:
        ProdCollection.insert_one(product.dict())
    except Exception as e:
        print(e)
    return {"id": product._id}


# get specific product data
@app.get("/products/{product_name}")
async def fetchAllProducts(product_name: str):
    data_cursor = ProdCollection.find({
        "ProductName": {
            "$regex": product_name,
            "$options": 'i'
        }
    })

    data_list = []

    for document in data_cursor:
        document["_id"] = str(document["_id"])
        data_list.append(document)

    return list(data_list)


# user registration
@app.post("/users/add")
async def registerUser(user: Users):
    try:
        UserCollection.insert_one(user.dict())
    except Exception as e:
        print(e)
    return {"id": user._id}


# get user details
@app.get("/users/{userEmail}")
async def getUserDetails(userEmail: str):
    data_cursor = UserCollection.find({
        "UserEmail": {
            "$regex": userEmail,
            "$options": 'i'
        }
    })
    
    data_list = []

    for document in data_cursor:
        document["_id"] = str(document["_id"])
        data_list.append(document)

    return data_list


# pharamacist registration
@app.post("/pharamacist/add")
async def registerPharamacist(pharamacist: Pharmacists):
    try:
        PharmacistCollection.insert_one(pharamacist.dict())
    except Exception as e:
        print(e)
    return {"id": pharamacist._id}


# get pharamacist details
@app.get("/pharamacist/{phmEmail}")
async def getUserDetails(phmEmail: str):
    
    data_cursor = PharmacistCollection.find({
        "PhmEmail": {
            "$regex": phmEmail,
            "$options": 'i'
        }
    })

    data_list = []

    for document in data_cursor:
        document["_id"] = str(document["_id"])
        data_list.append(document)

    return list(data_list)  