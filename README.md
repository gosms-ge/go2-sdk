# Go2 SDK

[![Go Reference](https://pkg.go.dev/badge/github.com/gosms-ge/go2-sdk/go.svg)](https://pkg.go.dev/github.com/gosms-ge/go2-sdk/go)
[![PyPI version](https://badge.fury.io/py/go2-sdk.svg)](https://pypi.org/project/go2-sdk/)
[![npm version](https://badge.fury.io/js/@go2ge%2Fsdk.svg)](https://www.npmjs.com/package/@go2ge/sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official SDKs for the [Go2](https://go2.ge) gRPC API - Smart App Links Platform.

## Available SDKs

| Language | Package | Installation |
|----------|---------|--------------|
| **Go** | [pkg.go.dev](https://pkg.go.dev/github.com/gosms-ge/go2-sdk/go) | `go get github.com/gosms-ge/go2-sdk/go` |
| **Python** | [PyPI](https://pypi.org/project/go2-sdk/) | `pip install go2-sdk` |
| **TypeScript** | [npm](https://www.npmjs.com/package/@go2ge/sdk) | `npm install @go2ge/sdk` |

## Quick Start

### Go

```go
client, _ := go2.NewClient(go2.WithAPIKey("go2_xxx"))
defer client.Close()

// Create a smart link
link, _ := client.Links.Create(ctx, &linksv1.CreateLinkRequest{
    Slug:       "myapp",
    IosUrl:     "https://apps.apple.com/app/id123",
    AndroidUrl: "https://play.google.com/store/apps/details?id=com.myapp",
})

// Get analytics
stats, _ := client.Analytics.GetStats(ctx, link.Id, "7d")
```

### Python

```python
with Go2Client(api_key="go2_xxx") as client:
    # Create a smart link
    link = client.links.create(
        slug="myapp",
        ios_url="https://apps.apple.com/app/id123",
        android_url="https://play.google.com/store/apps/details?id=com.myapp",
    )

    # Get analytics
    stats = client.analytics.get_stats(link.id, period="7d")
```

### TypeScript

```typescript
const client = new Go2Client({ apiKey: 'go2_xxx' });

// Create a smart link
const link = await client.links.create({
    slug: 'myapp',
    iosUrl: 'https://apps.apple.com/app/id123',
    androidUrl: 'https://play.google.com/store/apps/details?id=com.myapp',
});

// Get analytics
const stats = await client.analytics.getStats(link.id, '7d');

client.close();
```

## Available Services

| Service | Description |
|---------|-------------|
| **Links** | Create and manage smart app links |
| **Analytics** | Click analytics, platforms, countries, referrers |
| **Domains** | Custom domain management |
| **QR** | Generate customizable QR codes |
| **Integrations** | Slack, Discord, Telegram, Zapier webhooks |
| **Campaigns** | SMS/Email marketing with bulk trackable links |

## gRPC Endpoint

```
grpc.go2.ge:443
```

## Proto Files

- [links.proto](proto/links/v1/links.proto)
- [analytics.proto](proto/analytics/v1/analytics.proto)
- [domains.proto](proto/domains/v1/domains.proto)
- [qr.proto](proto/qr/v1/qr.proto)
- [integrations.proto](proto/integrations/v1/integrations.proto)
- [campaigns.proto](proto/campaigns/v1/campaigns.proto)

## Documentation

Full API documentation: **https://app.go2.ge/docs**

## Development

### Prerequisites

- Go 1.21+
- Python 3.8+
- Node.js 18+
- protoc (Protocol Buffers compiler)

### Generating Proto Code

```bash
# Generate for all languages
./scripts/generate-all.sh

# Or individually
./scripts/generate-go.sh
./scripts/generate-python.sh
./scripts/generate-typescript.sh
```

## Support

- Documentation: https://app.go2.ge/docs
- Issues: https://github.com/gosms-ge/go2-sdk/issues

## License

MIT - see [LICENSE](LICENSE)
