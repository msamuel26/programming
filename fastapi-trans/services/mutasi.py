from decorators.database import transactional
from models.mutasi import Mutation
from repositories.mutasi import save, get, get_all, update, get_for_update, delete


@transactional
def create_mutation(account_id: int, amount_trans: int, balance: int):
    mutation = Mutation(account_id=account_id, amount_trans=amount_trans, balance=balance)
    print(mutation)
    mutation = save(mutation)
    return mutation


@transactional
def get_mutation(mutation_id: int):
    return get(mutation_id)


@transactional
def update_mutation(id: int, account_id: int, amount_trans: int, balance: int):
    mutation = get_for_update(id)
    mutation.account_id = account_id
    mutation.amount_trans = amount_trans
    mutation.balance = balance
    result = update(mutation)
    return result


@transactional
def get_customers(skip: int = 0, limit: int = 100):
    return get_all(skip, limit)


@transactional
def delete_customer(customer_id: int):
    customer = get_for_update(customer_id)
    delete(customer)
