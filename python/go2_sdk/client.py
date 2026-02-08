"""Go2 gRPC API Client."""

from typing import List, Optional, Any, Dict
import grpc

from go2_sdk.errors import wrap_error

DEFAULT_ENDPOINT = "grpc.go2.ge:443"


class _AuthInterceptor(grpc.UnaryUnaryClientInterceptor):
    """Interceptor that adds API key to all requests."""

    def __init__(self, api_key: str):
        self._api_key = api_key

    def intercept_unary_unary(
        self,
        continuation: Any,
        client_call_details: grpc.ClientCallDetails,
        request: Any,
    ) -> Any:
        metadata = list(client_call_details.metadata or [])
        metadata.append(("x-api-key", self._api_key))

        new_details = grpc.ClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            metadata=metadata,
            credentials=client_call_details.credentials,
            wait_for_ready=client_call_details.wait_for_ready,
            compression=client_call_details.compression,
        )

        return continuation(new_details, request)


class IntegrationsService:
    """Service for managing integrations."""

    def __init__(self, stub: Any):
        self._stub = stub

    def list(self) -> List[Any]:
        """List all integrations."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        try:
            response = self._stub.ListIntegrations(
                integrations_pb2.ListIntegrationsRequest()
            )
            return list(response.integrations)
        except grpc.RpcError as e:
            raise wrap_error(e)

    def create(
        self,
        type: Any,
        name: str,
        config: Any,
        events: List[str],
    ) -> Any:
        """Create a new integration."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        try:
            return self._stub.CreateIntegration(
                integrations_pb2.CreateIntegrationRequest(
                    type=type,
                    name=name,
                    config=config,
                    events=events,
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get(self, id: str) -> Any:
        """Get an integration by ID."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        try:
            return self._stub.GetIntegration(
                integrations_pb2.GetIntegrationRequest(id=id)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def update(
        self,
        id: str,
        name: Optional[str] = None,
        config: Optional[Any] = None,
        events: Optional[List[str]] = None,
        is_active: Optional[bool] = None,
    ) -> Any:
        """Update an integration."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        request = integrations_pb2.UpdateIntegrationRequest(id=id)
        if name is not None:
            request.name = name
        if config is not None:
            request.config.CopyFrom(config)
        if events is not None:
            request.events.extend(events)
        if is_active is not None:
            request.is_active = is_active

        try:
            return self._stub.UpdateIntegration(request)
        except grpc.RpcError as e:
            raise wrap_error(e)

    def delete(self, id: str) -> bool:
        """Delete an integration."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        try:
            response = self._stub.DeleteIntegration(
                integrations_pb2.DeleteIntegrationRequest(id=id)
            )
            return response.success
        except grpc.RpcError as e:
            raise wrap_error(e)

    def test(self, id: str) -> Any:
        """Test an integration by sending a test notification."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        try:
            return self._stub.TestIntegration(
                integrations_pb2.TestIntegrationRequest(id=id)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get_types(self) -> Any:
        """Get available integration types and events."""
        from go2_sdk.gen.integrations.v1 import integrations_pb2

        try:
            return self._stub.GetIntegrationTypes(
                integrations_pb2.GetIntegrationTypesRequest()
            )
        except grpc.RpcError as e:
            raise wrap_error(e)


class LinksService:
    """Service for managing smart links."""

    def __init__(self, stub: Any):
        self._stub = stub

    def list(self, page: int = 1, per_page: int = 20) -> Any:
        """List all links."""
        from go2_sdk.gen.links.v1 import links_pb2

        try:
            return self._stub.ListLinks(
                links_pb2.ListLinksRequest(page=page, per_page=per_page)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def create(
        self,
        slug: str,
        title: Optional[str] = None,
        ios_url: Optional[str] = None,
        android_url: Optional[str] = None,
        web_url: Optional[str] = None,
        fallback_url: Optional[str] = None,
    ) -> Any:
        """Create a new smart link."""
        from go2_sdk.gen.links.v1 import links_pb2

        try:
            return self._stub.CreateLink(
                links_pb2.CreateLinkRequest(
                    slug=slug,
                    title=title or "",
                    ios_url=ios_url or "",
                    android_url=android_url or "",
                    web_url=web_url or "",
                    fallback_url=fallback_url or "",
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get(self, id: str) -> Any:
        """Get a link by ID."""
        from go2_sdk.gen.links.v1 import links_pb2

        try:
            return self._stub.GetLink(links_pb2.GetLinkRequest(id=id))
        except grpc.RpcError as e:
            raise wrap_error(e)

    def update(
        self,
        id: str,
        title: Optional[str] = None,
        ios_url: Optional[str] = None,
        android_url: Optional[str] = None,
        web_url: Optional[str] = None,
        fallback_url: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> Any:
        """Update a link."""
        from go2_sdk.gen.links.v1 import links_pb2

        request = links_pb2.UpdateLinkRequest(id=id)
        if title is not None:
            request.title = title
        if ios_url is not None:
            request.ios_url = ios_url
        if android_url is not None:
            request.android_url = android_url
        if web_url is not None:
            request.web_url = web_url
        if fallback_url is not None:
            request.fallback_url = fallback_url
        if is_active is not None:
            request.is_active = is_active

        try:
            return self._stub.UpdateLink(request)
        except grpc.RpcError as e:
            raise wrap_error(e)

    def delete(self, id: str) -> bool:
        """Delete a link."""
        from go2_sdk.gen.links.v1 import links_pb2

        try:
            response = self._stub.DeleteLink(links_pb2.DeleteLinkRequest(id=id))
            return response.success
        except grpc.RpcError as e:
            raise wrap_error(e)


class AnalyticsService:
    """Service for link analytics."""

    def __init__(self, stub: Any):
        self._stub = stub

    def get_stats(self, link_id: str, period: str = "30d") -> Any:
        """Get stats for a link."""
        from go2_sdk.gen.analytics.v1 import analytics_pb2

        try:
            return self._stub.GetStats(
                analytics_pb2.GetStatsRequest(link_id=link_id, period=period)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get_timeseries(self, link_id: str, period: str = "30d") -> Any:
        """Get timeseries data for a link."""
        from go2_sdk.gen.analytics.v1 import analytics_pb2

        try:
            return self._stub.GetTimeseries(
                analytics_pb2.GetTimeseriesRequest(link_id=link_id, period=period)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get_platforms(self, link_id: str, period: str = "30d") -> Any:
        """Get platform breakdown for a link."""
        from go2_sdk.gen.analytics.v1 import analytics_pb2

        try:
            return self._stub.GetPlatforms(
                analytics_pb2.GetPlatformsRequest(link_id=link_id, period=period)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get_countries(self, link_id: str, period: str = "30d", limit: int = 10) -> Any:
        """Get country breakdown for a link."""
        from go2_sdk.gen.analytics.v1 import analytics_pb2

        try:
            return self._stub.GetCountries(
                analytics_pb2.GetCountriesRequest(
                    link_id=link_id, period=period, limit=limit
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get_referrers(self, link_id: str, period: str = "30d", limit: int = 10) -> Any:
        """Get referrer breakdown for a link."""
        from go2_sdk.gen.analytics.v1 import analytics_pb2

        try:
            return self._stub.GetReferrers(
                analytics_pb2.GetReferrersRequest(
                    link_id=link_id, period=period, limit=limit
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)


class DomainsService:
    """Service for managing custom domains."""

    def __init__(self, stub: Any):
        self._stub = stub

    def list(self) -> List[Any]:
        """List all custom domains."""
        from go2_sdk.gen.domains.v1 import domains_pb2

        try:
            response = self._stub.ListDomains(domains_pb2.ListDomainsRequest())
            return list(response.domains)
        except grpc.RpcError as e:
            raise wrap_error(e)

    def create(self, domain: str) -> Any:
        """Add a custom domain."""
        from go2_sdk.gen.domains.v1 import domains_pb2

        try:
            return self._stub.CreateDomain(
                domains_pb2.CreateDomainRequest(domain=domain)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get(self, id: str) -> Any:
        """Get a domain by ID."""
        from go2_sdk.gen.domains.v1 import domains_pb2

        try:
            return self._stub.GetDomain(domains_pb2.GetDomainRequest(id=id))
        except grpc.RpcError as e:
            raise wrap_error(e)

    def delete(self, id: str) -> bool:
        """Delete a custom domain."""
        from go2_sdk.gen.domains.v1 import domains_pb2

        try:
            response = self._stub.DeleteDomain(
                domains_pb2.DeleteDomainRequest(id=id)
            )
            return response.success
        except grpc.RpcError as e:
            raise wrap_error(e)

    def verify(self, id: str) -> Any:
        """Verify a custom domain."""
        from go2_sdk.gen.domains.v1 import domains_pb2

        try:
            return self._stub.VerifyDomain(domains_pb2.VerifyDomainRequest(id=id))
        except grpc.RpcError as e:
            raise wrap_error(e)


class QRService:
    """Service for QR code generation."""

    def __init__(self, stub: Any):
        self._stub = stub

    def generate(
        self,
        link_id: str,
        size: int = 256,
        format: str = "png",
        foreground_color: str = "#000000",
        background_color: str = "#FFFFFF",
    ) -> Any:
        """Generate a QR code for a link."""
        from go2_sdk.gen.qr.v1 import qr_pb2

        try:
            return self._stub.GenerateQR(
                qr_pb2.GenerateQRRequest(
                    link_id=link_id,
                    size=size,
                    format=format,
                    foreground_color=foreground_color,
                    background_color=background_color,
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)


class CampaignsService:
    """Service for managing marketing campaigns."""

    def __init__(self, stub: Any):
        self._stub = stub

    def list(self, page: int = 1, per_page: int = 20) -> Any:
        """List all campaigns."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            return self._stub.ListCampaigns(
                campaigns_pb2.ListCampaignsRequest(page=page, per_page=per_page)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def create(
        self,
        name: str,
        base_link_id: str,
        type: str = "sms",
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
    ) -> Any:
        """Create a new campaign."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            return self._stub.CreateCampaign(
                campaigns_pb2.CreateCampaignRequest(
                    name=name,
                    base_link_id=base_link_id,
                    type=type,
                    utm_source=utm_source or "",
                    utm_medium=utm_medium or "",
                    utm_campaign=utm_campaign or "",
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get(self, id: str) -> Any:
        """Get a campaign by ID."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            return self._stub.GetCampaign(campaigns_pb2.GetCampaignRequest(id=id))
        except grpc.RpcError as e:
            raise wrap_error(e)

    def update(
        self,
        id: str,
        name: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
    ) -> Any:
        """Update a campaign."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        request = campaigns_pb2.UpdateCampaignRequest(id=id)
        if name is not None:
            request.name = name
        if utm_source is not None:
            request.utm_source = utm_source
        if utm_medium is not None:
            request.utm_medium = utm_medium
        if utm_campaign is not None:
            request.utm_campaign = utm_campaign

        try:
            return self._stub.UpdateCampaign(request)
        except grpc.RpcError as e:
            raise wrap_error(e)

    def delete(self, id: str) -> bool:
        """Delete a campaign."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            response = self._stub.DeleteCampaign(
                campaigns_pb2.DeleteCampaignRequest(id=id)
            )
            return response.success
        except grpc.RpcError as e:
            raise wrap_error(e)

    def generate_links(self, id: str, recipients: List[Dict[str, str]]) -> Any:
        """Generate unique trackable links for recipients."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        recipient_msgs = [
            campaigns_pb2.Recipient(
                identifier=r.get("identifier", ""),
                metadata=r.get("metadata", {}),
            )
            for r in recipients
        ]

        try:
            return self._stub.GenerateLinks(
                campaigns_pb2.GenerateLinksRequest(
                    campaign_id=id, recipients=recipient_msgs
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def list_links(
        self, id: str, page: int = 1, per_page: int = 100
    ) -> Any:
        """List campaign links."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            return self._stub.ListCampaignLinks(
                campaigns_pb2.ListCampaignLinksRequest(
                    campaign_id=id, page=page, per_page=per_page
                )
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def get_stats(self, id: str) -> Any:
        """Get campaign statistics."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            return self._stub.GetCampaignStats(
                campaigns_pb2.GetCampaignStatsRequest(campaign_id=id)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)

    def export_links(self, id: str, format: str = "csv") -> Any:
        """Export campaign links."""
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2

        try:
            return self._stub.ExportLinks(
                campaigns_pb2.ExportLinksRequest(campaign_id=id, format=format)
            )
        except grpc.RpcError as e:
            raise wrap_error(e)


class Go2Client:
    """
    Go2 gRPC API Client.

    Example:
        with Go2Client(api_key="go2_xxx") as client:
            # Links
            links = client.links.list()
            link = client.links.create(slug="myapp", ios_url="...", android_url="...")

            # Analytics
            stats = client.analytics.get_stats(link_id="...")

            # Domains
            domains = client.domains.list()

            # QR Codes
            qr = client.qr.generate(link_id="...")

            # Integrations
            integrations = client.integrations.list()

            # Campaigns
            campaigns = client.campaigns.list()

    Args:
        api_key: Your Go2 API key (required)
        endpoint: gRPC endpoint (default: grpc.go2.ge:443)
        insecure: Use insecure connection for local development
    """

    def __init__(
        self,
        api_key: str,
        endpoint: str = DEFAULT_ENDPOINT,
        insecure: bool = False,
    ):
        if not api_key:
            raise ValueError("API key is required")

        # Create channel
        if insecure:
            channel = grpc.insecure_channel(endpoint)
        else:
            credentials = grpc.ssl_channel_credentials()
            channel = grpc.secure_channel(endpoint, credentials)

        # Add auth interceptor
        interceptor = _AuthInterceptor(api_key)
        self._channel = grpc.intercept_channel(channel, interceptor)

        # Import generated code and create service clients
        from go2_sdk.gen.integrations.v1 import integrations_pb2_grpc
        from go2_sdk.gen.links.v1 import links_pb2_grpc
        from go2_sdk.gen.analytics.v1 import analytics_pb2_grpc
        from go2_sdk.gen.domains.v1 import domains_pb2_grpc
        from go2_sdk.gen.qr.v1 import qr_pb2_grpc
        from go2_sdk.gen.campaigns.v1 import campaigns_pb2_grpc

        # Initialize all services
        self.integrations = IntegrationsService(
            integrations_pb2_grpc.IntegrationServiceStub(self._channel)
        )
        self.links = LinksService(
            links_pb2_grpc.LinkServiceStub(self._channel)
        )
        self.analytics = AnalyticsService(
            analytics_pb2_grpc.AnalyticsServiceStub(self._channel)
        )
        self.domains = DomainsService(
            domains_pb2_grpc.DomainServiceStub(self._channel)
        )
        self.qr = QRService(
            qr_pb2_grpc.QRServiceStub(self._channel)
        )
        self.campaigns = CampaignsService(
            campaigns_pb2_grpc.CampaignServiceStub(self._channel)
        )

    def close(self) -> None:
        """Close the client connection."""
        self._channel.close()

    def __enter__(self) -> "Go2Client":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
