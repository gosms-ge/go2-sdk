# Go2 SDK for Go

Official Go SDK for the Go2 gRPC API.

## Installation

```bash
go get github.com/gosms-ge/go2-sdk/go
```

## Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"

    go2 "github.com/gosms-ge/go2-sdk/go"
)

func main() {
    // Create client
    client, err := go2.NewClient(
        go2.WithAPIKey("go2_your_api_key"),
    )
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    ctx := context.Background()

    // List integrations
    integrations, err := client.Integrations.List(ctx)
    if err != nil {
        log.Fatal(err)
    }

    for _, integration := range integrations {
        fmt.Printf("Integration: %s (%s)\n", integration.Name, integration.Type)
    }
}
```

## Creating an Integration

```go
integration, err := client.Integrations.Create(ctx, &go2.CreateIntegrationInput{
    Type:   go2.IntegrationTypeSlack,
    Name:   "My Slack Alerts",
    Config: &go2.IntegrationConfig{
        WebhookURL: "https://hooks.slack.com/services/...",
    },
    Events: []string{"click_alert", "link_created"},
})
if err != nil {
    log.Fatal(err)
}

fmt.Printf("Created integration: %s\n", integration.ID)
```

## Updating an Integration

```go
updated, err := client.Integrations.Update(ctx, "integration-id", &go2.UpdateIntegrationInput{
    Name:     "Updated Name",
    IsActive: true,
})
```

## Testing an Integration

```go
result, err := client.Integrations.Test(ctx, "integration-id")
if err != nil {
    log.Fatal(err)
}

if result.Success {
    fmt.Println("Test notification sent successfully!")
} else {
    fmt.Printf("Test failed: %s\n", result.Message)
}
```

## Error Handling

```go
integration, err := client.Integrations.Get(ctx, "invalid-id")
if err != nil {
    switch e := err.(type) {
    case *go2.NotFoundError:
        fmt.Println("Integration not found")
    case *go2.AuthenticationError:
        fmt.Println("Invalid API key")
    case *go2.ValidationError:
        fmt.Printf("Validation error: %s\n", e.Message)
    default:
        fmt.Printf("Error: %v\n", err)
    }
}
```

## Configuration Options

```go
// Custom endpoint (for development)
client, _ := go2.NewClient(
    go2.WithAPIKey("go2_xxx"),
    go2.WithEndpoint("localhost:9090"),
    go2.WithInsecure(), // Disable TLS for local dev
)
```

## Available Integration Types

- `IntegrationTypeSlack` - Slack webhooks
- `IntegrationTypeDiscord` - Discord webhooks
- `IntegrationTypeTelegram` - Telegram bots
- `IntegrationTypeSegment` - Segment analytics
- `IntegrationTypeZapier` - Zapier webhooks

## License

MIT
