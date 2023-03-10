from pydantic import BaseModel, Field

# Create a Pydantic model for the Customer
class CustomerInfo(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    age: int = Field(..., example=23)
    country: str = Field(..., example='USA')

    class Config:
        orm_mode = True