from ctypes import Union
from fastapi import APIRouter, Header

from src.chat.chatgpt import chat_models

router = APIRouter()

@router.get("/models")
def req_models(authorization: str = Header(None)):
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    models = chat_models(auth_token)
    return models

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
