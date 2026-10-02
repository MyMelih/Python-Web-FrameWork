from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Melih Trac"

products = [
    Product(id = 1,name = "Phone", description = "A smartphone", price = 998, quantity =  50),
    Product(id = 2,name = "Laptop", description = "A powerful laptop", price = 1099, quantity =  22),
    Product(id = 3,name = "Tablet", description = "A wooden tablet", price = 299, quantity =  147),
    Product(id = 4,name = "Pen", description = "A blue ink pen", price = 1.99, quantity =  58)
    
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products: 
        if product.id == id:
            return product
    return "Product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product
