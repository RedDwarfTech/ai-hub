from fastapi import APIRouter

router = APIRouter()

@router.get("/url-list")
def get_all_urls():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list