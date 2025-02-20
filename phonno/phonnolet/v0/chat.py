import urllib, requests


def similar_with(queries, topk=5, origin="", app_name="", token=""):
    if not token:
        raise Exception("No token provided")
    qs = []
    for q in queries:
        if isinstance(q, list):
            if len(q) != 3 or (not "text" in q[2]) or (not "desc" in q[2]):
                continue
            [_, _, metadata] = q
            q_str = metadata["desc"] if "desc" in metadata else metadata["text"]
            qs.append(q_str.strip())
        else:
            qs.append(q.strip())
    if len(qs) == 0:
        return [], []
    api_url = "{}/api/v2/app/{}/chat/similar?q={}&limit={}".format(
        origin,
        app_name,
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
        return data["activities"], qs
    else:
        raise Exception("Error: {}".format(r.status_code))
