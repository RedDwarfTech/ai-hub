from fastapi import APIRouter, Header, Request
import asyncio
import json
import openai

from fastapi.responses import StreamingResponse
from src.chat.poe.poeclient import poe_ask

router = APIRouter()

async def event_generator():
    while True:
        yield f"data: ddd\n"
        await asyncio.sleep(1)


@router.get("/v1/poe/completions")
def poe_chat(q: str, authorization: str = Header(None)):
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    return poe_ask(auth_token,q)
   
@router.get("/v1/poe/chat/stream/completions")
def poe_chat_completions(q: str, authorization: str = Header(None), request: Request = None):
    client_host = request.client.host
    print("real ip:" + client_host)
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    openai.api_key = auth_token
    async def gpt_event_generator():
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": q,}],
                                            stream=True)
        for _ in completion:
            yield f"data:{json.dumps(_)}\n\n"
    return StreamingResponse(gpt_event_generator(), media_type="text/event-stream")
