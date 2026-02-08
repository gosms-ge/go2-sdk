import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';
import { wrapError } from './errors';

const PROTO_PATH = path.join(__dirname, '../proto/links/v1/links.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: false,
  longs: String,
  enums: Number,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const LinkServiceClient = protoDescriptor.links.v1.LinkService;

/**
 * Link resource.
 */
export interface Link {
  id: string;
  userId: string;
  slug: string;
  title: string;
  iosUrl?: string;
  androidUrl?: string;
  webUrl?: string;
  fallbackUrl?: string;
  huaweiUrl?: string;
  amazonUrl?: string;
  windowsUrl?: string;
  macosUrl?: string;
  appName?: string;
  appIconUrl?: string;
  description?: string;
  isActive: boolean;
  totalClicks: number;
  createdAt: Date;
  updatedAt: Date;
}

/**
 * Parameters for creating a link.
 */
export interface CreateLinkParams {
  slug: string;
  title: string;
  iosUrl?: string;
  androidUrl?: string;
  webUrl?: string;
  fallbackUrl?: string;
  huaweiUrl?: string;
  amazonUrl?: string;
  windowsUrl?: string;
  macosUrl?: string;
  appName?: string;
  appIconUrl?: string;
  description?: string;
}

/**
 * Parameters for updating a link.
 */
export interface UpdateLinkParams {
  slug?: string;
  title?: string;
  iosUrl?: string;
  androidUrl?: string;
  webUrl?: string;
  fallbackUrl?: string;
  isActive?: boolean;
}

/**
 * Service for managing links.
 */
export class LinksService {
  private client: any;

  constructor(
    endpoint: string,
    credentials: grpc.ChannelCredentials,
    options: grpc.ClientOptions
  ) {
    this.client = new LinkServiceClient(endpoint, credentials, options);
  }

  /**
   * List all links with pagination.
   */
  async list(page = 1, perPage = 20): Promise<{ links: Link[]; total: number }> {
    return new Promise((resolve, reject) => {
      this.client.listLinks(
        { page, perPage },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              links: (response?.links || []).map(this.mapLink),
              total: response?.total || 0,
            });
          }
        }
      );
    });
  }

  /**
   * Create a new link.
   */
  async create(params: CreateLinkParams): Promise<Link> {
    return new Promise((resolve, reject) => {
      this.client.createLink(
        params,
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapLink(response));
          }
        }
      );
    });
  }

  /**
   * Get a link by ID.
   */
  async get(id: string): Promise<Link> {
    return new Promise((resolve, reject) => {
      this.client.getLink(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapLink(response));
          }
        }
      );
    });
  }

  /**
   * Update a link.
   */
  async update(id: string, params: UpdateLinkParams): Promise<Link> {
    return new Promise((resolve, reject) => {
      this.client.updateLink(
        { id, ...params },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapLink(response));
          }
        }
      );
    });
  }

  /**
   * Delete a link.
   */
  async delete(id: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
      this.client.deleteLink(
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
   * Check if a slug is available.
   */
  async checkSlug(slug: string): Promise<{ available: boolean; slug: string }> {
    return new Promise((resolve, reject) => {
      this.client.checkSlug(
        { slug },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              available: response?.available || false,
              slug: response?.slug || slug,
            });
          }
        }
      );
    });
  }

  close(): void {
    this.client?.close?.();
  }

  private mapLink(raw: any): Link {
    return {
      id: raw.id,
      userId: raw.userId,
      slug: raw.slug,
      title: raw.title,
      iosUrl: raw.iosUrl,
      androidUrl: raw.androidUrl,
      webUrl: raw.webUrl,
      fallbackUrl: raw.fallbackUrl,
      huaweiUrl: raw.huaweiUrl,
      amazonUrl: raw.amazonUrl,
      windowsUrl: raw.windowsUrl,
      macosUrl: raw.macosUrl,
      appName: raw.appName,
      appIconUrl: raw.appIconUrl,
      description: raw.description,
      isActive: raw.isActive,
      totalClicks: parseInt(raw.totalClicks) || 0,
      createdAt: new Date(raw.createdAt),
      updatedAt: new Date(raw.updatedAt),
    };
  }
}
