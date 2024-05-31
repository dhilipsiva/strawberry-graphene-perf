import orjson

from graphene import Field, Int, String, Boolean, ObjectType, Schema, List, DateTime
from datetime import datetime
from pytz import timezone


DATA = []
TZ = timezone("UTC")
with open("data.json") as data:
    import json

    DATA = json.load(data)


def orjson_dumps(data):
    return orjson.dumps(data).decode()


def orjson_loads(data):
    return orjson.loads(data)


class ORJSONMiddleware:
    def resolve(self, next, root, info, **kwargs):
        result = next(root, info, **kwargs)
        if isinstance(result, dict):
            result = orjson_dumps(result)
        return result

    def process_response(self, request, response):
        if response["Content-Type"] == "application/json" and isinstance(reposese.content, dict):
            response.content = orjson_dumps(response.content)
        return response


class Datum(ObjectType):
    name = String()
    address = String()
    text = String()
    hex_color = String()
    random_int = Int()
    random_digit = Int()
    boolean = Boolean()
    items = List(String)


class Hello(ObjectType):
    data = List(Datum)
    datetime = DateTime()


class Query(ObjectType):
    hello = Field(Hello)

    def resolve_hello(*args, **kwargs):
        return dict(
            data=DATA,
            datetime=datetime.now(TZ),
        )


schema = Schema(query=Query)
