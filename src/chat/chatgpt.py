
import openai

def chat_server(question: str, key: str):
    openai.api_key = key
    # create a completion
    # completion = openai.Completion.create(model="gpt-3.5-turbo-0301", prompt="你好")

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": question}
                                        ])
    # print the completion
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def chat_models(key: str):
    openai.api_key = key
    # list models
    models = openai.Model.list()
    return models
