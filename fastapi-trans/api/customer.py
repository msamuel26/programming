from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.customer import create_customer, get_customer, update_customer, delete_customer, get_customers

customer_router = APIRouter()

@customer_router.get("/customers/", response_class=JSONResponse)
async def home(request: Request, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    print("ini eksekusi app get/", request)
    customers = get_customers(db, skip, limit)
    return JSONResponse(content= [{"id": customer.id, "first_name": customer.first_name, "last_name": customer.last_name, "age": customer.age, "country": customer.country} for customer in customers])

# Define a route to create a new customer in the database
@customer_router.post("/customers/") 
async def post_add_customer(request: Request, customer: CustomerCreate, db: Session = Depends(get_db)):
    print(customer)
    new_customer = create_customer(db, **customer.dict())
    return {"message": "Customer created successfully"}

@customer_router.get("/customer/edit/{customer_id}", response_class=JSONResponse)
async def get_edit(request: Request, customer_id: int, db: Session = Depends(get_db)):
    print("ini get edit")
    customer = get_customer(db, customer_id)
    return JSONResponse(content = {"id": customer.id, "first_name": customer.first_name, "last_name": customer.last_name, "age": customer.age, "country": customer.country})

@customer_router.put("/customer/edit/{customer_id}", response_class=JSONResponse)
async def put_edit(request: Request, customer_id: int, first_name: str, last_name: str, age: int, country: str, db: Session = Depends(get_db)):
    print("ini put edit")
    update_customer(db, customer_id=customer_id, first=first_name, last=last_name, age=age, country=country)
    return {"message": "Customer created successfully"}


@customer_router.delete("/customer/delete/{customer_id}", response_class=JSONResponse)
async def delete(customer_id: int, db: Session = Depends(get_db)):
    print("ini untuk delete")
    delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}