import requests, json


def run_chat(messages, model="gpt-3.5-turbo", temperature=0.5, key=""):
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]

    if len(messages) == 0:
        return []

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + key,
    }
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": messages,
        "stream": True,
    }

    print(payload)
