import json
from pytz import timezone


DATA = []
TZ = timezone("UTC")
with open("data.json") as data:
    DATA = json.load(data)
