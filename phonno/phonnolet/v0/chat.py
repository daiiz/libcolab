import urllib, requests


def similar_with(queries, topk=5, origin="", token=""):
    if not token:
        raise Exception("No token provided")
    qs = []
    for q in queries:
        if isinstance(q, list):
            continue
        else:
            qs.append(q.strip())
    if len(qs) == 0:
        return []
    api_url = "{}/api/chat/similar?q={}&limit={}".format(
        origin,
        urllib.parse.quote(" ".join(qs)),
        topk,
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + token,
    }

    res = requests.get(api_url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        return data["activities"]
    else:
        raise Exception("Error: {}".format(r.status_code))
