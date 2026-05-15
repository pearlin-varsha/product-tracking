from fastapi import FastAPI
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

@app.post("/add-products")
def add_products(name : str , quantity : int , price : int , description : str):
    inserted=False
    inserted = insert_product(pg_connection,name, quantity,price, description)
    if inserted:
        return {"message":"added successfully"}
    else:
        return {"message":"insertion failed"}

@app.put("/update-product/{product_id}")
def update_product(product_id : str , price:int):
    updated=False
    updated = update_products(pg_connection,product_id,price)
    if updated:
        return{"Message ":" product updated successfully"}
    else:
        return{"Message ":" update failed"}

@app.delete("/delete-product/{product_id}")
def delete_product(product_id:str):
    deleted=False
    deleted=delete_products(pg_connection,product_id)
    if deleted:
        return{"message":"product deleted successfully"}
    else:
        return{"message":"product deletion failed"}