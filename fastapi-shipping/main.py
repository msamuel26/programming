# main.py berisi FastAPI mapping

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
from models import create_shipping
from models import delete_shipping
from models import get_shipping
from models import get_shippings
from models import update_shipping
from fastapi.responses import JSONResponse
from models import ShippingCreate, Shipping

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/shippings/", response_class=JSONResponse)
def home(request: Request, db: Session = Depends(get_db)):
    print("ini eksekusi app get/", request)
    shippings = get_shippings(db)
    return JSONResponse(content=[{"id": shipping.id, "status": shipping.status, "customer_id": shipping.customer_id} for shipping in shippings])

# Define a route to create a new shipping in the database
@app.post("/shippings/") 
async def post_add_shipping(request: Request, shipping: ShippingCreate, db: Session = Depends(get_db)):
    print(shipping)
    new_shipping = create_shipping(db, **shipping.dict())
    return {"message": "Shipping created successfully"}

@app.get("/shipping/edit/{shipping_id}", response_class=JSONResponse)
def get_edit(request: Request, shipping_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    shipping = get_shipping(db, shipping_id)
    return JSONResponse(content = {"id": shipping.id, "status": shipping.status, "customer_id": shipping.customer_id})

@app.put("/shipping/edit/{shipping_id}", response_class=JSONResponse)
def put_edit(request: Request, shipping_id: int, status: str, customer_id: int, db: Session = Depends(get_db)):
    print("ini put edit")
    update_shipping(db, shipping_id=shipping_id, status=status, customer_id=customer_id)
    return {"message": "Shipping created successfully"}


@app.delete("/shipping/delete/{shipping_id}", response_class=JSONResponse)
def delete(shipping_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_shipping(db, shipping_id)
    return {"message": "Shipping deleted successfully"}
