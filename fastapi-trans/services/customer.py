from decorators.database import transactional, db
from extensions.database import SessionMaker
from models.customer import CustomerModel
from repositories.customer import save, delete

@transactional
def create_customer(first_name: str, last_name: str, age: int, country: str):
    customer = CustomerModel(first_name=first_name, last_name=last_name, age=age, country=country)
    print(customer)
    save(customer)
    return customer

@db
def get_customer(customer_id: int, db):
    return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

@transactional
def update_customer(customer_id: int, first: str, last: str, age: int, country: str):
    customer = get_customer(customer_id)
    customer.first_name = first
    customer.last_name = last
    customer.age = age
    customer.country = country
    save(customer)
    return customer

@db
def get_customers(skip: int = 0, limit: int = 100, db=SessionMaker):
    return db.query(CustomerModel).offset(skip).limit(limit).all()

@transactional
def delete_customer(customer_id: int):
    customer = get_customer(customer_id)
    delete(customer)