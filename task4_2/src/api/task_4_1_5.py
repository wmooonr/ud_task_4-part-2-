from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch
from migration.index import client

router = APIRouter()

@router.get("/get")
def search_cve(query: str = Query(...)):
    return get_cve_by_query(query)

def get_cve_by_query(query: str):
    response = client.search(
        index="index_1",
        body={
            "query": {
                "match": {
                    "cve.shortDescription": query
                }
            },
            "sort": [
                {"cve.dateAdded": {"order": "desc"}}
            ],
        }
    )

    keyword_cve = []
    for hit in response['hits']['hits']:
        source = hit['_source']
        keyword_cve.append(source)

    client.index(index="index_2", document={"keyword_cve": keyword_cve})
    return {"cve_results": keyword_cve}
