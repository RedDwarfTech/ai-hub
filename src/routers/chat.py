from config.openai.openai_config import set_openai_endpoint
from fastapi import APIRouter, Header, Request
import asyncio
import json
import openai

from fastapi.responses import StreamingResponse
from src.chat.chatgpt import chat_server

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/chat")
def req_chat(q: str, authorization: str = Header(None)):
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    answer = chat_server(q, auth_token)
    return answer

@router.get("/v1/test")
def stream_chat_test():
    resp_headers = {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    return StreamingResponse(content=event_generator(), media_type="text/event-stream", headers=resp_headers)


async def event_generator():
    while True:
        yield f"data: ddd\n"
        await asyncio.sleep(1)


@router.get("/v1/completions")
def stream_chat(q: str, authorization: str = Header(None)):
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    openai.api_key = auth_token
    async def event_generator():
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=q,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
            stream=True
        )
        for _ in completions:
            yield f"data:{json.dumps(_)}\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@router.get("/v1/chat/stream/completions")
def chat_completions(q: str, authorization: str = Header(None), request: Request = None):
    client_host = request.client.host
    print("real ip:" + client_host)
    auth_mode, auth_token = authorization.split(' ')
    if auth_token is None:
        return "Authorization token is missing"
    set_openai_endpoint(auth_token)
    async def gpt_event_generator():
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": q,}],
                                            stream=True)
        for _ in completion:
            yield f"data:{json.dumps(_)}\n\n"
    return StreamingResponse(gpt_event_generator(), media_type="text/event-stream")
