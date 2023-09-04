import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def _convertToMilliSeconds(date_str, zone="UTC"):
    # e.g. date_str: "2021-08-01"
    # Convert string to a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    # Set the timezone for the date
    tokyo_timezone = ZoneInfo(zone)
    date_obj_tz = date_obj.replace(tzinfo=tokyo_timezone)
    # Convert to a timestamp
    timestamp = date_obj_tz.timestamp()
    # Convert to milliseconds
    return int(timestamp * 1000)


# def get_photos_at()
