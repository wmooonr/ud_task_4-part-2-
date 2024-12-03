from elasticsearch import Elasticsearch
from fastapi import APIRouter

URL = "your_url"
API_KEY = "your_api_key"
index = "index_1" # сюди завантажили дані з json-a і звідси виводимо
saved_index = "index_2" # сюди зберігаємо виведені дані

router = APIRouter()

@router.get("/create/index")
def get_info():
    return create_index()

client = Elasticsearch(
    URL,
    api_key=API_KEY
)

def create_index():
    response = client.indices.create(index=index)
    response_save = client.indices.create(index=saved_index)
    
    return "Success! Yipee!" if response.meta.status == 200 and response_save.meta.status == 200 else "Sorry. Creation Failed :("

if __name__ == "__main__":
    create_index()
