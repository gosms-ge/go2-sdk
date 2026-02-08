# Go2 SDK

Official SDKs for the Go2 gRPC API.

## Available SDKs

| Language | Package | Installation |
|----------|---------|--------------|
| **Go** | `github.com/gosms-ge/go2-sdk/go` | `go get github.com/gosms-ge/go2-sdk/go` |
| **Python** | `go2-sdk` | `pip install go2-sdk` |
| **TypeScript/Node.js** | `@go2/sdk` | `npm install @go2/sdk` |

## Quick Examples

### Go

```go
client, _ := go2.NewClient(go2.WithAPIKey("go2_xxx"))
defer client.Close()

integrations, _ := client.Integrations.List(ctx)
```

### Python

```python
with Go2Client(api_key="go2_xxx") as client:
    integrations = client.integrations.list()
```

### TypeScript

```typescript
const client = new Go2Client({ apiKey: 'go2_xxx' });
const integrations = await client.integrations.list();
client.close();
```

## Features

- **Type-safe** - Full type support in all languages
- **gRPC** - High-performance binary protocol
- **Authentication** - Simple API key authentication
- **Error handling** - Structured error types

## API Reference

All SDKs provide the following methods:

### Integrations

| Method | Description |
|--------|-------------|
| `list()` | List all integrations |
| `create(params)` | Create a new integration |
| `get(id)` | Get integration by ID |
| `update(id, params)` | Update an integration |
| `delete(id)` | Delete an integration |
| `test(id)` | Send a test notification |
| `getTypes()` | Get available integration types |

### Integration Types

- **Slack** - Webhook notifications
- **Discord** - Webhook notifications
- **Telegram** - Bot messages
- **Segment** - Analytics events
- **Zapier** - Webhook triggers

## Development

### Prerequisites

- Go 1.21+
- Python 3.8+
- Node.js 16+
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

### Project Structure

```
go2-sdk/
├── proto/
│   └── integrations/v1/integrations.proto
├── scripts/
│   ├── generate-all.sh
│   ├── generate-go.sh
│   ├── generate-python.sh
│   └── generate-typescript.sh
├── go/
│   ├── client.go
│   ├── auth.go
│   ├── errors.go
│   └── gen/
├── python/
│   ├── go2_sdk/
│   │   ├── client.py
│   │   ├── errors.py
│   │   └── gen/
│   └── pyproject.toml
└── typescript/
    ├── src/
    │   ├── client.ts
    │   ├── errors.ts
    │   └── gen/
    └── package.json
```

## Support

- Documentation: https://docs.go2.ge
- Issues: https://github.com/gosms-ge/go2-sdk/issues

## License

MIT
