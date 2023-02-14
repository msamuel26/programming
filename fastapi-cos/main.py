import random
import uuid
from datetime import timedelta

from fastapi import Depends
from fastapi import FastAPI, Form
from fastapi import Request, Response
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from database import Base
from database import SessionLocal
from database import engine
from model.customer import create_customer
from model.customer import delete_customer
from model.customer import get_customer
from model.customer import get_customers
from model.customer import update_customer
from model.customer import CustomerCreate, Customer

from model.order import create_order
from model.order import delete_order
from model.order import get_order
from model.order import get_orders
from model.order import update_order
from model.order import OrderCreate, Order

from model.shipping import create_shipping
from model.shipping import delete_shipping
from model.shipping import get_shipping
from model.shipping import get_shippings
from model.shipping import update_shipping
from model.shipping import ShippingCreate, Shipping

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Customer

@app.get("/customers/", response_class=JSONResponse)
async def home(request: Request, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    print("ini eksekusi app get/", request)
    customers = get_customers(db, skip, limit)
    return JSONResponse(content= [{"id": customer.id, "first_name": customer.first_name, "last_name": customer.last_name, "age": customer.age, "country": customer.country} for customer in customers])

# Define a route to create a new customer in the database
@app.post("/customers/") 
async def post_add_customer(request: Request, customer: CustomerCreate, db: Session = Depends(get_db)):
    print(customer)
    new_customer = create_customer(db, **customer.dict())
    return {"message": "Customer created successfully"}

@app.get("/customer/edit/{customer_id}", response_class=JSONResponse)
async def get_edit(request: Request, customer_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    customer = get_customer(db, customer_id)
    return JSONResponse(content = {"id": customer.id, "first_name": customer.first_name, "last_name": customer.last_name, "age": customer.age, "country": customer.country})

@app.put("/customer/edit/{customer_id}", response_class=JSONResponse)
async def put_edit(request: Request, customer_id: int, first_name: str, last_name: str, age: int, country: str, db: Session = Depends(get_db)):
    print("ini put edit")
    update_customer(db, customer_id=customer_id, first=first_name, last=last_name, age=age, country=country)
    return {"message": "Customer created successfully"}


@app.delete("/customer/delete/{customer_id}", response_class=JSONResponse)
async def delete(customer_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}

# Order

@app.get("/orders/", response_class=JSONResponse)
async def home(request: Request, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    print("ini eksekusi app get/", request)
    orders = get_orders(db, skip, limit)
    return JSONResponse(content= [{"id": order.id, "item": order.item, "amount": order.amount, "customer_id": order.customer_id} for order in orders])

# Define a route to create a new order in the database
@app.post("/orders/")
async def post_add_order(request: Request, order: OrderCreate, db: Session = Depends(get_db)):
    print(order)
    new_order = create_order(db, **order.dict())
    return {"message": "Order created successfully"}

@app.get("/order/edit/{order_id}", response_class=JSONResponse)
async def get_edit(request: Request, order_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    order = get_order(db, order_id)
    return JSONResponse(content = {"id": order.id, "item": order.item, "amount": order.amount, "customer_id": order.customer_id})

@app.put("/order/edit/{order_id}", response_class=JSONResponse)
async def put_edit(request: Request, order_id: int, item: str, amount: int, customer_id: int, db: Session = Depends(get_db)):
    print("ini put edit")
    update_order(db, order_id=order_id, item=item, amount=amount, customer_id=customer_id)
    return {"message": "Order created successfully"}


@app.delete("/order/delete/{order_id}", response_class=JSONResponse)
async def delete(order_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_order(db, order_id)
    return {"message": "Order deleted successfully"}

# Shipping

@app.get("/shippings/", response_class=JSONResponse)
async def home(request: Request, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    print("ini eksekusi app get/", request)
    shippings = get_shippings(db, skip, limit)
    return JSONResponse(content=[{"id": shipping.id, "status": shipping.status, "customer_id": shipping.customer_id} for shipping in shippings])

# Define a route to create a new shipping in the database
@app.post("/shippings/") 
async def post_add_shipping(request: Request, shipping: ShippingCreate, db: Session = Depends(get_db)):
    print(shipping)
    new_shipping = create_shipping(db, **shipping.dict())
    return {"message": "Shipping created successfully"}

@app.get("/shipping/edit/{shipping_id}", response_class=JSONResponse)
async def get_edit(request: Request, shipping_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    shipping = get_shipping(db, shipping_id)
    return JSONResponse(content = {"id": shipping.id, "status": shipping.status, "customer_id": shipping.customer_id})

@app.put("/shipping/edit/{shipping_id}", response_class=JSONResponse)
async def put_edit(request: Request, shipping_id: int, status: str, customer_id: int, db: Session = Depends(get_db)):
    print("ini put edit")
    update_shipping(db, shipping_id=shipping_id, status=status, customer_id=customer_id)
    return {"message": "Shipping created successfully"}


@app.delete("/shipping/delete/{shipping_id}", response_class=JSONResponse)
async def delete(shipping_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_shipping(db, shipping_id)
    return {"message": "Shipping deleted successfully"}
