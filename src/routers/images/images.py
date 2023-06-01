from fastapi import APIRouter, Header
import openai

from fastapi.responses import JSONResponse
from src.models.images.ImageRequest import ImageRequest

router = APIRouter()

@router.post("/v1/images/generations")
def chat_completions(req: ImageRequest, authorization: str = Header(None)):
    auth_mode, auth_token = authorization.split(' ')
    openai.api_key = auth_token
    completion = openai.Image.create(prompt = req.prompt, n = 2, size = "1024x1024")
    return JSONResponse(completion)



