"""
Go2 SDK - Official Python SDK for the Go2 gRPC API.

Example usage:
    from go2_sdk import Go2Client, IntegrationType, IntegrationConfig

    with Go2Client(api_key="go2_your_key") as client:
        integration = client.integrations.create(
            type=IntegrationType.INTEGRATION_TYPE_SLACK,
            name="My Slack Integration",
            config=IntegrationConfig(webhook_url="https://..."),
            events=["click_alert"],
        )
        print(f"Created: {integration.id}")
"""

from go2_sdk.client import Go2Client, IntegrationsService
from go2_sdk.errors import (
    Go2Error,
    AuthenticationError,
    NotFoundError,
    PermissionDeniedError,
    ValidationError,
    RateLimitError,
)

__version__ = "1.0.0"
__all__ = [
    "Go2Client",
    "IntegrationsService",
    "Go2Error",
    "AuthenticationError",
    "NotFoundError",
    "PermissionDeniedError",
    "ValidationError",
    "RateLimitError",
]

# Re-export generated types when available
try:
    from go2_sdk.gen.integrations.v1 import integrations_pb2

    IntegrationType = integrations_pb2.IntegrationType
    IntegrationConfig = integrations_pb2.IntegrationConfig
    Integration = integrations_pb2.Integration

    __all__.extend([
        "IntegrationType",
        "IntegrationConfig",
        "Integration",
    ])
except ImportError:
    pass  # Generated code not yet available
