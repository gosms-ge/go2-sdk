from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Campaign(_message.Message):
    __slots__ = ("id", "user_id", "name", "description", "destination_url", "pass_recipient_id", "recipient_param_name", "total_recipients", "total_clicks", "unique_clicks", "status", "created_at", "updated_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URL_FIELD_NUMBER: _ClassVar[int]
    PASS_RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CLICKS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    name: str
    description: str
    destination_url: str
    pass_recipient_id: bool
    recipient_param_name: str
    total_recipients: int
    total_clicks: int
    unique_clicks: int
    status: str
    created_at: str
    updated_at: str
    expires_at: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., destination_url: _Optional[str] = ..., pass_recipient_id: bool = ..., recipient_param_name: _Optional[str] = ..., total_recipients: _Optional[int] = ..., total_clicks: _Optional[int] = ..., unique_clicks: _Optional[int] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., expires_at: _Optional[str] = ...) -> None: ...

class CampaignLink(_message.Message):
    __slots__ = ("id", "campaign_id", "slug", "recipient_id", "recipient_name", "recipient_metadata", "clicked", "first_clicked_at", "last_clicked_at", "click_count", "first_click_platform", "first_click_country", "first_click_city", "created_at", "short_url")
    class RecipientMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    CLICKED_FIELD_NUMBER: _ClassVar[int]
    FIRST_CLICKED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_CLICKED_AT_FIELD_NUMBER: _ClassVar[int]
    CLICK_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_CLICK_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    FIRST_CLICK_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    FIRST_CLICK_CITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SHORT_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    campaign_id: str
    slug: str
    recipient_id: str
    recipient_name: str
    recipient_metadata: _containers.ScalarMap[str, str]
    clicked: bool
    first_clicked_at: str
    last_clicked_at: str
    click_count: int
    first_click_platform: str
    first_click_country: str
    first_click_city: str
    created_at: str
    short_url: str
    def __init__(self, id: _Optional[str] = ..., campaign_id: _Optional[str] = ..., slug: _Optional[str] = ..., recipient_id: _Optional[str] = ..., recipient_name: _Optional[str] = ..., recipient_metadata: _Optional[_Mapping[str, str]] = ..., clicked: bool = ..., first_clicked_at: _Optional[str] = ..., last_clicked_at: _Optional[str] = ..., click_count: _Optional[int] = ..., first_click_platform: _Optional[str] = ..., first_click_country: _Optional[str] = ..., first_click_city: _Optional[str] = ..., created_at: _Optional[str] = ..., short_url: _Optional[str] = ...) -> None: ...

class Recipient(_message.Message):
    __slots__ = ("id", "name", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListCampaignsRequest(_message.Message):
    __slots__ = ("limit", "offset", "status", "search")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    status: str
    search: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., status: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class ListCampaignsResponse(_message.Message):
    __slots__ = ("campaigns", "total")
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    campaigns: _containers.RepeatedCompositeFieldContainer[Campaign]
    total: int
    def __init__(self, campaigns: _Optional[_Iterable[_Union[Campaign, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class CreateCampaignRequest(_message.Message):
    __slots__ = ("name", "description", "destination_url", "pass_recipient_id", "recipient_param_name", "expires_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URL_FIELD_NUMBER: _ClassVar[int]
    PASS_RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    destination_url: str
    pass_recipient_id: bool
    recipient_param_name: str
    expires_at: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., destination_url: _Optional[str] = ..., pass_recipient_id: bool = ..., recipient_param_name: _Optional[str] = ..., expires_at: _Optional[str] = ...) -> None: ...

class GetCampaignRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class UpdateCampaignRequest(_message.Message):
    __slots__ = ("id", "name", "description", "destination_url", "pass_recipient_id", "recipient_param_name", "status", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URL_FIELD_NUMBER: _ClassVar[int]
    PASS_RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    destination_url: str
    pass_recipient_id: bool
    recipient_param_name: str
    status: str
    expires_at: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., destination_url: _Optional[str] = ..., pass_recipient_id: bool = ..., recipient_param_name: _Optional[str] = ..., status: _Optional[str] = ..., expires_at: _Optional[str] = ...) -> None: ...

class DeleteCampaignRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteCampaignResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GenerateLinksRequest(_message.Message):
    __slots__ = ("campaign_id", "recipients")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    recipients: _containers.RepeatedCompositeFieldContainer[Recipient]
    def __init__(self, campaign_id: _Optional[str] = ..., recipients: _Optional[_Iterable[_Union[Recipient, _Mapping]]] = ...) -> None: ...

class GenerateLinksResponse(_message.Message):
    __slots__ = ("campaign_id", "links_created", "sample_links")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_LINKS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    links_created: int
    sample_links: _containers.RepeatedCompositeFieldContainer[CampaignLink]
    def __init__(self, campaign_id: _Optional[str] = ..., links_created: _Optional[int] = ..., sample_links: _Optional[_Iterable[_Union[CampaignLink, _Mapping]]] = ...) -> None: ...

class ListCampaignLinksRequest(_message.Message):
    __slots__ = ("campaign_id", "limit", "offset", "clicked_only", "search")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CLICKED_ONLY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    limit: int
    offset: int
    clicked_only: bool
    search: str
    def __init__(self, campaign_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., clicked_only: bool = ..., search: _Optional[str] = ...) -> None: ...

class ListCampaignLinksResponse(_message.Message):
    __slots__ = ("links", "total")
    LINKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[CampaignLink]
    total: int
    def __init__(self, links: _Optional[_Iterable[_Union[CampaignLink, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class GetCampaignStatsRequest(_message.Message):
    __slots__ = ("campaign_id",)
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    def __init__(self, campaign_id: _Optional[str] = ...) -> None: ...

class CampaignStats(_message.Message):
    __slots__ = ("campaign_id", "total_recipients", "total_clicks", "unique_clicks", "click_rate", "clicks_by_platform", "clicks_by_country", "clicks_by_day")
    class ClicksByPlatformEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ClicksByCountryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ClicksByDayEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CLICKS_FIELD_NUMBER: _ClassVar[int]
    CLICK_RATE_FIELD_NUMBER: _ClassVar[int]
    CLICKS_BY_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLICKS_BY_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CLICKS_BY_DAY_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    total_recipients: int
    total_clicks: int
    unique_clicks: int
    click_rate: float
    clicks_by_platform: _containers.ScalarMap[str, int]
    clicks_by_country: _containers.ScalarMap[str, int]
    clicks_by_day: _containers.ScalarMap[str, int]
    def __init__(self, campaign_id: _Optional[str] = ..., total_recipients: _Optional[int] = ..., total_clicks: _Optional[int] = ..., unique_clicks: _Optional[int] = ..., click_rate: _Optional[float] = ..., clicks_by_platform: _Optional[_Mapping[str, int]] = ..., clicks_by_country: _Optional[_Mapping[str, int]] = ..., clicks_by_day: _Optional[_Mapping[str, int]] = ...) -> None: ...

class ExportLinksRequest(_message.Message):
    __slots__ = ("campaign_id", "format")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    format: str
    def __init__(self, campaign_id: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...

class ExportLinksResponse(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[CampaignLink]
    def __init__(self, links: _Optional[_Iterable[_Union[CampaignLink, _Mapping]]] = ...) -> None: ...
