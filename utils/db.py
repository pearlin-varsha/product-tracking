from sqlalchemy import create_engine
from sqlalchemy import text
import logging

DATABASE_URL = "postgresql://pearlinvarsha:pearl%4012@localhost:5432/tracker"

def initialise_db():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    logging.info("connected successfully")
    print('a')
    return connection

def get_products(connection):
    try:
        result = connection.execute(
            text("SELECT * FROM products")
        )
        data = [dict(row._mapping) for row in result]
        return data
    except Exception as e:
        logging.error(e)
        return False


def insert_product(conenction,name,quantity,price,description):
    try:
        conenction.execute(text("""
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
        conenction.commit()
        return True
    except Exception as e:
        logging.error(e)
        return False
    
def update_products(connection,id,price):
    try:
        connection.execute(
            text("update products set price =:price where id = :id"),
            {
                "price":price,
                "id":id
            }
        )
        connection.commit()
        return True
    except Exception as e:
        logging.error(e)
        return False
    
def delete_products(connection,id):
    try:
        connection.execute(
            text("delete from products where id = :id"),
            {
                "id":id
            }
        )
        connection.commit()
        return True
    except Exception as e:
        logging.error(e)
        return False
