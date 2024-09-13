from http import HTTPMethod
from http.cookies import SimpleCookie
from typing import Annotated, Dict, Optional

from typing_extensions import Doc

from src.nanohttp import MultiDict


class Request:
    """An HTTP request. Created every time the application is called on the HTTP protocol with a shallow copy of the state."""

    def __init__(
        self,
        method: Annotated[
            HTTPMethod,
            Doc(
                """Standard HTTP method.
                Read more [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)"""
            ),
        ],
        path: Annotated[
            str,
            Doc(
                "URL path. For example: https://www.example.com/products/12345/details"
            ),
        ],
        *,
        ip: Annotated[
            Optional[str],
            Doc(
                "The IP address of the request. Defaults to an empty string if not provided."
            ),
        ] = "",
        params: Annotated[
            Optional[MultiDict],
            Doc(
                "Query parameters passed with the request. Defaults to an empty dictionary if not provided."
            ),
        ] = None,
        args: Annotated[
            Optional[Dict],
            Doc(
                "Arguments passed with the request, typically in the form of key-value pairs. Defaults to an empty MultiDict if not provided."
            ),
        ] = None,
        headers: Annotated[
            Optional[MultiDict],
            Doc(
                "HTTP headers sent with the request. Defaults to an empty MultiDict if not provided."
            ),
        ] = None,
        cookies: Annotated[
            Optional[SimpleCookie],
            Doc(
                "Cookies sent with the request. Defaults to an empty SimpleCookie if not provided."
            ),
        ] = None,
        body: Annotated[
            Optional[bytes],
            Doc(
                "The body of the request, typically for POST or PUT requests. Defaults to an empty byte string."
            ),
        ] = b"",
        json: Annotated[
            Optional[Dict],
            Doc(
                "Parsed JSON data sent with the request. Defaults to None if not provided."
            ),
        ] = None,
        form: Annotated[
            MultiDict,
            Doc(
                "Form data sent with the request. Defaults to an empty MultiDict if not provided."
            ),
        ] = None,
        state: Annotated[
            Optional[Dict],
            Doc(
                "State associated with the request. Defaults to an empty dictionary if not provided."
            ),
        ] = None,
    ) -> None:
        self.method = method
        self.path = path
        self.ip = ip
        self.params = params or {}
        self.args = MultiDict(args)
        self.headers = MultiDict(headers)
        self.cookies = SimpleCookie(cookies)
        self.body = body
        self.json = json
        self.form = MultiDict(form)
        self.state = state or {}

    def __repr__(self):
        return f"{self.method} {self.path}"
