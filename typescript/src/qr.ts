import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';
import { wrapError } from './errors';

const PROTO_PATH = path.join(__dirname, '../proto/qr/v1/qr.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: false,
  longs: String,
  enums: Number,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const QRServiceClient = protoDescriptor.qr.v1.QRService;

export interface GenerateQRParams {
  linkId: string;
  size?: number; // 128, 256, 512, 1024
  format?: 'png' | 'svg';
  foregroundColor?: string; // hex color
  backgroundColor?: string; // hex color
  logoUrl?: string;
}

export interface QRCode {
  url: string;
  size: number;
  format: string;
}

/**
 * Service for QR code generation.
 */
export class QRService {
  private client: any;

  constructor(
    endpoint: string,
    credentials: grpc.ChannelCredentials,
    options: grpc.ClientOptions
  ) {
    this.client = new QRServiceClient(endpoint, credentials, options);
  }

  /**
   * Generate a QR code for a link.
   */
  async generate(params: GenerateQRParams): Promise<QRCode> {
    return new Promise((resolve, reject) => {
      this.client.generateQR(
        {
          linkId: params.linkId,
          size: params.size || 256,
          format: params.format || 'png',
          foregroundColor: params.foregroundColor || '#000000',
          backgroundColor: params.backgroundColor || '#FFFFFF',
          logoUrl: params.logoUrl || '',
        },
        (err: grpc.ServiceError | null, response: any) => {
          if (err) {
            reject(wrapError(err));
          } else {
            resolve({
              url: response?.url || '',
              size: response?.size || 256,
              format: response?.format || 'png',
            });
          }
        }
      );
    });
  }

  close(): void {
    this.client?.close?.();
  }
}
