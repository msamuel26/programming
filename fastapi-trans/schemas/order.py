from pydantic import BaseModel, Field


# Create a Pydantic model for the Order
class OrderInfo(BaseModel):
    item: str = Field(..., example="Monitor")
    amount: int = Field(..., example=10000)
    customer_id: int = Field(..., example=3)

    class Config:
        orm_mode = True


class OrderInfoID(OrderInfo):
    id: int