from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStatsRequest(_message.Message):
    __slots__ = ("link_id", "period")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    period: str
    def __init__(self, link_id: _Optional[str] = ..., period: _Optional[str] = ...) -> None: ...

class GetStatsResponse(_message.Message):
    __slots__ = ("total_clicks", "unique_clicks", "ios_clicks", "android_clicks", "web_clicks", "other_clicks", "top_countries", "top_referrers")
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CLICKS_FIELD_NUMBER: _ClassVar[int]
    IOS_CLICKS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_CLICKS_FIELD_NUMBER: _ClassVar[int]
    WEB_CLICKS_FIELD_NUMBER: _ClassVar[int]
    OTHER_CLICKS_FIELD_NUMBER: _ClassVar[int]
    TOP_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    TOP_REFERRERS_FIELD_NUMBER: _ClassVar[int]
    total_clicks: int
    unique_clicks: int
    ios_clicks: int
    android_clicks: int
    web_clicks: int
    other_clicks: int
    top_countries: _containers.RepeatedCompositeFieldContainer[CountryStats]
    top_referrers: _containers.RepeatedCompositeFieldContainer[ReferrerStats]
    def __init__(self, total_clicks: _Optional[int] = ..., unique_clicks: _Optional[int] = ..., ios_clicks: _Optional[int] = ..., android_clicks: _Optional[int] = ..., web_clicks: _Optional[int] = ..., other_clicks: _Optional[int] = ..., top_countries: _Optional[_Iterable[_Union[CountryStats, _Mapping]]] = ..., top_referrers: _Optional[_Iterable[_Union[ReferrerStats, _Mapping]]] = ...) -> None: ...

class GetTimeseriesRequest(_message.Message):
    __slots__ = ("link_id", "period")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    period: str
    def __init__(self, link_id: _Optional[str] = ..., period: _Optional[str] = ...) -> None: ...

class GetTimeseriesResponse(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[TimeseriesPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[TimeseriesPoint, _Mapping]]] = ...) -> None: ...

class TimeseriesPoint(_message.Message):
    __slots__ = ("date", "clicks", "unique_clicks")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CLICKS_FIELD_NUMBER: _ClassVar[int]
    date: str
    clicks: int
    unique_clicks: int
    def __init__(self, date: _Optional[str] = ..., clicks: _Optional[int] = ..., unique_clicks: _Optional[int] = ...) -> None: ...

class GetPlatformsRequest(_message.Message):
    __slots__ = ("link_id", "period")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    period: str
    def __init__(self, link_id: _Optional[str] = ..., period: _Optional[str] = ...) -> None: ...

class GetPlatformsResponse(_message.Message):
    __slots__ = ("platforms",)
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    platforms: _containers.RepeatedCompositeFieldContainer[PlatformStats]
    def __init__(self, platforms: _Optional[_Iterable[_Union[PlatformStats, _Mapping]]] = ...) -> None: ...

class PlatformStats(_message.Message):
    __slots__ = ("platform", "clicks", "percentage")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    platform: str
    clicks: int
    percentage: float
    def __init__(self, platform: _Optional[str] = ..., clicks: _Optional[int] = ..., percentage: _Optional[float] = ...) -> None: ...

class GetCountriesRequest(_message.Message):
    __slots__ = ("link_id", "period", "limit")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    period: str
    limit: int
    def __init__(self, link_id: _Optional[str] = ..., period: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class GetCountriesResponse(_message.Message):
    __slots__ = ("countries",)
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    countries: _containers.RepeatedCompositeFieldContainer[CountryStats]
    def __init__(self, countries: _Optional[_Iterable[_Union[CountryStats, _Mapping]]] = ...) -> None: ...

class CountryStats(_message.Message):
    __slots__ = ("country_code", "country_name", "clicks", "percentage")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    country_name: str
    clicks: int
    percentage: float
    def __init__(self, country_code: _Optional[str] = ..., country_name: _Optional[str] = ..., clicks: _Optional[int] = ..., percentage: _Optional[float] = ...) -> None: ...

class GetReferrersRequest(_message.Message):
    __slots__ = ("link_id", "period", "limit")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    period: str
    limit: int
    def __init__(self, link_id: _Optional[str] = ..., period: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class GetReferrersResponse(_message.Message):
    __slots__ = ("referrers",)
    REFERRERS_FIELD_NUMBER: _ClassVar[int]
    referrers: _containers.RepeatedCompositeFieldContainer[ReferrerStats]
    def __init__(self, referrers: _Optional[_Iterable[_Union[ReferrerStats, _Mapping]]] = ...) -> None: ...

class ReferrerStats(_message.Message):
    __slots__ = ("referrer", "clicks", "percentage")
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    referrer: str
    clicks: int
    percentage: float
    def __init__(self, referrer: _Optional[str] = ..., clicks: _Optional[int] = ..., percentage: _Optional[float] = ...) -> None: ...
