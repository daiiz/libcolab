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

    # POST
    payload = {
        "searchPhrase": search_phrase,
        "annotationHints": [],
        "paginateSkip": 0,
    }
    print("run_search", payload, api_url)
