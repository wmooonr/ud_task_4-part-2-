from fastapi import APIRouter
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
from migration.index import client

router = APIRouter()

@router.get("/newest_cve")
def get_new_cve():
    return get_new_cve_list()

def get_new_cve_list():
    current_date = datetime.now()
    ten_days_ago = (current_date - timedelta(days=10)).strftime('%Y-%m-%d') 

    response = client.search(
        index="index_1",
        body={
            "query": {
                "range": {
                    "cve.dateAdded": {
                        "gte": ten_days_ago,
                    }
                }
            },
            "sort": [
                {"cve.dateAdded": {"order": "desc"}}
            ],
            "size": 10
        }
    )

    newest_cve = []
    for hit in response['hits']['hits']:
        source = hit['_source']
        newest_cve.append(source)
    
    client.index(index="index_2", document={"newest_cve": newest_cve})
    return {"newest_cve": newest_cve}
