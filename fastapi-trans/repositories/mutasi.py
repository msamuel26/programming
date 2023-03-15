from decorators.database import db
from schemas.mutasi import MutationInfo, MutationInfoID
from models.mutasi import Mutation


@db
def save(mutation, db):
    db.add(mutation)
    db.flush()
    db.refresh(mutation)
    return MutationInfoID.from_orm(mutation)

@db
def update(mutation, db):
    db.add(mutation)
    db.flush()
    db.refresh(mutation)
    return mutation


@db
def delete(mutation, db):
    db.delete(mutation)
    db.flush()
    return

@db
def get(mutation_id: int, db):
    return MutationInfoID.from_orm(
        db.query(Mutation).filter(Mutation.id == mutation_id).first()
    )

@db
def get_for_update(mutation_id: int, db):
    return db.query(Mutation).filter(Mutation.id == mutation_id).first()

@db
def get_all(skip: int, limit: int, db):
    result = []
    datas = db.query(Mutation).offset(skip).limit(limit).all()
    for data in datas:
        result.append(MutationInfoID.from_orm(data))
    return result
