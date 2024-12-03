from elasticsearch import Elasticsearch
from fastapi import APIRouter

URL = "https://922c039b12124d658b96c3aab4e310dd.us-central1.gcp.cloud.es.io:443"
API_KEY = "czZPM2laTUJ1TzdCd1B5RU56YUI6Nng0VjdlMkhSYm1QUEp4VDFLOU1pdw=="
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