from decorators.database import transactional
from models.shipping import ShippingModel
from repositories.shipping import save, update, delete, get, get_all, get_for_update


@transactional
def create_shipping(status: str, customer: int):
    shipping = ShippingModel(status=status, customer=customer)
    print(shipping)
    shipping = save(shipping)
    return shipping


@transactional
def get_shipping(shipping_id: int):
    return get(shipping_id)


@transactional
def update_shipping(shipping_id: int, status: str, customer: int):
    shipping = get_for_update(shipping_id)
    shipping.status = status
    shipping.customer = customer
    result = update(shipping)
    return result


@transactional
def get_shippings(skip: int = 0, limit: int = 100):
    return get_all(skip, limit)


@transactional
def delete_shipping(shipping_id: int):
    shipping = get_for_update(shipping_id)
    delete(shipping)
