from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    product_name: str
    quantity: int


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    product_name: str
    quantity: int
    status: str

    model_config = {
        "from_attributes": True
    }