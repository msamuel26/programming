from decorators.database import db
from schemas.shipping import ShippingInfo, ShippingInfoID
from models.shipping import ShippingModel


@db
def save(shipping, db):
    db.add(shipping)
    db.flush()
    db.refresh(shipping)
    return ShippingInfoID.from_orm(shipping)


@db
def update(shipping, db):
    db.add(shipping)
    db.flush()
    db.refresh(shipping)
    return shipping


@db
def delete(shipping, db):
    db.delete(shipping)
    db.flush()
    return


@db
def get(shipping_id: int, db):
    return ShippingInfoID.from_orm(
        db.query(ShippingModel).filter(ShippingModel.id == shipping_id).first()
    )


@db
def get_for_update(shipping_id: int, db):
    return db.query(ShippingModel).filter(ShippingModel.id == shipping_id).first()


@db
def get_all(skip: int, limit: int, db):
    result = []
    datas = db.query(ShippingModel).offset(skip).limit(limit).all()
    for data in datas:
        result.append(ShippingInfoID.from_orm(data))
    return result
