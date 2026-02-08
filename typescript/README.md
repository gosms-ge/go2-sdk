# Go2 SDK for Node.js/TypeScript

Official TypeScript/Node.js SDK for the Go2 gRPC API.

## Installation

```bash
npm install @go2/sdk
# or
yarn add @go2/sdk
# or
pnpm add @go2/sdk
```

## Quick Start

```typescript
import { Go2Client, IntegrationType } from '@go2/sdk';

const client = new Go2Client({ apiKey: 'go2_your_api_key' });

try {
  // List integrations
  const integrations = await client.integrations.list();

  for (const integration of integrations) {
    console.log(`Integration: ${integration.name} (${integration.type})`);
  }
} finally {
  client.close();
}
```

## Creating an Integration

```typescript
import { Go2Client, IntegrationType } from '@go2/sdk';

const client = new Go2Client({ apiKey: 'go2_xxx' });

const integration = await client.integrations.create({
  type: IntegrationType.SLACK,
  name: 'My Slack Alerts',
  config: {
    webhookUrl: 'https://hooks.slack.com/services/...',
  },
  events: ['click_alert', 'link_created'],
});

console.log(`Created integration: ${integration.id}`);

client.close();
```

## Updating an Integration

```typescript
const updated = await client.integrations.update('integration-id', {
  name: 'Updated Name',
  isActive: true,
});
```

## Testing an Integration

```typescript
const result = await client.integrations.test('integration-id');

if (result.success) {
  console.log('Test notification sent successfully!');
} else {
  console.log(`Test failed: ${result.message}`);
}
```

## Error Handling

```typescript
import {
  Go2Client,
  NotFoundError,
  AuthenticationError,
  ValidationError,
} from '@go2/sdk';

try {
  const integration = await client.integrations.get('invalid-id');
} catch (error) {
  if (error instanceof NotFoundError) {
    console.log('Integration not found');
  } else if (error instanceof AuthenticationError) {
    console.log('Invalid API key');
  } else if (error instanceof ValidationError) {
    console.log(`Validation error: ${error.message}`);
  } else {
    console.error('Error:', error);
  }
}
```

## Configuration Options

```typescript
// Custom endpoint (for development)
const client = new Go2Client({
  apiKey: 'go2_xxx',
  endpoint: 'localhost:9090',
  insecure: true, // Disable TLS for local dev
});
```

## Available Integration Types

```typescript
enum IntegrationType {
  UNSPECIFIED = 0,
  SLACK = 1,
  DISCORD = 2,
  TELEGRAM = 3,
  SEGMENT = 4,
  ZAPIER = 5,
}
```

## TypeScript Support

This SDK is written in TypeScript and provides full type definitions out of the box.

```typescript
import type {
  Integration,
  IntegrationConfig,
  CreateIntegrationParams,
  UpdateIntegrationParams,
} from '@go2/sdk';
```

## Requirements

- Node.js 16+
- TypeScript 4.5+ (for TypeScript users)

## License

MIT
