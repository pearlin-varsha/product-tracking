from pydantic import BaseModel
import uuid
print("product init.")
class product(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    price: float
    quantity: int