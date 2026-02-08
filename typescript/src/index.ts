/**
 * Go2 SDK - Official TypeScript/Node.js SDK for the Go2 gRPC API.
 *
 * @example
 * ```typescript
 * import { Go2Client, IntegrationType } from '@go2/sdk';
 *
 * const client = new Go2Client({ apiKey: 'go2_your_key' });
 *
 * const integration = await client.integrations.create({
 *   type: IntegrationType.INTEGRATION_TYPE_SLACK,
 *   name: 'My Slack Integration',
 *   webhookUrl: 'https://hooks.slack.com/...',
 *   events: ['click_alert'],
 * });
 *
 * client.close();
 * ```
 *
 * @packageDocumentation
 */

export { Go2Client, Go2ClientOptions } from './client';
export { IntegrationsService } from './integrations';
export {
  Go2Error,
  AuthenticationError,
  NotFoundError,
  PermissionDeniedError,
  ValidationError,
  RateLimitError,
} from './errors';

// Re-export types from generated code (when available)
export * from './types';
