from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session
from database import Base
from pydantic import BaseModel, Field

# Create a Pydantic model for the Customer
class CustomerCreate(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    age: int = Field(..., example=23)
    country: str = Field(..., example='USA')

# Create a SQLAlchemy model for the Customer
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    country = Column(String)

def create_customer(db: Session, first_name: str, last_name: str, age: int, country: str):
    customer = Customer(first_name=first_name, last_name=last_name, age=age, country=country)
    print(customer)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def update_customer(db: Session, customer_id: int, first: str, last: str, age: int, country: str):
    customer = get_customer(db, customer_id)
    customer.first_name = first
    customer.last_name = last
    customer.age = age
    customer.country = country
    db.commit()
    db.refresh(customer)
    return customer


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    db.delete(customer)
    db.commit()