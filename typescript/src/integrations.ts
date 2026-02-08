import * as grpc from '@grpc/grpc-js';
import { wrapError } from './errors';
import type {
  Integration,
  IntegrationType,
  IntegrationConfig,
  CreateIntegrationParams,
  UpdateIntegrationParams,
  TestIntegrationResponse,
  GetIntegrationTypesResponse,
} from './types';

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
    // Dynamic import of generated client
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { IntegrationServiceClient } = require('./gen/integrations/v1/integrations_grpc_pb');
    this.client = new IntegrationServiceClient(endpoint, credentials, options);
  }

  /**
   * List all integrations.
   */
  async list(): Promise<Integration[]> {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { ListIntegrationsRequest } = require('./gen/integrations/v1/integrations_pb');

    return new Promise((resolve, reject) => {
      this.client.listIntegrations(
        new ListIntegrationsRequest(),
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(response?.getIntegrationsList() || []);
          }
        }
      );
    });
  }

  /**
   * Create a new integration.
   */
  async create(params: CreateIntegrationParams): Promise<Integration> {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { CreateIntegrationRequest, IntegrationConfig } = require('./gen/integrations/v1/integrations_pb');

    const request = new CreateIntegrationRequest();
    request.setType(params.type);
    request.setName(params.name);
    request.setEventsList(params.events);

    if (params.config) {
      const config = new IntegrationConfig();
      if (params.config.webhookUrl) config.setWebhookUrl(params.config.webhookUrl);
      if (params.config.channel) config.setChannel(params.config.channel);
      if (params.config.botToken) config.setBotToken(params.config.botToken);
      if (params.config.chatId) config.setChatId(params.config.chatId);
      if (params.config.writeKey) config.setWriteKey(params.config.writeKey);
      request.setConfig(config);
    }

    return new Promise((resolve, reject) => {
      this.client.createIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(response);
          }
        }
      );
    });
  }

  /**
   * Get an integration by ID.
   */
  async get(id: string): Promise<Integration> {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { GetIntegrationRequest } = require('./gen/integrations/v1/integrations_pb');

    const request = new GetIntegrationRequest();
    request.setId(id);

    return new Promise((resolve, reject) => {
      this.client.getIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(response);
          }
        }
      );
    });
  }

  /**
   * Update an integration.
   */
  async update(id: string, params: UpdateIntegrationParams): Promise<Integration> {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { UpdateIntegrationRequest, IntegrationConfig } = require('./gen/integrations/v1/integrations_pb');

    const request = new UpdateIntegrationRequest();
    request.setId(id);

    if (params.name !== undefined) request.setName(params.name);
    if (params.events !== undefined) request.setEventsList(params.events);
    if (params.isActive !== undefined) request.setIsActive(params.isActive);

    if (params.config) {
      const config = new IntegrationConfig();
      if (params.config.webhookUrl) config.setWebhookUrl(params.config.webhookUrl);
      if (params.config.channel) config.setChannel(params.config.channel);
      if (params.config.botToken) config.setBotToken(params.config.botToken);
      if (params.config.chatId) config.setChatId(params.config.chatId);
      if (params.config.writeKey) config.setWriteKey(params.config.writeKey);
      request.setConfig(config);
    }

    return new Promise((resolve, reject) => {
      this.client.updateIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(response);
          }
        }
      );
    });
  }

  /**
   * Delete an integration.
   */
  async delete(id: string): Promise<boolean> {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { DeleteIntegrationRequest } = require('./gen/integrations/v1/integrations_pb');

    const request = new DeleteIntegrationRequest();
    request.setId(id);

    return new Promise((resolve, reject) => {
      this.client.deleteIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(response?.getSuccess() || false);
          }
        }
      );
    });
  }

  /**
   * Test an integration by sending a test notification.
   */
  async test(id: string): Promise<TestIntegrationResponse> {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { TestIntegrationRequest } = require('./gen/integrations/v1/integrations_pb');

    const request = new TestIntegrationRequest();
    request.setId(id);

    return new Promise((resolve, reject) => {
      this.client.testIntegration(
        request,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              success: response?.getSuccess() || false,
              message: response?.getMessage() || '',
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
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    const { GetIntegrationTypesRequest } = require('./gen/integrations/v1/integrations_pb');

    return new Promise((resolve, reject) => {
      this.client.getIntegrationTypes(
        new GetIntegrationTypesRequest(),
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              types: response?.getTypesList() || [],
              events: response?.getEventsList() || [],
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
}
