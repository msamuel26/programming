from pydantic import BaseModel, Field


# Create a Pydantic model for the Order
class AccountInfo(BaseModel):
    account_number: str = Field(..., example="1039009900")
    balance: int = Field(..., example=2500)
    customer_id: int = Field(..., example=1)

    class Config:
        orm_mode = True


class AccountInfoID(AccountInfo):
    id: int