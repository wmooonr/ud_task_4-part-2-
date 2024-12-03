from fastapi import APIRouter
from uuid import uuid4
from migration.index import client, index
import json

router = APIRouter()

@router.get("/db")
def initialize_database():
    with open(r"C:\Users\Anastasiia\homework_python\task4\src\api\known_exploited_vulnerabilities.json") as file:
        data = json.load(file)
    documents = [{"cve": cve} for cve in data['vulnerabilities']]

    for doc in documents:
        client.create(index=index, id=str(uuid4()), body=doc)

    return {"message": "Initialization successful", "count": len(documents)}
