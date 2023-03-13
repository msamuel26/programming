import uvicorn
from fastapi import FastAPI

from api.customer import customer_router
from api.order import order_router
from extensions.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {'message': 'Moses Transactional <3'}


app.include_router(customer_router)
app.include_router(order_router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
