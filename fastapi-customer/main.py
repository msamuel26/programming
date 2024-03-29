import random
import uuid
from datetime import timedelta

from fastapi import Depends
from fastapi import FastAPI, Form
from fastapi import Request, Response
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session

from database import Base
from database import SessionLocal
from database import engine
from models import create_customer
from models import delete_customer
from models import get_customer
from models import get_customers
from models import update_customer
from fastapi.responses import JSONResponse
from models import CustomerCreate, Customer

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/customers/", response_class=JSONResponse)
def home(request: Request, db: Session = Depends(get_db)):
    print("ini eksekusi app get/", request)
    customers = get_customers(db)
    return JSONResponse(content= [{"id": customer.id, "first_name": customer.first_name, "last_name": customer.last_name, "age": customer.age, "country": customer.country} for customer in customers])

# Define a route to create a new customer in the database
@app.post("/customers/") 
async def post_add_customer(request: Request, customer: CustomerCreate, db: Session = Depends(get_db)):
    print(customer)
    new_customer = create_customer(db, **customer.dict())
    return {"message": "Customer created successfully"}

@app.get("/customer/edit/{customer_id}", response_class=JSONResponse)
def get_edit(request: Request, customer_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    customer = get_customer(db, customer_id)
    return JSONResponse(content = {"id": customer.id, "first_name": customer.first_name, "last_name": customer.last_name, "age": customer.age, "country": customer.country})

@app.put("/customer/edit/{customer_id}", response_class=JSONResponse)
def put_edit(request: Request, customer_id: int, first_name: str, last_name: str, age: int, country: str, db: Session = Depends(get_db)):
    print("ini put edit")
    update_customer(db, customer_id=customer_id, first=first_name, last=last_name, age=age, country=country)
    return {"message": "Customer created successfully"}


@app.delete("/customer/delete/{customer_id}", response_class=JSONResponse)
def delete(customer_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}
