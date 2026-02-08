# Go2 SDK for Node.js/TypeScript

[![npm version](https://badge.fury.io/js/@go2ge%2Fsdk.svg)](https://www.npmjs.com/package/@go2ge/sdk)
[![Node.js 16+](https://img.shields.io/badge/node-16+-green.svg)](https://nodejs.org/)

Official TypeScript/Node.js SDK for the [Go2](https://go2.ge) gRPC API - Smart App Links Platform.

## Installation

```bash
npm install @go2ge/sdk
# or
yarn add @go2ge/sdk
# or
pnpm add @go2ge/sdk
```

## Quick Start

```typescript
import { Go2Client } from '@go2ge/sdk';

const client = new Go2Client({ apiKey: 'go2_your_api_key' });

try {
  // Create a smart link
  const link = await client.links.create({
    slug: 'myapp',
    title: 'My Awesome App',
    iosUrl: 'https://apps.apple.com/app/id123456',
    androidUrl: 'https://play.google.com/store/apps/details?id=com.myapp',
    webUrl: 'https://myapp.com',
  });
  console.log(`Created: https://go2.ge/${link.slug}`);

  // Get analytics
  const stats = await client.analytics.getStats(link.id, '7d');
  console.log(`Total clicks: ${stats.totalClicks}`);
} finally {
  client.close();
}
```

## Available Services

### Links

Create and manage smart links that redirect users to the right app store.

```typescript
// List all links
const { links, total } = await client.links.list({ page: 1, perPage: 20 });

// Create a link
const link = await client.links.create({
  slug: 'myapp',
  title: 'My App',
  iosUrl: 'https://apps.apple.com/...',
  androidUrl: 'https://play.google.com/...',
  webUrl: 'https://myapp.com',
  fallbackUrl: 'https://myapp.com/download',
});

// Get a link
const link = await client.links.get('link-id');

// Update a link
const updated = await client.links.update('link-id', {
  title: 'New Title',
  isActive: false,
});

// Delete a link
await client.links.delete('link-id');
```

### Analytics

Access detailed click analytics for your links.

```typescript
// Get overview stats
const stats = await client.analytics.getStats('link-id', '30d');

// Get timeseries data
const timeseries = await client.analytics.getTimeseries('link-id', '7d');

// Get platform breakdown
const platforms = await client.analytics.getPlatforms('link-id', '30d');

// Get country breakdown
const countries = await client.analytics.getCountries('link-id', '30d', 10);

// Get referrer breakdown
const referrers = await client.analytics.getReferrers('link-id', '30d', 10);
```

### Domains

Add and manage custom domains.

```typescript
// List domains
const domains = await client.domains.list();

// Add a domain
const domain = await client.domains.create('links.myapp.com');

// Verify a domain
const verified = await client.domains.verify('domain-id');

// Delete a domain
await client.domains.delete('domain-id');
```

### QR Codes

Generate customizable QR codes for your links.

```typescript
const qr = await client.qr.generate({
  linkId: 'link-id',
  size: 512,
  format: 'png',
  foregroundColor: '#000000',
  backgroundColor: '#FFFFFF',
});
console.log(`QR Code URL: ${qr.url}`);
```

### Integrations

Connect with third-party services (Slack, Discord, Telegram, etc.).

```typescript
import { IntegrationType } from '@go2ge/sdk';

// List integrations
const integrations = await client.integrations.list();

// Create an integration
const integration = await client.integrations.create({
  type: IntegrationType.SLACK,
  name: 'Marketing Alerts',
  config: { webhookUrl: 'https://hooks.slack.com/...' },
  events: ['click_alert', 'click_milestone'],
});

// Test an integration
const result = await client.integrations.test('integration-id');

// Delete an integration
await client.integrations.delete('integration-id');
```

### Campaigns

Create SMS/Email marketing campaigns with bulk trackable links.

```typescript
// Create a campaign
const campaign = await client.campaigns.create({
  name: 'Summer Sale 2024',
  baseLinkId: 'link-id',
  type: 'sms',
  utmSource: 'sms',
  utmCampaign: 'summer_sale',
});

// Generate unique links for recipients
const result = await client.campaigns.generateLinks(campaign.id, [
  { identifier: '+1234567890', metadata: { name: 'John' } },
  { identifier: '+0987654321', metadata: { name: 'Jane' } },
]);

// Get campaign stats
const stats = await client.campaigns.getStats(campaign.id);
console.log(`Click rate: ${stats.clickRate}%`);

// Export links
const exportData = await client.campaigns.exportLinks(campaign.id, 'csv');
```

## Error Handling

```typescript
import {
  Go2Client,
  Go2Error,
  NotFoundError,
  AuthenticationError,
  ValidationError,
  RateLimitError,
} from '@go2ge/sdk';

try {
  const link = await client.links.get('invalid-id');
} catch (error) {
  if (error instanceof NotFoundError) {
    console.log('Link not found');
  } else if (error instanceof AuthenticationError) {
    console.log('Invalid API key');
  } else if (error instanceof ValidationError) {
    console.log(`Validation error: ${error.message}`);
  } else if (error instanceof RateLimitError) {
    console.log('Rate limit exceeded, try again later');
  } else if (error instanceof Go2Error) {
    console.log(`API error: ${error.message}`);
  }
}
```

## Configuration

```typescript
// Production (default)
const client = new Go2Client({ apiKey: 'go2_xxx' });

// Custom endpoint (for development)
const client = new Go2Client({
  apiKey: 'go2_xxx',
  endpoint: 'localhost:9090',
  insecure: true, // Disable TLS for local dev
});
```

## TypeScript Support

This SDK is written in TypeScript and provides full type definitions.

```typescript
import type {
  Link,
  LinkStats,
  Campaign,
  Integration,
  Domain,
  QRCode,
} from '@go2ge/sdk';
```

## Documentation

Full API documentation: **https://app.go2.ge/docs#sdks**

## Requirements

- Node.js 16+
- TypeScript 4.5+ (for TypeScript users)

## License

MIT
