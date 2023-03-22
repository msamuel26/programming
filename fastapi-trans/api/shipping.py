from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from services.shipping import create_shipping, get_shipping, update_shipping, delete_shipping, get_shippings
from schemas.shipping import ShippingInfo

shipping_router = APIRouter()


@shipping_router.get("/shippings/", response_class=JSONResponse)
async def home(request: Request, skip: int = 0, limit: int = 100):
    print("ini eksekusi app get/", request)
    shippings = get_shippings(skip, limit)
    return JSONResponse(content= [{"id": shipping.id, "status": shipping.status, "customer": shipping.customer} for shipping in shippings])


# Define a route to create a new shipping in the database
@shipping_router.post("/shippings/") 
async def post_add_shipping(request: Request, shipping: ShippingInfo):
    print(shipping)
    new_shipping = create_shipping(**shipping.dict())
    return JSONResponse(content={"id": new_shipping.id, "status": new_shipping.status,
                                 "customer": new_shipping.customer})


@shipping_router.get("/shipping/edit/{shipping_id}", response_class=JSONResponse)
async def get_edit(request: Request, shipping_id: int):
    print("ini get edit")
    shipping = get_shipping(shipping_id)
    return JSONResponse(content = {"id": shipping.id, "status": shipping.status, "customer": shipping.customer})


@shipping_router.put("/shipping/edit/{shipping_id}", response_class=JSONResponse)
async def put_edit(request: Request, shipping_id: int, status: str, customer: int):
    print("ini put edit")
    update_shipping(shipping_id=shipping_id, status=status, customer=customer)
    return {"message": "Shipping updated successfully"}


@shipping_router.delete("/shipping/delete/{shipping_id}", response_class=JSONResponse)
async def delete(shipping_id: int):
    print("ini untuk delete")
    delete_shipping(shipping_id)
    return {"message": "Shipping deleted successfully"}