# Go2 SDK for Python

Official Python SDK for the Go2 gRPC API.

## Installation

```bash
pip install go2-sdk
```

## Quick Start

```python
from go2_sdk import Go2Client, IntegrationType

# Using context manager (recommended)
with Go2Client(api_key="go2_your_api_key") as client:
    # List integrations
    integrations = client.integrations.list()

    for integration in integrations:
        print(f"Integration: {integration.name} ({integration.type})")
```

## Creating an Integration

```python
from go2_sdk import Go2Client, IntegrationType, IntegrationConfig

with Go2Client(api_key="go2_xxx") as client:
    integration = client.integrations.create(
        type=IntegrationType.SLACK,
        name="My Slack Alerts",
        config=IntegrationConfig(webhook_url="https://hooks.slack.com/..."),
        events=["click_alert", "link_created"],
    )

    print(f"Created integration: {integration.id}")
```

## Updating an Integration

```python
updated = client.integrations.update(
    "integration-id",
    name="Updated Name",
    is_active=True,
)
```

## Testing an Integration

```python
result = client.integrations.test("integration-id")

if result.success:
    print("Test notification sent successfully!")
else:
    print(f"Test failed: {result.message}")
```

## Error Handling

```python
from go2_sdk import (
    Go2Client,
    NotFoundError,
    AuthenticationError,
    ValidationError,
)

try:
    integration = client.integrations.get("invalid-id")
except NotFoundError:
    print("Integration not found")
except AuthenticationError:
    print("Invalid API key")
except ValidationError as e:
    print(f"Validation error: {e}")
```

## Configuration Options

```python
# Custom endpoint (for development)
client = Go2Client(
    api_key="go2_xxx",
    endpoint="localhost:9090",
    insecure=True,  # Disable TLS for local dev
)
```

## Async Support

```python
import asyncio
from go2_sdk import Go2Client

async def main():
    async with Go2Client(api_key="go2_xxx") as client:
        integrations = await client.integrations.list_async()
        print(integrations)

asyncio.run(main())
```

## Available Integration Types

- `IntegrationType.SLACK` - Slack webhooks
- `IntegrationType.DISCORD` - Discord webhooks
- `IntegrationType.TELEGRAM` - Telegram bots
- `IntegrationType.SEGMENT` - Segment analytics
- `IntegrationType.ZAPIER` - Zapier webhooks

## Requirements

- Python 3.8+
- grpcio
- protobuf

## License

MIT
