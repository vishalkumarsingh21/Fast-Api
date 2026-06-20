# def greet():
#     print("Hello Baby")
# greet()    

from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"]
)

database_models.Base.metadata.create_all(bind = engine)

@app.get("/") #read
def greet():
    return "JUST A DEMO"

products = [
    Product(id = 1, name = "Laptop", description = "Budget Gaming PC", price = 150000, quantity = 89),
    Product(id = 2, name = "SmartPhone", description = "Crazy Ass Phone", price = 100000, quantity = 85),
    Product(id = 3, name = "Fridge", description = "Electronic Appliance", price = 180000, quantity = 52),
    Product(id = 4, name = "Suit", description = "Clothings", price = 110000, quantity = 96)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()    

def init_db():
    db = session()
    count = db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()    
init_db()    

@app.get("/products") #read
def get_all_products(db : Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products 

@app.get("/products/{id}") #read
def get_product_by_id(id : int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product        
    return "Not Found B-"

@app.post("/products") #create
def add_product(product : Product, db : Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}") #update
def update_product(id : int, product : Product, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "Product Not Found XD"    

@app.delete("/products/{id}") #delete
def delete_product(id : int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    else:
        return "Product Not Found"    