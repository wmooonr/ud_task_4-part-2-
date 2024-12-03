from fastapi import APIRouter
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
from migration.index import client
router = APIRouter()

@router.get("/recent_cve")
def get_info():
    return get_recent_cve()

def get_recent_cve():
    current_date = datetime.now()
    ten_days_ago = (current_date - timedelta(days=10)).strftime('%Y-%m-%d')
    # десять днів тому, що 5 це замало і нічого не покаже(( як і в першій частині дз

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
            "size": 40
        }
    )

    recent_cve = []
    for hit in response['hits']['hits']:
        source = hit['_source']
        recent_cve.append(source)

    client.index(index="index_2", document={"recent_cve": recent_cve})
    return {"recent_cve": recent_cve}
