from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateQRRequest(_message.Message):
    __slots__ = ("link_id", "size", "format", "foreground_color", "background_color", "logo_url")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FOREGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    size: int
    format: str
    foreground_color: str
    background_color: str
    logo_url: str
    def __init__(self, link_id: _Optional[str] = ..., size: _Optional[int] = ..., format: _Optional[str] = ..., foreground_color: _Optional[str] = ..., background_color: _Optional[str] = ..., logo_url: _Optional[str] = ...) -> None: ...

class GenerateQRResponse(_message.Message):
    __slots__ = ("url", "size", "format")
    URL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    url: str
    size: int
    format: str
    def __init__(self, url: _Optional[str] = ..., size: _Optional[int] = ..., format: _Optional[str] = ...) -> None: ...
