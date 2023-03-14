from decorators.database import transactional
from models.order import OrderModel
from repositories.order import save, update, delete, get, get_all, get_for_update


@transactional
def create_order(item: str, amount: int, customer_id: int):
    order = OrderModel(item=item, amount=amount, customer_id=customer_id)
    print(order)
    order = save(order)
    return order


@transactional
def get_order(order_id: int):
    return get(order_id)


@transactional
def update_order(order_id: int, item: str, amount: int, customer_id: int):
    order = get_for_update(order_id)
    order.item = item
    order.amount = amount
    order.customer_id = customer_id
    result = update(order)
    return result


@transactional
def get_orders(skip: int = 0, limit: int = 100):
    return get_all(skip, limit)


@transactional
def delete_order(order_id: int):
    order = get_for_update(order_id)
    delete(order)
