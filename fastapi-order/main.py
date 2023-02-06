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
from models import create_order
from models import delete_order
from models import get_order
from models import get_orders
from models import update_order
from fastapi.responses import JSONResponse
from models import OrderCreate, Order

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/orders/", response_class=JSONResponse)
def home(request: Request, db: Session = Depends(get_db)):
    print("ini eksekusi app get/", request)
    orders = get_orders(db)
    return JSONResponse(content= [{"id": order.id, "item": order.item, "amount": order.amount, "customer_id": order.customer_id} for order in orders])

# Define a route to create a new order in the database
@app.post("/orders/")
async def post_add_order(request: Request, order: OrderCreate, db: Session = Depends(get_db)):
    print(order)
    new_order = create_order(db, **order.dict())
    return {"message": "Order created successfully"}

@app.get("/order/edit/{order_id}", response_class=JSONResponse)
def get_edit(request: Request, order_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    order = get_order(db, order_id)
    return JSONResponse(content = {"id": order.id, "item": order.item, "amount": order.amount, "customer_id": order.customer_id})

@app.put("/order/edit/{order_id}", response_class=JSONResponse)
def put_edit(request: Request, order_id: int, item: str, amount: int, customer_id: int, db: Session = Depends(get_db)):
    print("ini put edit")
    update_order(db, order_id=order_id, item=item, amount=amount, customer_id=customer_id)
    return {"message": "Order created successfully"}


@app.delete("/delete/{order_id}", response_class=JSONResponse)
def delete(order_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_order(db, order_id)
    return {"message": "Order deleted successfully"}
