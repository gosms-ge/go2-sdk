# Go2 SDK for Go

[![Go Reference](https://pkg.go.dev/badge/github.com/gosms-ge/go2-sdk/go.svg)](https://pkg.go.dev/github.com/gosms-ge/go2-sdk/go)
[![Go 1.21+](https://img.shields.io/badge/go-1.21+-00ADD8.svg)](https://go.dev/)

Official Go SDK for the [Go2](https://go2.ge) gRPC API - Smart App Links Platform.

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
    linksv1 "github.com/gosms-ge/go2-sdk/go/gen/links/v1"
)

func main() {
    client, err := go2.NewClient(go2.WithAPIKey("go2_your_api_key"))
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    ctx := context.Background()

    // Create a smart link
    link, err := client.Links.Create(ctx, &linksv1.CreateLinkRequest{
        Slug:       "myapp",
        Title:      "My Awesome App",
        IosUrl:     "https://apps.apple.com/app/id123456",
        AndroidUrl: "https://play.google.com/store/apps/details?id=com.myapp",
        WebUrl:     "https://myapp.com",
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created: https://go2.ge/%s\n", link.Slug)

    // Get analytics
    stats, err := client.Analytics.GetStats(ctx, link.Id, "7d")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Total clicks: %d\n", stats.TotalClicks)
}
```

## Available Services

### Links

Create and manage smart links that redirect users to the right app store.

```go
// List all links
links, err := client.Links.List(ctx, 1, 20)

// Create a link
link, err := client.Links.Create(ctx, &linksv1.CreateLinkRequest{
    Slug:        "myapp",
    Title:       "My App",
    IosUrl:      "https://apps.apple.com/...",
    AndroidUrl:  "https://play.google.com/...",
    WebUrl:      "https://myapp.com",
    FallbackUrl: "https://myapp.com/download",
})

// Get a link
link, err := client.Links.Get(ctx, "link-id")

// Update a link
link, err := client.Links.Update(ctx, &linksv1.UpdateLinkRequest{
    Id:       "link-id",
    Title:    "New Title",
    IsActive: false,
})

// Delete a link
err := client.Links.Delete(ctx, "link-id")
```

### Analytics

Access detailed click analytics for your links.

```go
// Get overview stats
stats, err := client.Analytics.GetStats(ctx, "link-id", "30d")

// Get timeseries data
timeseries, err := client.Analytics.GetTimeseries(ctx, "link-id", "7d")

// Get platform breakdown
platforms, err := client.Analytics.GetPlatforms(ctx, "link-id", "30d")

// Get country breakdown
countries, err := client.Analytics.GetCountries(ctx, "link-id", "30d", 10)

// Get referrer breakdown
referrers, err := client.Analytics.GetReferrers(ctx, "link-id", "30d", 10)
```

### Domains

Add and manage custom domains.

```go
// List domains
domains, err := client.Domains.List(ctx)

// Add a domain
domain, err := client.Domains.Create(ctx, "links.myapp.com")

// Verify a domain
domain, err := client.Domains.Verify(ctx, "domain-id")

// Delete a domain
err := client.Domains.Delete(ctx, "domain-id")
```

### QR Codes

Generate customizable QR codes for your links.

```go
qr, err := client.QR.Generate(ctx, &qrv1.GenerateQRRequest{
    LinkId:          "link-id",
    Size:            512,
    Format:          "png",
    ForegroundColor: "#000000",
    BackgroundColor: "#FFFFFF",
})
fmt.Printf("QR Code URL: %s\n", qr.Url)
```

### Integrations

Connect with third-party services (Slack, Discord, Telegram, etc.).

```go
import integrationsv1 "github.com/gosms-ge/go2-sdk/go/gen/integrations/v1"

// List integrations
integrations, err := client.Integrations.List(ctx)

// Create an integration
integration, err := client.Integrations.Create(ctx, &integrationsv1.CreateIntegrationRequest{
    Type: integrationsv1.IntegrationType_INTEGRATION_TYPE_SLACK,
    Name: "Marketing Alerts",
    Config: &integrationsv1.IntegrationConfig{
        WebhookUrl: "https://hooks.slack.com/...",
    },
    Events: []string{"click_alert", "click_milestone"},
})

// Test an integration
result, err := client.Integrations.Test(ctx, "integration-id")

// Delete an integration
err := client.Integrations.Delete(ctx, "integration-id")
```

### Campaigns

Create SMS/Email marketing campaigns with bulk trackable links.

```go
import campaignsv1 "github.com/gosms-ge/go2-sdk/go/gen/campaigns/v1"

// Create a campaign
campaign, err := client.Campaigns.Create(ctx, &campaignsv1.CreateCampaignRequest{
    Name:        "Summer Sale 2024",
    BaseLinkId:  "link-id",
    Type:        "sms",
    UtmSource:   "sms",
    UtmCampaign: "summer_sale",
})

// Generate unique links for recipients
result, err := client.Campaigns.GenerateLinks(ctx, &campaignsv1.GenerateLinksRequest{
    CampaignId: campaign.Id,
    Recipients: []*campaignsv1.Recipient{
        {Identifier: "+1234567890", Metadata: map[string]string{"name": "John"}},
        {Identifier: "+0987654321", Metadata: map[string]string{"name": "Jane"}},
    },
})

// Get campaign stats
stats, err := client.Campaigns.GetStats(ctx, campaign.Id)
fmt.Printf("Click rate: %.2f%%\n", stats.ClickRate)

// Export links
export, err := client.Campaigns.ExportLinks(ctx, campaign.Id, "csv")
```

## Error Handling

```go
import "github.com/gosms-ge/go2-sdk/go/errors"

link, err := client.Links.Get(ctx, "invalid-id")
if err != nil {
    switch e := err.(type) {
    case *errors.NotFoundError:
        fmt.Println("Link not found")
    case *errors.AuthenticationError:
        fmt.Println("Invalid API key")
    case *errors.ValidationError:
        fmt.Printf("Validation error: %s\n", e.Message)
    case *errors.RateLimitError:
        fmt.Println("Rate limit exceeded, try again later")
    default:
        fmt.Printf("Error: %v\n", err)
    }
}
```

## Configuration

```go
// Production (default)
client, _ := go2.NewClient(go2.WithAPIKey("go2_xxx"))

// Custom endpoint (for development)
client, _ := go2.NewClient(
    go2.WithAPIKey("go2_xxx"),
    go2.WithEndpoint("localhost:9090"),
    go2.WithInsecure(), // Disable TLS for local dev
)
```

## Documentation

Full API documentation: **https://app.go2.ge/docs#sdks**

## Requirements

- Go 1.21+

## License

MIT
