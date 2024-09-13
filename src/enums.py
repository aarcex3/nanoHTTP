# Copied from Litestar. https://github.com/litestar-org/litestar/blob/main/litestar/enums.py
from enum import StrEnum


class MediaType(StrEnum):
    """An Enum for ``Content-Type`` header values."""

    JSON = "application/json"
    MESSAGEPACK = "application/x-msgpack"
    HTML = "text/html"
    TEXT = "text/plain"
    CSS = "text/css"
    XML = "application/xml"


class RequestEncodingType(StrEnum):
    """An Enum for request ``Content-Type`` header values designating encoding formats."""

    JSON = "application/json"
    MESSAGEPACK = "application/x-msgpack"
    MULTI_PART = "multipart/form-data"
    URL_ENCODED = "application/x-www-form-urlencoded"
