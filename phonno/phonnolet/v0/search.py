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
    annotation_hints = []
    for [idx, q] in enumerate(queries):
        if isinstance(q, list):
            if len(q) != 3 or (not "text" in q[2]) or (not "desc" in q[2]):
                continue
            [image_id, anno_id, metadata] = q
            annotation_hint = {
                "imageId": image_id,
                "annoId": str(anno_id),
                "queryIndex": idx,
                "text": metadata["text"],
            }
            phrase = {
                "type": "annotation",
                "imageId": image_id,
                "annoId": str(anno_id),
                "desc": metadata["desc"],
            }
            print(idx, image_id, anno_id, "|", annotation_hint, phrase)
            continue
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
