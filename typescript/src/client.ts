import * as grpc from '@grpc/grpc-js';
import { IntegrationsService } from './integrations';

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
 * try {
 *   const integrations = await client.integrations.list();
 *   console.log(integrations);
 * } finally {
 *   client.close();
 * }
 * ```
 */
export class Go2Client {
  private channel: grpc.Channel | null = null;

  /** Service for managing integrations */
  public readonly integrations: IntegrationsService;

  constructor(options: Go2ClientOptions) {
    if (!options.apiKey) {
      throw new Error('API key is required');
    }

    const endpoint = options.endpoint || DEFAULT_ENDPOINT;

    // Create credentials
    const credentials = options.insecure
      ? grpc.credentials.createInsecure()
      : grpc.credentials.createSsl();

    // Create channel options with interceptors
    const channelOptions: grpc.ClientOptions = {
      interceptors: [createAuthInterceptor(options.apiKey)],
    };

    // Create service clients
    this.integrations = new IntegrationsService(
      endpoint,
      credentials,
      channelOptions
    );
  }

  /**
   * Close the client connection.
   */
  close(): void {
    this.integrations.close();
  }
}
