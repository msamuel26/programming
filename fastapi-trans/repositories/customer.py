from decorators.database import db
from schemas.customer import CustomerInfo

@db
def save(customer, db):
    db.add(customer)
    db.flush()
    return CustomerInfo.from_orm(customer)

@db
def delete(customer, db):
    db.delete(customer)
    db.flush()
    return CustomerInfo.from_orm(customer)