from models import product
from fastapi import FastAPI

app = FastAPI()

products = [
    product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
]

@app.get("/")
def greet():
    return {"message": "welcome"}

@app.get("/products")
def get_products():
    return products