from pydantic import BaseModel, Field

# Create a Pydantic model for the Shipping
class ShippingInfo(BaseModel):
    status: str = Field(..., example='Pending')
    customer: int = Field(..., example=3)

    class Config:
        orm_mode = True


class ShippingInfoID(ShippingInfo):
    id: int