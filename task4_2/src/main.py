from fastapi import FastAPI
from migration import index
from api import db
from api import task_4_1_1
from api import task_4_1_2
from api import task_4_1_3
from api import task_4_1_4
from api import task_4_1_5

api_object = FastAPI()
api_object.include_router(index.router)
api_object.include_router(db.router)
api_object.include_router(task_4_1_1.router)
api_object.include_router(task_4_1_2.router)
api_object.include_router(task_4_1_3.router)
api_object.include_router(task_4_1_4.router)
api_object.include_router(task_4_1_5.router)
