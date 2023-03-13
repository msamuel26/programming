from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from services.order import create_order, get_order, update_order, delete_order, get_orders
from schemas.order import OrderInfo

order_router = APIRouter()


@order_router.get("/orders/", response_class=JSONResponse)
async def home(request: Request, skip: int = 0, limit: int = 100):
    print("ini eksekusi app get/", request)
    orders = get_orders(skip, limit)
    return JSONResponse(content= [{"id": order.id, "item": order.item, "amount": order.amount, "customer_id": order.customer_id} for order in orders])


# Define a route to create a new order in the database
@order_router.post("/orders/") 
async def post_add_order(request: Request, order: OrderInfo):
    print(order)
    new_order = create_order(**order.dict())
    return JSONResponse(content={"id": new_order.id, "item": new_order.item,
                                 "amount": new_order.amount, "customer_id": new_order.customer_id})


@order_router.get("/order/edit/{order_id}", response_class=JSONResponse)
async def get_edit(request: Request, order_id: int):
    print("ini get edit")
    order = get_order(order_id)
    return JSONResponse(content = {"id": order.id, "item": order.item, "amount": order.amount, "customer_id": order.customer_id})


@order_router.put("/order/edit/{order_id}", response_class=JSONResponse)
async def put_edit(request: Request, order_id: int, item: str, amount: int, customer_id: int):
    print("ini put edit")
    update_order(order_id=order_id, item=item, amount=amount, customer_id=customer_id)
    return {"message": "Order updated successfully"}


@order_router.delete("/order/delete/{order_id}", response_class=JSONResponse)
async def delete(order_id: int):
    print("ini untuk delete")
    delete_order(order_id)
    return {"message": "Order deleted successfully"}