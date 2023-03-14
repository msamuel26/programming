from decorators.database import transactional
from models.account import AccountModel
from repositories.account import save, update, delete, get, get_all, get_for_update


@transactional
def create_account(account_number: str, balance: int, customer_id: int):
    account = AccountModel(account_number=account_number, balance=balance, customer_id=customer_id)
    print(account)
    account = save(account)
    return account


@transactional
def get_account(account_id: int):
    return get(account_id)


@transactional
def update_account(account_id: int, account_number: str, balance: int, customer_id: int):
    account = get_for_update(account_id)
    account.account_number = account_number
    account.balance = balance
    account.customer_id = customer_id
    result = update(account)
    return result


@transactional
def get_accounts(skip: int = 0, limit: int = 100):
    return get_all(skip, limit)


@transactional
def delete_account(account_id: int):
    account = get_for_update(account_id)
    delete(account)
