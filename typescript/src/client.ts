import * as grpc from '@grpc/grpc-js';
import { IntegrationsService } from './integrations';
import { LinksService } from './links';
import { AnalyticsService } from './analytics';
import { DomainsService } from './domains';
import { QRService } from './qr';
import { CampaignsService } from './campaigns';

const DEFAULT_ENDPOINT = 'grpc.go2.ge:443';

/**
 * Options for creating a Go2Client.
 */
export interface Go2ClientOptions {
  /** Your Go2 API key (required) */
  apiKey: string;
  /** gRPC endpoint (default: grpc.go2.ge:443) */
  endpoint?: string;
  /** Use insecure connection for local development */
  insecure?: boolean;
}

/**
 * Creates an auth interceptor that adds the API key to all requests.
 */
function createAuthInterceptor(apiKey: string): grpc.Interceptor {
  return (options, nextCall) => {
    return new grpc.InterceptingCall(nextCall(options), {
      start: (metadata, listener, next) => {
        metadata.add('x-api-key', apiKey);
        next(metadata, listener);
      },
    });
  };
}

/**
 * Go2 gRPC API Client.
 *
 * @example
 * ```typescript
 * const client = new Go2Client({ apiKey: 'go2_xxx' });
 *
 * // Links
 * const links = await client.links.list();
 * const link = await client.links.create({ slug: 'myapp', title: 'My App' });
 *
 * // Analytics
 * const stats = await client.analytics.getStats(link.id);
 *
 * // Integrations
 * const integrations = await client.integrations.list();
 *
 * // Domains
 * const domains = await client.domains.list();
 *
 * // QR Codes
 * const qr = await client.qr.generate({ linkId: link.id });
 *
 * client.close();
 * ```
 */
export class Go2Client {
  private endpoint: string;
  private credentials: grpc.ChannelCredentials;
  private channelOptions: grpc.ClientOptions;

  /** Service for managing smart links */
  public readonly links: LinksService;

  /** Service for link analytics */
  public readonly analytics: AnalyticsService;

  /** Service for managing integrations */
  public readonly integrations: IntegrationsService;

  /** Service for managing custom domains */
  public readonly domains: DomainsService;

  /** Service for QR code generation */
  public readonly qr: QRService;

  /** Service for managing marketing campaigns */
  public readonly campaigns: CampaignsService;

  constructor(options: Go2ClientOptions) {
    if (!options.apiKey) {
      throw new Error('API key is required');
    }

    this.endpoint = options.endpoint || DEFAULT_ENDPOINT;

    // Create credentials
    this.credentials = options.insecure
      ? grpc.credentials.createInsecure()
      : grpc.credentials.createSsl();

    // Create channel options with interceptors
    this.channelOptions = {
      interceptors: [createAuthInterceptor(options.apiKey)],
    };

    // Create service clients
    this.links = new LinksService(
      this.endpoint,
      this.credentials,
      this.channelOptions
    );

    this.analytics = new AnalyticsService(
      this.endpoint,
      this.credentials,
      this.channelOptions
    );

    this.integrations = new IntegrationsService(
      this.endpoint,
      this.credentials,
      this.channelOptions
    );

    this.domains = new DomainsService(
      this.endpoint,
      this.credentials,
      this.channelOptions
    );

    this.qr = new QRService(
      this.endpoint,
      this.credentials,
      this.channelOptions
    );

    this.campaigns = new CampaignsService(
      this.endpoint,
      this.credentials,
      this.channelOptions
    );
  }

  /**
   * Close the client connection.
   */
  close(): void {
    this.links.close();
    this.analytics.close();
    this.integrations.close();
    this.domains.close();
    this.qr.close();
    this.campaigns.close();
  }
}
