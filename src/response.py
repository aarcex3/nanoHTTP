import json
from http import HTTPStatus
from http.cookies import SimpleCookie
from typing import Annotated, Callable, Optional

from typing_extensions import Doc

from src.enums import MediaType
from src.nanohttp import MultiDict


class Response(Exception):
    """An HTTP Response. May be raised or returned at any time in middleware or route functions."""

    def __init__(
        self,
        status: Annotated[
            HTTPStatus,
            Doc(
                "The HTTP status code for the response. For example, `HTTPStatus.OK` for a 200 OK response."
            ),
        ] = HTTPStatus.OK,
        *,
        headers: Annotated[
            Optional[MultiDict],
            Doc(
                "HTTP headers to be included in the response. Defaults to None if not provided."
            ),
        ] = None,
        cookies: Annotated[
            Optional[SimpleCookie],
            Doc("Cookies to be set in the response. Defaults to None if not provided."),
        ] = None,
        body: Annotated[
            Optional[bytes],
            Doc("The body of the response. Defaults to an empty byte string."),
        ] = b"",
        dumps: Annotated[
            Callable,
            Doc(
                "Callable used to serialize data (e.g., `msgspec`, `orjson`, etc), defaults to `json.dumps`."
            ),
        ] = json.dumps,
    ) -> None:
        self.status: HTTPStatus = status
        try:
            self.description = HTTPStatus(status).phrase
        except ValueError:
            self.description = ""
        super().__init__(f"{self.status} {self.description}")
        self.headers = MultiDict(headers)
        self.headers.setdefault("content-type", f"{MediaType.HTML}; charset=utf-8")
        self.cookies = SimpleCookie(cookies)
        self.body = body
        self.dumps = dumps

    @classmethod
    def from_any(cls, any):
        if isinstance(any, int):
            return cls(status=any, body=HTTPStatus(any).phrase.encode())
        elif isinstance(any, str):
            return cls(status=HTTPStatus.OK, body=any.encode())
        elif isinstance(any, bytes):
            return cls(status=HTTPStatus.OK, body=any)
        elif isinstance(any, dict):
            return cls(
                status=HTTPStatus.OK,
                headers={"content-type": MediaType.JSON},
                body=cls().dumps(any).encode(),
            )
        elif isinstance(any, cls):
            return any
        elif any is None:
            return cls(status=HTTPStatus.NO_CONTENT)
        else:
            raise TypeError
