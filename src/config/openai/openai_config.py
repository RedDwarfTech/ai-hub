import os


def set_openai_endpoint(api_key: str):
    import openai
    openai.api_version = "2023-05-15"
    openai.api_type = "azure"
    openai.api_key = api_key
    openai.api_base = os.environ.get('OPENAI_API_BASE')