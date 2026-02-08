import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';
import { wrapError } from './errors';

const PROTO_PATH = path.join(__dirname, '../proto/campaigns/v1/campaigns.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: false,
  longs: String,
  enums: Number,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const CampaignServiceClient = protoDescriptor.campaigns.v1.CampaignService;

export interface Campaign {
  id: string;
  userId: string;
  name: string;
  description?: string;
  destinationUrl: string;
  passRecipientId: boolean;
  recipientParamName: string;
  totalRecipients: number;
  totalClicks: number;
  uniqueClicks: number;
  status: 'active' | 'paused' | 'completed' | 'archived';
  createdAt: Date;
  updatedAt: Date;
  expiresAt?: Date;
}

export interface CampaignLink {
  id: string;
  campaignId: string;
  slug: string;
  recipientId: string;
  recipientName?: string;
  recipientMetadata?: Record<string, string>;
  clicked: boolean;
  firstClickedAt?: Date;
  lastClickedAt?: Date;
  clickCount: number;
  firstClickPlatform?: string;
  firstClickCountry?: string;
  firstClickCity?: string;
  createdAt: Date;
  shortUrl: string;
}

export interface Recipient {
  id: string;
  name?: string;
  metadata?: Record<string, string>;
}

export interface CreateCampaignParams {
  name: string;
  description?: string;
  destinationUrl: string;
  passRecipientId?: boolean;
  recipientParamName?: string;
  expiresAt?: Date;
}

export interface UpdateCampaignParams {
  name?: string;
  description?: string;
  destinationUrl?: string;
  passRecipientId?: boolean;
  recipientParamName?: string;
  status?: 'active' | 'paused' | 'completed' | 'archived';
  expiresAt?: Date;
}

export interface GenerateLinksResult {
  campaignId: string;
  linksCreated: number;
  sampleLinks: CampaignLink[];
}

export interface CampaignStats {
  campaignId: string;
  totalRecipients: number;
  totalClicks: number;
  uniqueClicks: number;
  clickRate: number;
  clicksByPlatform: Record<string, number>;
  clicksByCountry: Record<string, number>;
  clicksByDay: Record<string, number>;
}

export interface ListCampaignsFilters {
  status?: string;
  search?: string;
}

export interface ListCampaignLinksFilters {
  clickedOnly?: boolean;
  search?: string;
}

/**
 * Service for managing SMS/Email marketing campaigns with bulk trackable links.
 */
export class CampaignsService {
  private client: any;

  constructor(
    endpoint: string,
    credentials: grpc.ChannelCredentials,
    options: grpc.ClientOptions
  ) {
    this.client = new CampaignServiceClient(endpoint, credentials, options);
  }

  /**
   * List all campaigns with optional filters.
   */
  async list(
    limit: number = 20,
    offset: number = 0,
    filters?: ListCampaignsFilters
  ): Promise<{ campaigns: Campaign[]; total: number }> {
    return new Promise((resolve, reject) => {
      this.client.listCampaigns(
        {
          limit,
          offset,
          status: filters?.status || '',
          search: filters?.search || '',
        },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              campaigns: (response?.campaigns || []).map(this.mapCampaign),
              total: response?.total || 0,
            });
          }
        }
      );
    });
  }

  /**
   * Create a new campaign.
   */
  async create(params: CreateCampaignParams): Promise<Campaign> {
    return new Promise((resolve, reject) => {
      this.client.createCampaign(
        {
          name: params.name,
          description: params.description || '',
          destinationUrl: params.destinationUrl,
          passRecipientId: params.passRecipientId || false,
          recipientParamName: params.recipientParamName || 'rid',
          expiresAt: params.expiresAt?.toISOString() || '',
        },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapCampaign(response));
          }
        }
      );
    });
  }

  /**
   * Get a campaign by ID.
   */
  async get(id: string): Promise<Campaign> {
    return new Promise((resolve, reject) => {
      this.client.getCampaign(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapCampaign(response));
          }
        }
      );
    });
  }

  /**
   * Update a campaign.
   */
  async update(id: string, params: UpdateCampaignParams): Promise<Campaign> {
    return new Promise((resolve, reject) => {
      this.client.updateCampaign(
        {
          id,
          name: params.name || '',
          description: params.description || '',
          destinationUrl: params.destinationUrl || '',
          passRecipientId: params.passRecipientId ?? false,
          recipientParamName: params.recipientParamName || '',
          status: params.status || '',
          expiresAt: params.expiresAt?.toISOString() || '',
        },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapCampaign(response));
          }
        }
      );
    });
  }

  /**
   * Delete a campaign.
   */
  async delete(id: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
      this.client.deleteCampaign(
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
   * Generate links for campaign recipients in bulk.
   * @param campaignId - The campaign ID
   * @param recipients - Array of recipients (max 100,000 per request)
   */
  async generateLinks(
    campaignId: string,
    recipients: Recipient[]
  ): Promise<GenerateLinksResult> {
    return new Promise((resolve, reject) => {
      this.client.generateLinks(
        {
          campaignId,
          recipients: recipients.map((r) => ({
            id: r.id,
            name: r.name || '',
            metadata: r.metadata || {},
          })),
        },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              campaignId: response?.campaignId || '',
              linksCreated: response?.linksCreated || 0,
              sampleLinks: (response?.sampleLinks || []).map(this.mapCampaignLink),
            });
          }
        }
      );
    });
  }

  /**
   * List campaign links with pagination.
   */
  async listLinks(
    campaignId: string,
    limit: number = 50,
    offset: number = 0,
    filters?: ListCampaignLinksFilters
  ): Promise<{ links: CampaignLink[]; total: number }> {
    return new Promise((resolve, reject) => {
      this.client.listCampaignLinks(
        {
          campaignId,
          limit,
          offset,
          clickedOnly: filters?.clickedOnly || false,
          search: filters?.search || '',
        },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              links: (response?.links || []).map(this.mapCampaignLink),
              total: response?.total || 0,
            });
          }
        }
      );
    });
  }

  /**
   * Get campaign statistics.
   */
  async getStats(campaignId: string): Promise<CampaignStats> {
    return new Promise((resolve, reject) => {
      this.client.getCampaignStats(
        { campaignId },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              campaignId: response?.campaignId || '',
              totalRecipients: response?.totalRecipients || 0,
              totalClicks: parseInt(response?.totalClicks) || 0,
              uniqueClicks: response?.uniqueClicks || 0,
              clickRate: response?.clickRate || 0,
              clicksByPlatform: this.mapInt64Map(response?.clicksByPlatform),
              clicksByCountry: this.mapInt64Map(response?.clicksByCountry),
              clicksByDay: this.mapInt64Map(response?.clicksByDay),
            });
          }
        }
      );
    });
  }

  /**
   * Export all campaign links.
   */
  async exportLinks(campaignId: string): Promise<CampaignLink[]> {
    return new Promise((resolve, reject) => {
      this.client.exportLinks(
        { campaignId, format: 'json' },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve((response?.links || []).map(this.mapCampaignLink));
          }
        }
      );
    });
  }

  close(): void {
    this.client?.close?.();
  }

  private mapCampaign(raw: any): Campaign {
    return {
      id: raw.id,
      userId: raw.userId,
      name: raw.name,
      description: raw.description || undefined,
      destinationUrl: raw.destinationUrl,
      passRecipientId: raw.passRecipientId,
      recipientParamName: raw.recipientParamName,
      totalRecipients: raw.totalRecipients || 0,
      totalClicks: parseInt(raw.totalClicks) || 0,
      uniqueClicks: raw.uniqueClicks || 0,
      status: raw.status,
      createdAt: new Date(raw.createdAt),
      updatedAt: new Date(raw.updatedAt),
      expiresAt: raw.expiresAt ? new Date(raw.expiresAt) : undefined,
    };
  }

  private mapCampaignLink(raw: any): CampaignLink {
    return {
      id: raw.id,
      campaignId: raw.campaignId,
      slug: raw.slug,
      recipientId: raw.recipientId,
      recipientName: raw.recipientName || undefined,
      recipientMetadata: raw.recipientMetadata || undefined,
      clicked: raw.clicked,
      firstClickedAt: raw.firstClickedAt ? new Date(raw.firstClickedAt) : undefined,
      lastClickedAt: raw.lastClickedAt ? new Date(raw.lastClickedAt) : undefined,
      clickCount: raw.clickCount || 0,
      firstClickPlatform: raw.firstClickPlatform || undefined,
      firstClickCountry: raw.firstClickCountry || undefined,
      firstClickCity: raw.firstClickCity || undefined,
      createdAt: new Date(raw.createdAt),
      shortUrl: raw.shortUrl,
    };
  }

  private mapInt64Map(raw: any): Record<string, number> {
    if (!raw) return {};
    const result: Record<string, number> = {};
    for (const key of Object.keys(raw)) {
      result[key] = parseInt(raw[key]) || 0;
    }
    return result;
  }
}
