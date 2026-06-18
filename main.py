# def greet():
#     print("Hello Baby")
# greet()    

from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "JUST A DEMO"

products = [
    Product(id = 1, name = "Laptop", description = "Budget Gaming PC", price = 150000, quantity = 89),
    Product(id = 2, name = "SmartPhone", description = "Crazy Ass Phone", price = 100000, quantity = 85),
    Product(id = 3, name = "Fridge", description = "Electronic Appliance", price = 180000, quantity = 52),
    Product(id = 4, name = "Suit", description = "Clothings", price = 110000, quantity = 96)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id : int):
    for product in products:
        if product.id == id:
            return product        
    return "Not Found B-"

@app.post("/product")
def add_product(product : Product):
    products.append(product)
    return product