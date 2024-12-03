from fastapi import APIRouter
from elasticsearch import Elasticsearch
from migration.index import client

router = APIRouter()

@router.get("/known_cve")
def get_known_cve():
    return get_known_cve_list()

def get_known_cve_list():
    response = client.search(
        index="index_1",
        body={
            "query": {
                "match": {
                    "cve.knownRansomwareCampaignUse": "Known"
                }
            },
            "sort": [
                {"cve.dateAdded": {"order": "desc"}}
            ],
            "size": 10
        }
    )

    known_cve = []
    for hit in response['hits']['hits']:
        source = hit['_source']
        known_cve.append(source)

    client.index(index="index_2", document={"known_cve": known_cve})

    return {"known_cve": known_cve}
