import requests


def similar_with(queries, topk=5, origin="", token=""):
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
        " ".join(qs),
        topk,
    )
    print(api_url)
