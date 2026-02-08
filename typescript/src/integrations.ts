import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';
import { wrapError } from './errors';
import type {
  Integration,
  CreateIntegrationParams,
  UpdateIntegrationParams,
  TestIntegrationResponse,
  GetIntegrationTypesResponse,
} from './types';

// Load proto file
const PROTO_PATH = path.join(__dirname, '../proto/integrations/v1/integrations.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: false,
  longs: String,
  enums: Number,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const IntegrationServiceClient = protoDescriptor.integrations.v1.IntegrationService;

/**
 * Service for managing integrations.
 */
export class IntegrationsService {
  private client: any;

  constructor(
    endpoint: string,
    credentials: grpc.ChannelCredentials,
    options: grpc.ClientOptions
  ) {
    this.client = new IntegrationServiceClient(endpoint, credentials, options);
  }

  /**
   * List all integrations.
   */
  async list(): Promise<Integration[]> {
    return new Promise((resolve, reject) => {
      this.client.listIntegrations(
        {},
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapIntegrations(response?.integrations || []));
          }
        }
      );
    });
  }

  /**
   * Create a new integration.
   */
  async create(params: CreateIntegrationParams): Promise<Integration> {
    const request: any = {
      type: params.type,
      name: params.name,
      events: params.events,
    };

    if (params.config) {
      request.config = {
        webhookUrl: params.config.webhookUrl,
        channel: params.config.channel,
        botToken: params.config.botToken,
        chatId: params.config.chatId,
        writeKey: params.config.writeKey,
      };
    }

    return new Promise((resolve, reject) => {
      this.client.createIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapIntegration(response));
          }
        }
      );
    });
  }

  /**
   * Get an integration by ID.
   */
  async get(id: string): Promise<Integration> {
    return new Promise((resolve, reject) => {
      this.client.getIntegration(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapIntegration(response));
          }
        }
      );
    });
  }

  /**
   * Update an integration.
   */
  async update(id: string, params: UpdateIntegrationParams): Promise<Integration> {
    const request: any = { id };

    if (params.name !== undefined) request.name = params.name;
    if (params.events !== undefined) request.events = params.events;
    if (params.isActive !== undefined) request.isActive = params.isActive;

    if (params.config) {
      request.config = {
        webhookUrl: params.config.webhookUrl,
        channel: params.config.channel,
        botToken: params.config.botToken,
        chatId: params.config.chatId,
        writeKey: params.config.writeKey,
      };
    }

    return new Promise((resolve, reject) => {
      this.client.updateIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapIntegration(response));
          }
        }
      );
    });
  }

  /**
   * Delete an integration.
   */
  async delete(id: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
      this.client.deleteIntegration(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(response?.success || false);
          }
        }
      );
    });
  }

  /**
   * Test an integration by sending a test notification.
   */
  async test(id: string): Promise<TestIntegrationResponse> {
    return new Promise((resolve, reject) => {
      this.client.testIntegration(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              success: response?.success || false,
              message: response?.message || '',
            });
          }
        }
      );
    });
  }

  /**
   * Get available integration types and events.
   */
  async getTypes(): Promise<GetIntegrationTypesResponse> {
    return new Promise((resolve, reject) => {
      this.client.getIntegrationTypes(
        {},
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              types: response?.types || [],
              events: response?.events || [],
            });
          }
        }
      );
    });
  }

  /**
   * Close the service connection.
   */
  close(): void {
    this.client?.close?.();
  }

  private mapIntegration(raw: any): Integration {
    return {
      id: raw.id,
      userId: raw.userId,
      type: raw.type,
      name: raw.name,
      config: {
        webhookUrl: raw.config?.webhookUrl,
        channel: raw.config?.channel,
        botToken: raw.config?.botToken,
        chatId: raw.config?.chatId,
        writeKey: raw.config?.writeKey,
      },
      events: raw.events || [],
      isActive: raw.isActive,
      lastTriggeredAt: raw.lastTriggeredAt ? new Date(raw.lastTriggeredAt) : undefined,
      triggerCount: raw.triggerCount || 0,
      createdAt: new Date(raw.createdAt),
      updatedAt: new Date(raw.updatedAt),
    };
  }

  private mapIntegrations(rawList: any[]): Integration[] {
    return rawList.map((raw) => this.mapIntegration(raw));
  }
}
