import requests, json, re


def run_chat(messages, model="gpt-3.5-turbo", temperature=0, key=""):
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

    completion = requests.post(api_url, headers=headers, json=payload, stream=True)
    res_lines = ""
    current_line = ""
    for chunk in completion:
        lines = chunk.decode("utf8").splitlines()
        for line in lines:
            if line.startswith("data: "):
                if current_line:
                    current_line = re.sub(r"^data:\s+", "", current_line)
                    data = json.loads(current_line)
                    # print("--", data) # for debug
                    try:
                        content = data["choices"][0]["delta"]["content"]
                        content = re.sub(r"\n+", "\n", content)
                        res_lines += content
                        print(content, end="")
                    except Exception as e:
                        print("Error:", e)
                        pass
                # 新たに記録を再開する
                current_line = line
            else:
                current_line += line

    # if current_line and current_line.strip() != "data: [DONE]":
    #     print("...", current_line)
    print("")
    return res_lines
