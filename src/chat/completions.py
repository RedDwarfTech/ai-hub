import json
import openai

def chat_stream(question: str, key: str):
    openai.api_key = key
    completion = openai.Completion.create(model="text-davinci-003",
                                          prompt=question,
                                          stream=True)
    for _ in completion:
        yield f"data:{json.dumps(_)}\n\n"