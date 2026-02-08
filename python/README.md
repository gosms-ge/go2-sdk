# Go2 SDK for Python

[![PyPI version](https://badge.fury.io/py/go2-sdk.svg)](https://pypi.org/project/go2-sdk/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Official Python SDK for the [Go2](https://go2.ge) gRPC API - Smart App Links Platform.

## Installation

```bash
pip install go2-sdk
```

## Quick Start

```python
from go2_sdk import Go2Client

with Go2Client(api_key="go2_your_api_key") as client:
    # Create a smart link
    link = client.links.create(
        slug="myapp",
        title="My Awesome App",
        ios_url="https://apps.apple.com/app/id123456",
        android_url="https://play.google.com/store/apps/details?id=com.myapp",
        web_url="https://myapp.com"
    )
    print(f"Created: https://go2.ge/{link.slug}")

    # Get analytics
    stats = client.analytics.get_stats(link.id, period="7d")
    print(f"Total clicks: {stats.total_clicks}")
```

## Available Services

### Links

Create and manage smart links that redirect users to the right app store.

```python
# List all links
links = client.links.list(page=1, per_page=20)

# Create a link
link = client.links.create(
    slug="myapp",
    title="My App",
    ios_url="https://apps.apple.com/...",
    android_url="https://play.google.com/...",
    web_url="https://myapp.com",
    fallback_url="https://myapp.com/download"
)

# Get a link
link = client.links.get("link-id")

# Update a link
link = client.links.update("link-id", title="New Title", is_active=False)

# Delete a link
client.links.delete("link-id")
```

### Analytics

Access detailed click analytics for your links.

```python
# Get overview stats
stats = client.analytics.get_stats(link_id="...", period="30d")

# Get timeseries data
timeseries = client.analytics.get_timeseries(link_id="...", period="7d")

# Get platform breakdown
platforms = client.analytics.get_platforms(link_id="...", period="30d")

# Get country breakdown
countries = client.analytics.get_countries(link_id="...", period="30d", limit=10)

# Get referrer breakdown
referrers = client.analytics.get_referrers(link_id="...", period="30d", limit=10)
```

### Domains

Add and manage custom domains.

```python
# List domains
domains = client.domains.list()

# Add a domain
domain = client.domains.create(domain="links.myapp.com")

# Verify a domain
domain = client.domains.verify("domain-id")

# Delete a domain
client.domains.delete("domain-id")
```

### QR Codes

Generate customizable QR codes for your links.

```python
qr = client.qr.generate(
    link_id="...",
    size=512,
    format="png",
    foreground_color="#000000",
    background_color="#FFFFFF"
)
print(f"QR Code URL: {qr.url}")
```

### Integrations

Connect with third-party services (Slack, Discord, Telegram, etc.).

```python
from go2_sdk import IntegrationType, IntegrationConfig

# List integrations
integrations = client.integrations.list()

# Create an integration
integration = client.integrations.create(
    type=IntegrationType.SLACK,
    name="Marketing Alerts",
    config=IntegrationConfig(webhook_url="https://hooks.slack.com/..."),
    events=["click_alert", "click_milestone"]
)

# Test an integration
result = client.integrations.test("integration-id")

# Delete an integration
client.integrations.delete("integration-id")
```

### Campaigns

Create SMS/Email marketing campaigns with bulk trackable links.

```python
# Create a campaign
campaign = client.campaigns.create(
    name="Summer Sale 2024",
    base_link_id="...",
    type="sms",
    utm_source="sms",
    utm_campaign="summer_sale"
)

# Generate unique links for recipients
result = client.campaigns.generate_links(
    id=campaign.id,
    recipients=[
        {"identifier": "+1234567890", "metadata": {"name": "John"}},
        {"identifier": "+0987654321", "metadata": {"name": "Jane"}},
    ]
)

# Get campaign stats
stats = client.campaigns.get_stats(campaign.id)
print(f"Click rate: {stats.click_rate}%")

# Export links
export = client.campaigns.export_links(campaign.id, format="csv")
```

## Error Handling

```python
from go2_sdk import (
    Go2Client,
    Go2Error,
    NotFoundError,
    AuthenticationError,
    ValidationError,
    RateLimitError,
)

try:
    link = client.links.get("invalid-id")
except NotFoundError:
    print("Link not found")
except AuthenticationError:
    print("Invalid API key")
except ValidationError as e:
    print(f"Validation error: {e}")
except RateLimitError:
    print("Rate limit exceeded, try again later")
except Go2Error as e:
    print(f"API error: {e}")
```

## Configuration

```python
# Production (default)
client = Go2Client(api_key="go2_xxx")

# Custom endpoint (for development)
client = Go2Client(
    api_key="go2_xxx",
    endpoint="localhost:9090",
    insecure=True  # Disable TLS for local dev
)
```

## Documentation

Full API documentation: **https://app.go2.ge/docs#sdks**

## Requirements

- Python 3.8+
- grpcio >= 1.59.0
- protobuf >= 4.25.0

## License

MIT
