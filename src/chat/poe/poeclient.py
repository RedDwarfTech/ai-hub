import poe

def poe_ask(token: str,prompt: str):
    poeclient = poe.Client(token)
    poe.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Te": "trailers",
        "Upgrade-Insecure-Requests": "1"
    }
    for chunk in poeclient.send_message("capybara", message = prompt):
        pass
    return chunk["text"]

def poe_ask_stream(token: str,prompt: str):
    print("hello")