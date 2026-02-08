import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';
import { wrapError } from './errors';

const PROTO_PATH = path.join(__dirname, '../proto/domains/v1/domains.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: false,
  longs: String,
  enums: Number,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const DomainServiceClient = protoDescriptor.domains.v1.DomainService;

export enum DomainStatus {
  UNSPECIFIED = 0,
  PENDING = 1,
  VERIFYING = 2,
  ACTIVE = 3,
  FAILED = 4,
}

export enum SSLStatus {
  UNSPECIFIED = 0,
  PENDING = 1,
  PROVISIONING = 2,
  ACTIVE = 3,
  FAILED = 4,
}

export interface Domain {
  id: string;
  userId: string;
  domain: string;
  status: DomainStatus;
  verificationToken: string;
  verifiedAt?: Date;
  sslStatus: SSLStatus;
  createdAt: Date;
  updatedAt: Date;
}

export interface DNSRecord {
  type: string;
  name: string;
  value: string;
}

export interface CreateDomainResponse {
  domain: Domain;
  dnsRecords: DNSRecord[];
}

/**
 * Service for managing custom domains.
 */
export class DomainsService {
  private client: any;

  constructor(
    endpoint: string,
    credentials: grpc.ChannelCredentials,
    options: grpc.ClientOptions
  ) {
    this.client = new DomainServiceClient(endpoint, credentials, options);
  }

  /**
   * List all custom domains.
   */
  async list(): Promise<Domain[]> {
    return new Promise((resolve, reject) => {
      this.client.listDomains(
        {},
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve((response?.domains || []).map(this.mapDomain));
          }
        }
      );
    });
  }

  /**
   * Add a new custom domain.
   */
  async create(domain: string): Promise<CreateDomainResponse> {
    return new Promise((resolve, reject) => {
      this.client.createDomain(
        { domain },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              domain: this.mapDomain(response?.domain),
              dnsRecords: response?.dnsRecords || [],
            });
          }
        }
      );
    });
  }

  /**
   * Get a domain by ID.
   */
  async get(id: string): Promise<Domain> {
    return new Promise((resolve, reject) => {
      this.client.getDomain(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapDomain(response));
          }
        }
      );
    });
  }

  /**
   * Verify a domain.
   */
  async verify(id: string): Promise<Domain> {
    return new Promise((resolve, reject) => {
      this.client.verifyDomain(
        { id },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(this.mapDomain(response));
          }
        }
      );
    });
  }

  /**
   * Delete a domain.
   */
  async delete(id: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
      this.client.deleteDomain(
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

  close(): void {
    this.client?.close?.();
  }

  private mapDomain(raw: any): Domain {
    return {
      id: raw.id,
      userId: raw.userId,
      domain: raw.domain,
      status: raw.status,
      verificationToken: raw.verificationToken,
      verifiedAt: raw.verifiedAt ? new Date(raw.verifiedAt) : undefined,
      sslStatus: raw.sslStatus,
      createdAt: new Date(raw.createdAt),
      updatedAt: new Date(raw.updatedAt),
    };
  }
}
