import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Link(_message.Message):
    __slots__ = ("id", "user_id", "slug", "title", "ios_url", "android_url", "web_url", "fallback_url", "huawei_url", "amazon_url", "windows_url", "macos_url", "app_name", "app_icon_url", "description", "is_active", "total_clicks", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IOS_URL_FIELD_NUMBER: _ClassVar[int]
    ANDROID_URL_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    HUAWEI_URL_FIELD_NUMBER: _ClassVar[int]
    AMAZON_URL_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_URL_FIELD_NUMBER: _ClassVar[int]
    MACOS_URL_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ICON_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    slug: str
    title: str
    ios_url: str
    android_url: str
    web_url: str
    fallback_url: str
    huawei_url: str
    amazon_url: str
    windows_url: str
    macos_url: str
    app_name: str
    app_icon_url: str
    description: str
    is_active: bool
    total_clicks: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., slug: _Optional[str] = ..., title: _Optional[str] = ..., ios_url: _Optional[str] = ..., android_url: _Optional[str] = ..., web_url: _Optional[str] = ..., fallback_url: _Optional[str] = ..., huawei_url: _Optional[str] = ..., amazon_url: _Optional[str] = ..., windows_url: _Optional[str] = ..., macos_url: _Optional[str] = ..., app_name: _Optional[str] = ..., app_icon_url: _Optional[str] = ..., description: _Optional[str] = ..., is_active: bool = ..., total_clicks: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListLinksRequest(_message.Message):
    __slots__ = ("page", "per_page")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    page: int
    per_page: int
    def __init__(self, page: _Optional[int] = ..., per_page: _Optional[int] = ...) -> None: ...

class ListLinksResponse(_message.Message):
    __slots__ = ("links", "total", "page", "per_page")
    LINKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[Link]
    total: int
    page: int
    per_page: int
    def __init__(self, links: _Optional[_Iterable[_Union[Link, _Mapping]]] = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., per_page: _Optional[int] = ...) -> None: ...

class CreateLinkRequest(_message.Message):
    __slots__ = ("slug", "title", "ios_url", "android_url", "web_url", "fallback_url", "huawei_url", "amazon_url", "windows_url", "macos_url", "app_name", "app_icon_url", "description")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IOS_URL_FIELD_NUMBER: _ClassVar[int]
    ANDROID_URL_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    HUAWEI_URL_FIELD_NUMBER: _ClassVar[int]
    AMAZON_URL_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_URL_FIELD_NUMBER: _ClassVar[int]
    MACOS_URL_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ICON_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    slug: str
    title: str
    ios_url: str
    android_url: str
    web_url: str
    fallback_url: str
    huawei_url: str
    amazon_url: str
    windows_url: str
    macos_url: str
    app_name: str
    app_icon_url: str
    description: str
    def __init__(self, slug: _Optional[str] = ..., title: _Optional[str] = ..., ios_url: _Optional[str] = ..., android_url: _Optional[str] = ..., web_url: _Optional[str] = ..., fallback_url: _Optional[str] = ..., huawei_url: _Optional[str] = ..., amazon_url: _Optional[str] = ..., windows_url: _Optional[str] = ..., macos_url: _Optional[str] = ..., app_name: _Optional[str] = ..., app_icon_url: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GetLinkRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class UpdateLinkRequest(_message.Message):
    __slots__ = ("id", "slug", "title", "ios_url", "android_url", "web_url", "fallback_url", "is_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IOS_URL_FIELD_NUMBER: _ClassVar[int]
    ANDROID_URL_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    slug: str
    title: str
    ios_url: str
    android_url: str
    web_url: str
    fallback_url: str
    is_active: bool
    def __init__(self, id: _Optional[str] = ..., slug: _Optional[str] = ..., title: _Optional[str] = ..., ios_url: _Optional[str] = ..., android_url: _Optional[str] = ..., web_url: _Optional[str] = ..., fallback_url: _Optional[str] = ..., is_active: bool = ...) -> None: ...

class DeleteLinkRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteLinkResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class CheckSlugRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class CheckSlugResponse(_message.Message):
    __slots__ = ("available", "slug")
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    available: bool
    slug: str
    def __init__(self, available: bool = ..., slug: _Optional[str] = ...) -> None: ...
