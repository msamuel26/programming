from decorators.database import transactional
from models.customer import CustomerModel
from repositories.customer import save, delete

from sqlalchemy.orm import Session

@transactional
def create_customer(db: Session, first_name: str, last_name: str, age: int, country: str):
    customer = CustomerModel(first_name=first_name, last_name=last_name, age=age, country=country)
    print(customer)
    save(customer)
    return customer

def get_customer(db: Session, customer_id: int):
    return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

@transactional
def update_customer(db: Session, customer_id: int, first: str, last: str, age: int, country: str):
    customer = get_customer(db, customer_id)
    customer.first_name = first
    customer.last_name = last
    customer.age = age
    customer.country = country
    save(customer)
    return customer

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CustomerModel).offset(skip).limit(limit).all()

@transactional
def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    delete(customer)