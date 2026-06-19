# def greet():
#     print("Hello Baby")
# greet()    

from fastapi import FastAPI
from models import Product
from database import session, engine
import database_models

app = FastAPI()
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

@app.get("/products") #read
def get_all_products():
    # db connection
    db = session()
    # query
    db.query()
    return products

@app.get("/product/{id}") #read
def get_product_by_id(id : int):
    for product in products:
        if product.id == id:
            return product        
    return "Not Found B-"

@app.post("/product") #create
def add_product(product : Product):
    products.append(product)
    return product

@app.put("/product") #update
def update_product(id : int, product : Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"
    return "No Product Found"      

@app.delete("/product") #delete
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "Product Not Found"    