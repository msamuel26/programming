from decorators.database import db
from schemas.order import OrderInfo, OrderInfoID
from models.order import OrderModel


@db
def save(order, db):
    db.add(order)
    db.flush()
    db.refresh(order)
    return OrderInfoID.from_orm(order)


@db
def update(order, db):
    db.add(order)
    db.flush()
    return order


@db
def delete(order, db):
    db.delete(order)
    db.flush()
    return


@db
def get(order_id: int, db):
    return OrderInfoID.from_orm(
        db.query(OrderModel).filter(OrderModel.id == order_id).first()
    )


@db
def get_for_update(order_id: int, db):
    return db.query(OrderModel).filter(OrderModel.id == order_id).first()


@db
def get_all(skip: int, limit: int, db):
    result = []
    datas = db.query(OrderModel).offset(skip).limit(limit).all()
    for data in datas:
        result.append(OrderInfoID.from_orm(data))
    return result
