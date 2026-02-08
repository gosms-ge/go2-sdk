"""Go2 gRPC API Client."""

from typing import List, Optional, Any
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


class Go2Client:
    """
    Go2 gRPC API Client.

    Example:
        with Go2Client(api_key="go2_xxx") as client:
            integrations = client.integrations.list()

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

        integrations_stub = integrations_pb2_grpc.IntegrationServiceStub(
            self._channel
        )
        self.integrations = IntegrationsService(integrations_stub)

    def close(self) -> None:
        """Close the client connection."""
        self._channel.close()

    def __enter__(self) -> "Go2Client":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
