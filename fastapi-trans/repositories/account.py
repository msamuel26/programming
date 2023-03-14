from decorators.database import db
from schemas.account import AccountInfoID
from models.account import AccountModel


@db
def save(account, db):
    db.add(account)
    db.flush()
    db.refresh(account)
    return AccountInfoID.from_orm(account)


@db
def update(account, db):
    db.add(account)
    db.flush()
    db.refresh(account)
    return account


@db
def delete(account, db):
    db.delete(account)
    db.flush()
    return


@db
def get(account_id: int, db):
    return AccountInfoID.from_orm(
        db.query(AccountModel).filter(AccountModel.id == account_id).first()
    )


@db
def get_for_update(account_id: int, db):
    return db.query(AccountModel).filter(AccountModel.id == account_id).first()


@db
def get_all(skip: int, limit: int, db):
    result = []
    datas = db.query(AccountModel).offset(skip).limit(limit).all()
    for data in datas:
        result.append(AccountInfoID.from_orm(data))
    return result
