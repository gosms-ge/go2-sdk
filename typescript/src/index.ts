/**
 * Go2 SDK - Official TypeScript/Node.js SDK for the Go2 gRPC API.
 *
 * @example
 * ```typescript
 * import { Go2Client } from '@go2ge/sdk';
 *
 * const client = new Go2Client({ apiKey: 'go2_your_key' });
 *
 * // Create a smart link
 * const link = await client.links.create({
 *   slug: 'myapp',
 *   title: 'My Awesome App',
 *   iosUrl: 'https://apps.apple.com/...',
 *   androidUrl: 'https://play.google.com/...',
 * });
 *
 * // Get analytics
 * const stats = await client.analytics.getStats(link.id);
 *
 * // Generate QR code
 * const qr = await client.qr.generate({ linkId: link.id });
 *
 * client.close();
 * ```
 *
 * @packageDocumentation
 */

// Main client
export { Go2Client, Go2ClientOptions } from './client';

// Services
export { LinksService, Link, CreateLinkParams, UpdateLinkParams } from './links';
export { AnalyticsService, Stats, TimeseriesPoint, PlatformStats, CountryStats, ReferrerStats } from './analytics';
export { IntegrationsService } from './integrations';
export { DomainsService, Domain, DomainStatus, SSLStatus, DNSRecord, CreateDomainResponse } from './domains';
export { QRService, QRCode, GenerateQRParams } from './qr';

// Errors
export {
  Go2Error,
  AuthenticationError,
  NotFoundError,
  PermissionDeniedError,
  ValidationError,
  RateLimitError,
} from './errors';

// Types from integrations
export * from './types';
