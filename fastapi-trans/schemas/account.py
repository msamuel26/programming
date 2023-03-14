from pydantic import BaseModel, Field, validator


# Create a Pydantic model for the Order
class AccountInfo(BaseModel):
    account_number: str = Field(..., example="1039009900")
    balance: int = Field(..., example=2500)
    customer_id: int = Field(..., example=1)

    @validator('balance')
    def balance_must_be_positive(cls, value):
        if value < 0:
            raise ValueError('Balance harus positif')
        return value

    class Config:
        orm_mode = True


class AccountInfoID(AccountInfo):
    id: int