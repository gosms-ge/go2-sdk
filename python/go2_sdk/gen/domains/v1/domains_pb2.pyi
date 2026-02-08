import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOMAIN_STATUS_UNSPECIFIED: _ClassVar[DomainStatus]
    DOMAIN_STATUS_PENDING: _ClassVar[DomainStatus]
    DOMAIN_STATUS_VERIFYING: _ClassVar[DomainStatus]
    DOMAIN_STATUS_ACTIVE: _ClassVar[DomainStatus]
    DOMAIN_STATUS_FAILED: _ClassVar[DomainStatus]

class SSLStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SSL_STATUS_UNSPECIFIED: _ClassVar[SSLStatus]
    SSL_STATUS_PENDING: _ClassVar[SSLStatus]
    SSL_STATUS_PROVISIONING: _ClassVar[SSLStatus]
    SSL_STATUS_ACTIVE: _ClassVar[SSLStatus]
    SSL_STATUS_FAILED: _ClassVar[SSLStatus]
DOMAIN_STATUS_UNSPECIFIED: DomainStatus
DOMAIN_STATUS_PENDING: DomainStatus
DOMAIN_STATUS_VERIFYING: DomainStatus
DOMAIN_STATUS_ACTIVE: DomainStatus
DOMAIN_STATUS_FAILED: DomainStatus
SSL_STATUS_UNSPECIFIED: SSLStatus
SSL_STATUS_PENDING: SSLStatus
SSL_STATUS_PROVISIONING: SSLStatus
SSL_STATUS_ACTIVE: SSLStatus
SSL_STATUS_FAILED: SSLStatus

class Domain(_message.Message):
    __slots__ = ("id", "user_id", "domain", "status", "verification_token", "verified_at", "ssl_status", "cloudflare_hostname_id", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    SSL_STATUS_FIELD_NUMBER: _ClassVar[int]
    CLOUDFLARE_HOSTNAME_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    domain: str
    status: DomainStatus
    verification_token: str
    verified_at: _timestamp_pb2.Timestamp
    ssl_status: SSLStatus
    cloudflare_hostname_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., domain: _Optional[str] = ..., status: _Optional[_Union[DomainStatus, str]] = ..., verification_token: _Optional[str] = ..., verified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ssl_status: _Optional[_Union[SSLStatus, str]] = ..., cloudflare_hostname_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DNSRecord(_message.Message):
    __slots__ = ("type", "name", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    value: str
    def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ListDomainsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDomainsResponse(_message.Message):
    __slots__ = ("domains",)
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    domains: _containers.RepeatedCompositeFieldContainer[Domain]
    def __init__(self, domains: _Optional[_Iterable[_Union[Domain, _Mapping]]] = ...) -> None: ...

class CreateDomainRequest(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    def __init__(self, domain: _Optional[str] = ...) -> None: ...

class CreateDomainResponse(_message.Message):
    __slots__ = ("domain", "dns_records")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DNS_RECORDS_FIELD_NUMBER: _ClassVar[int]
    domain: Domain
    dns_records: _containers.RepeatedCompositeFieldContainer[DNSRecord]
    def __init__(self, domain: _Optional[_Union[Domain, _Mapping]] = ..., dns_records: _Optional[_Iterable[_Union[DNSRecord, _Mapping]]] = ...) -> None: ...

class GetDomainRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class VerifyDomainRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteDomainRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteDomainResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
