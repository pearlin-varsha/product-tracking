from fastapi import FastAPI, Request
from models import product
from sqlalchemy import text
from utils.db import initialise_db, insert_product,update_products,delete_products,get_products

app = FastAPI()

pg_connection = initialise_db()

@app.get("/")
def get_product():
    data = get_products(pg_connection)
    if data is not False:
        return data
    else:
        return {"message": "failed"}

@app.post("/product/add/")
def add_product(product: product):
    inserted=False
    inserted = insert_product(pg_connection,product.name, product.quantity,product.price, product.description)
    if inserted:
        return {"message":"added successfully"}
    else:
        return {"message":"insertion failed"}

@app.put("/product/update/{product_id}")
def update_product(product: product):
    updated=False
    updated = update_products(pg_connection,product.product_id,product.price)
    if updated:
        return{"Message ":" product updated successfully"}
    else:
        return{"Message ":" update failed"}

@app.delete("/delete-product/{product_id}")
def delete_product(product: product):
    deleted=False
    deleted=delete_products(pg_connection,product.product_id)
    if deleted:
        return{"message":"product deleted successfully"}
    else:
        return{"message":"product deletion failed"}