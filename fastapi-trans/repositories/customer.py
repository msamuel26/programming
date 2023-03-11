from decorators.database import db
from schemas.customer import CustomerInfo, CustomerInfoID
from models.customer import CustomerModel


@db
def save(customer, db):
    db.add(customer)
    db.flush()
    return customer


@db
def update(customer, db):
    db.add(customer)
    db.flush()
    return customer


@db
def delete(customer, db):
    db.delete(customer)
    db.flush()
    return


@db
def get(customer_id: int, db):
    return CustomerInfoID.from_orm(
        db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    )


@db
def get_for_update(customer_id: int, db):
    return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()


@db
def get_all(skip: int, limit: int, db):
    result = []
    datas = db.query(CustomerModel).offset(skip).limit(limit).all()
    for data in datas:
        result.append(CustomerInfoID.from_orm(data))
    return result
