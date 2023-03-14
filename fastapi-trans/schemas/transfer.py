from pydantic import BaseModel


# Create a Pydantic model for the Order
class TransferInfo(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: int

    # @validator('amount')
    # def amount_must_be_positive(cls, value):
    #     if value < 0:
    #         raise ValueError('Nilai harus positif')
    #     return value
