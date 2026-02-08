/**
 * Integration types supported by Go2.
 */
export enum IntegrationType {
  UNSPECIFIED = 0,
  SLACK = 1,
  DISCORD = 2,
  TELEGRAM = 3,
  SEGMENT = 4,
  ZAPIER = 5,
}

/**
 * Integration configuration.
 */
export interface IntegrationConfig {
  /** Webhook URL for Slack/Discord/Zapier */
  webhookUrl?: string;
  /** Channel for Slack */
  channel?: string;
  /** Bot token for Telegram */
  botToken?: string;
  /** Chat ID for Telegram */
  chatId?: string;
  /** Write key for Segment */
  writeKey?: string;
}

/**
 * Integration resource.
 */
export interface Integration {
  id: string;
  userId: string;
  type: IntegrationType;
  name: string;
  config: IntegrationConfig;
  events: string[];
  isActive: boolean;
  lastTriggeredAt?: Date;
  triggerCount: number;
  createdAt: Date;
  updatedAt: Date;
}

/**
 * Parameters for creating an integration.
 */
export interface CreateIntegrationParams {
  type: IntegrationType;
  name: string;
  config: IntegrationConfig;
  events: string[];
}

/**
 * Parameters for updating an integration.
 */
export interface UpdateIntegrationParams {
  name?: string;
  config?: IntegrationConfig;
  events?: string[];
  isActive?: boolean;
}

/**
 * Response from testing an integration.
 */
export interface TestIntegrationResponse {
  success: boolean;
  message: string;
}

/**
 * Integration type information.
 */
export interface IntegrationTypeInfo {
  type: IntegrationType;
  name: string;
  description: string;
  icon: string;
  available: boolean;
  configFields: ConfigField[];
}

/**
 * Configuration field description.
 */
export interface ConfigField {
  name: string;
  label: string;
  fieldType: string;
  required: boolean;
  placeholder: string;
  helpText: string;
}

/**
 * Response from getting integration types.
 */
export interface GetIntegrationTypesResponse {
  types: IntegrationTypeInfo[];
  events: string[];
}
