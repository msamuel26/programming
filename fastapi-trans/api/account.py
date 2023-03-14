from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from pydantic import ValidationError

from schemas.account import AccountInfo
from schemas.transfer import TransferInfo
from services.account import create_account, get_account, update_account, \
    delete_account, get_accounts, transfer_account

account_router = APIRouter()


@account_router.get("/accounts/", response_class=JSONResponse)
async def home(request: Request, skip: int = 0, limit: int = 100):
    accounts = get_accounts(skip, limit)
    return JSONResponse(content= [{"id": account.id, "account number": account.account_number, "balance": account.balance,
                                   "customer id": account.customer_id} for account in accounts])


# Define a route to create a new customer in the database
@account_router.post("/account/")
async def post_add_account(request: Request, account: AccountInfo):
    new_account = create_account(**account.dict())
    return JSONResponse(content={"id": new_account.id, "account number": new_account.account_number,
                                 "balance": new_account.balance,
                                 "customer id": new_account.customer_id})


@account_router.get("/account/edit/{account_id}", response_class=JSONResponse)
async def get_edit(request: Request, account_id: int):
    account = get_account(account_id)
    return JSONResponse(content={"id": account.id, "account_number": account.account_number,
                                 "balance": account.balance,
                                 "customer id": account.customer_id})


@account_router.put("/account/edit/{account_id}", response_class=JSONResponse)
async def put_edit(request: Request, account_id: int, account_number: str, balance: int, customer_id: int):
    update_account(account_id=account_id, account_number=account_number, balance=balance, customer_id=customer_id)
    return {"message": "Account updated successfully"}


@account_router.delete("/account/delete/{account_id}", response_class=JSONResponse)
async def delete(account_id: int):
    delete_account(account_id)
    return {"message": "Account deleted successfully"}


@account_router.post(f"/account/transfer/", response_class=JSONResponse)
async def perform_transfer(transfer: TransferInfo):
    try:
        transfer_account(transfer)
    except ValidationError as e:
        return e.errors()
    return {"message": "Amount transferred successfully"}
