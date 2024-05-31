from graphene import Field, Int, String, Boolean, ObjectType, Schema, List, DateTime
from datetime import datetime
from pytz import timezone


DATA = []
TZ = timezone("UTC")
with open("data.json") as data:
    import json

    DATA = json.load(data)


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
