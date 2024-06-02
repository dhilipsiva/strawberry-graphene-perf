import typing
import strawberry
import orjson

from datetime import datetime
from strawberry.http import GraphQLHTTPResponse
from strawberry.django.views import AsyncGraphQLView
from json_serde_exp.data import DATA, TZ
from strawberry_django.optimizer import DjangoOptimizerExtension


@strawberry.type
class Datum:
    name: str
    address: str
    text: str
    hex_color: str
    random_int: int
    random_digit: int
    boolean: bool
    items: typing.List[str]

DATA = [Datum(**datum) for datum in DATA]


@strawberry.type
class Hello:
    data: typing.List[Datum]
    datetime: datetime


def get_hello():
    return Hello(data=DATA, datetime=datetime.now(TZ))


@strawberry.type
class Query:
    hello: Hello = strawberry.field(resolver=get_hello)


class MyGraphQLView(AsyncGraphQLView):
    def encode_json(self, data: GraphQLHTTPResponse) -> str:
        return orjson.dumps(data).decode()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
