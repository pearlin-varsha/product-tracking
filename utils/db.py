from sqlalchemy import create_engine
DATABASE_URL = "postgresql://pearlinvarsha:pearl%4012@localhost:5432/tracker"
engine = create_engine(DATABASE_URL)
connection = engine.connect()
print("connected successfully")
