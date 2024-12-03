from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.get("/info", response_class=PlainTextResponse)
def get_info():
    return (
        "HI! This is Python Homework №4 Part 2\n"
        "Project Author name's Anastasiia\n"
        "/recent_cve Page will show all CVE's from up to 5 days ago\n"
        "/newest_cve Page will show 10 newest CVE's\n"
        "/known_cve  Page will show all 'Known' CVE's\n"
        "/get?query= Page will show all CVE's with a keyword"
    )
