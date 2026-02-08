import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';
import { wrapError } from './errors';

const PROTO_PATH = path.join(__dirname, '../proto/analytics/v1/analytics.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: false,
  longs: String,
  enums: Number,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const AnalyticsServiceClient = protoDescriptor.analytics.v1.AnalyticsService;

export interface Stats {
  totalClicks: number;
  uniqueClicks: number;
  iosClicks: number;
  androidClicks: number;
  webClicks: number;
  otherClicks: number;
  topCountries: CountryStats[];
  topReferrers: ReferrerStats[];
}

export interface TimeseriesPoint {
  date: string;
  clicks: number;
  uniqueClicks: number;
}

export interface PlatformStats {
  platform: string;
  clicks: number;
  percentage: number;
}

export interface CountryStats {
  countryCode: string;
  countryName: string;
  clicks: number;
  percentage: number;
}

export interface ReferrerStats {
  referrer: string;
  clicks: number;
  percentage: number;
}

/**
 * Service for link analytics.
 */
export class AnalyticsService {
  private client: any;

  constructor(
    endpoint: string,
    credentials: grpc.ChannelCredentials,
    options: grpc.ClientOptions
  ) {
    this.client = new AnalyticsServiceClient(endpoint, credentials, options);
  }

  /**
   * Get overview statistics for a link.
   */
  async getStats(linkId: string): Promise<Stats> {
    return new Promise((resolve, reject) => {
      this.client.getStats(
        { linkId },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              totalClicks: parseInt(response?.totalClicks) || 0,
              uniqueClicks: parseInt(response?.uniqueClicks) || 0,
              iosClicks: parseInt(response?.iosClicks) || 0,
              androidClicks: parseInt(response?.androidClicks) || 0,
              webClicks: parseInt(response?.webClicks) || 0,
              otherClicks: parseInt(response?.otherClicks) || 0,
              topCountries: response?.topCountries || [],
              topReferrers: response?.topReferrers || [],
            });
          }
        }
      );
    });
  }

  /**
   * Get click data over time.
   * @param period - "7d", "30d", or "90d"
   */
  async getTimeseries(linkId: string, period: '7d' | '30d' | '90d' = '7d'): Promise<TimeseriesPoint[]> {
    return new Promise((resolve, reject) => {
      this.client.getTimeseries(
        { linkId, period },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(
              (response?.points || []).map((p: any) => ({
                date: p.date,
                clicks: parseInt(p.clicks) || 0,
                uniqueClicks: parseInt(p.uniqueClicks) || 0,
              }))
            );
          }
        }
      );
    });
  }

  /**
   * Get breakdown by platform.
   */
  async getPlatforms(linkId: string): Promise<PlatformStats[]> {
    return new Promise((resolve, reject) => {
      this.client.getPlatforms(
        { linkId },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(
              (response?.platforms || []).map((p: any) => ({
                platform: p.platform,
                clicks: parseInt(p.clicks) || 0,
                percentage: p.percentage || 0,
              }))
            );
          }
        }
      );
    });
  }

  /**
   * Get breakdown by country.
   */
  async getCountries(linkId: string): Promise<CountryStats[]> {
    return new Promise((resolve, reject) => {
      this.client.getCountries(
        { linkId },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(
              (response?.countries || []).map((c: any) => ({
                countryCode: c.countryCode,
                countryName: c.countryName,
                clicks: parseInt(c.clicks) || 0,
                percentage: c.percentage || 0,
              }))
            );
          }
        }
      );
    });
  }

  /**
   * Get top referrers.
   */
  async getReferrers(linkId: string): Promise<ReferrerStats[]> {
    return new Promise((resolve, reject) => {
      this.client.getReferrers(
        { linkId },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve(
              (response?.referrers || []).map((r: any) => ({
                referrer: r.referrer,
                clicks: parseInt(r.clicks) || 0,
                percentage: r.percentage || 0,
              }))
            );
          }
        }
      );
    });
  }

  close(): void {
    this.client?.close?.();
  }
}
