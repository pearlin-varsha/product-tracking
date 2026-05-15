from fastapi import FastAPI
from sqlalchemy import text
from utils.db import engine

app = FastAPI()

@app.get("/")
def get_products():
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from products")
        )
        data = [dict(row._mapping) for row in result]

    return data

@app.post("/add-products")
def add_products(name : str , quantity : int , price : int , description : str):
    with engine.connect() as conn:
        conn.execute(text("""
                          insert into products
                          (name,quantity,price,description) 
                          values
                          (:name, :quantity, :price, :description)
                          """),
                          {
                              "name":name,
                              "quantity":quantity,
                              "price":price,
                              "description":description
                          }
                    )
        conn.commit()
    return{"message":"added successfully"}

@app.put("/update-product/{product_id}")
def update_product(product_id : int , price:int):
    with engine.connect() as conn:
        conn.execute(
            text("update products set price =:price where id = :id"),
            {
                "price":price,
                "id":product_id
            }
        )
        conn.commit()
    return{"Message ":" product updated successfully"}

@app.delete("/delete-product/{product_id}")
def delete_product(product_id:int):
    with engine.connect() as conn:
        conn.execute(
            text("delete from products where id = :id"),
            {
                "id":product_id
            }
        )
        conn.commit()
    return{"message":"product deleted successfully"}