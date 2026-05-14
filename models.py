from pydantic import BaseModel
import uuid

class product(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    price: float
    quantity: int