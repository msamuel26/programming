from pydantic import BaseModel

class MutationInfo(BaseModel):
    account_id: int
    amount_trans: int
    balance: int

    class Config:
        orm_mode = True

class MutationInfoID(MutationInfo):
    id: int