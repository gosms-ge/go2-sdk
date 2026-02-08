"""
Go2 SDK - Official Python SDK for the Go2 gRPC API.

Example usage:
    from go2_sdk import Go2Client

    with Go2Client(api_key="go2_your_key") as client:
        # Smart Links
        links = client.links.list()
        link = client.links.create(
            slug="myapp",
            ios_url="https://apps.apple.com/...",
            android_url="https://play.google.com/...",
        )

        # Analytics
        stats = client.analytics.get_stats(link_id=link.id)

        # Custom Domains
        domains = client.domains.list()

        # QR Codes
        qr = client.qr.generate(link_id=link.id)

        # Integrations
        integrations = client.integrations.list()

        # Campaigns
        campaigns = client.campaigns.list()
"""

from go2_sdk.client import (
    Go2Client,
    IntegrationsService,
    LinksService,
    AnalyticsService,
    DomainsService,
    QRService,
    CampaignsService,
)
from go2_sdk.errors import (
    Go2Error,
    AuthenticationError,
    NotFoundError,
    PermissionDeniedError,
    ValidationError,
    RateLimitError,
)

__version__ = "1.2.7"
__all__ = [
    "Go2Client",
    "IntegrationsService",
    "LinksService",
    "AnalyticsService",
    "DomainsService",
    "QRService",
    "CampaignsService",
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
    from go2_sdk.gen.links.v1 import links_pb2
    from go2_sdk.gen.campaigns.v1 import campaigns_pb2

    IntegrationType = integrations_pb2.IntegrationType
    IntegrationConfig = integrations_pb2.IntegrationConfig
    Integration = integrations_pb2.Integration
    Link = links_pb2.Link
    Campaign = campaigns_pb2.Campaign

    __all__.extend([
        "IntegrationType",
        "IntegrationConfig",
        "Integration",
        "Link",
        "Campaign",
    ])
except ImportError:
    pass  # Generated code not yet available
