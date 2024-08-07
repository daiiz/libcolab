import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def _convertToMilliSeconds(date_str, zone="UTC"):
    # Convert string to a datetime object
    if "-" in date_str:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    elif "/" in date_str:
        date_obj = datetime.strptime(date_str, "%Y/%m/%d")
    # Set the timezone for the date
    tokyo_timezone = ZoneInfo(zone)
    date_obj_tz = date_obj.replace(tzinfo=tokyo_timezone)
    # Convert to a timestamp
    timestamp = date_obj_tz.timestamp()
    # Convert to milliseconds
    return int(timestamp * 1000)


def get_photos_at(date_str=None, location=None, origin="", token="", zone="UTC"):
    if not date_str and not location:
        raise Exception("No date or location provided")
    api_url = "{}/api/v1/memory/photos".format(origin)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + token,
    }
    payload = {}
    if date_str:
        payload["timestamp"] = _convertToMilliSeconds(date_str, zone)
    if location:
        payload["location"] = [location["lng"], location["lat"]]

    r = requests.post(api_url, json=payload, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data["images"]
    else:
        raise Exception("Error: {}".format(r.status_code))


def get_images_at(date_str, origin="", token="", zone="UTC"):
    if not date_str:
        raise Exception("No date provided")
    api_url = "{}/api/v1/memory/images".format(origin)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + token,
    }
    payload = {"timestamp": _convertToMilliSeconds(date_str, zone)}
    r = requests.post(api_url, json=payload, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data["images"]
    else:
        raise Exception("Error: {}".format(r.status_code))
