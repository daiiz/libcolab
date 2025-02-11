import requests


def run_search(queries, origin="", app_name="", token=""):
    if not token:
        raise Exception("No token provided")
    search_type = "similar"
    if len(queries) == 0:
        search_type = "random"
    print("#### search_type: ", search_type)
    api_url = "{}/api/v2/{}/{}".format(origin, app_name, search_type)
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
                "annoId": int(anno_id),
                "queryIndex": idx,
                "text": metadata["text"],
            }
            phrase = {
                "type": "annotation",
                "imageId": image_id,
                "annoId": int(anno_id),
                "desc": metadata["desc"],
            }
            annotation_hints.append(annotation_hint)
            search_phrase.append(phrase)
        else:
            search_phrase.append(
                {
                    "type": "text",
                    "text": q.strip(),
                }
            )

    payload = {
        "searchPhrase": search_phrase,
        "annotationHints": annotation_hints,
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
