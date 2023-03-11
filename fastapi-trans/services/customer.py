from decorators.database import transactional
from models.customer import CustomerModel
from repositories.customer import save, update, delete, get, get_all, get_for_update


@transactional
def create_customer(first_name: str, last_name: str, age: int, country: str):
    customer = CustomerModel(first_name=first_name, last_name=last_name, age=age, country=country)
    print(customer)
    save(customer)
    return customer


@transactional
def get_customer(customer_id: int):
    return get(customer_id)


@transactional
def update_customer(customer_id: int, first: str, last: str, age: int, country: str):
    customer = get_for_update(customer_id)
    customer.first_name = first
    customer.last_name = last
    customer.age = age
    customer.country = country
    update(customer)
    return customer


@transactional
def get_customers(skip: int = 0, limit: int = 100):
    return get_all(skip, limit)


@transactional
def delete_customer(customer_id: int):
    customer = get_for_update(customer_id)
    delete(customer)
