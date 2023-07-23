import requests


def run_search(queries, origin="", token=""):
    if len(queries) == 0:
        return []
    if not token:
        raise Exception("No token provided")
    api_url = "{}/api/similar".format(origin)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + token,
    }

    search_phrase = []
    for q in queries:
        if isinstance(q, list):
            continue
            # search_phrase.append({"imageId": q[0], "annoId": q[1]})
        else:
            search_phrase.append(
                {
                    "type": "text",
                    "text": q.strip(),
                }
            )

    payload = {
        "searchPhrase": search_phrase,
        "annotationHints": [],
        "paginateSkip": 0,
    }

    r = requests.post(api_url, json=payload, headers=headers)
    if r.status_code == 200:
        data = r.json()
        suggestions = []  # annotationsをクエリとして渡せる形式に変換したもの
        for anno in data["annotations"]:
            metadata = {
                "text": anno["text"],
                "desc": anno["desc"],
            }
            suggestions.append([anno["imageId"], int(anno["annoId"]), metadata])
        return suggestions, data["annotations"]
    else:
        raise Exception("Error: {}".format(r.status_code))
