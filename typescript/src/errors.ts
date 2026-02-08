import * as grpc from '@grpc/grpc-js';

/**
 * Base error class for Go2 SDK errors.
 */
export class Go2Error extends Error {
  public readonly code: grpc.status;

  constructor(message: string, code: grpc.status = grpc.status.UNKNOWN) {
    super(message);
    this.name = 'Go2Error';
    this.code = code;
  }
}

/**
 * Raised when authentication fails (invalid API key).
 */
export class AuthenticationError extends Go2Error {
  constructor(message: string = 'Invalid or missing API key') {
    super(message, grpc.status.UNAUTHENTICATED);
    this.name = 'AuthenticationError';
  }
}

/**
 * Raised when a resource is not found.
 */
export class NotFoundError extends Go2Error {
  constructor(message: string = 'Resource not found') {
    super(message, grpc.status.NOT_FOUND);
    this.name = 'NotFoundError';
  }
}

/**
 * Raised when permission is denied.
 */
export class PermissionDeniedError extends Go2Error {
  constructor(message: string = 'Permission denied') {
    super(message, grpc.status.PERMISSION_DENIED);
    this.name = 'PermissionDeniedError';
  }
}

/**
 * Raised when input validation fails.
 */
export class ValidationError extends Go2Error {
  constructor(message: string = 'Invalid input') {
    super(message, grpc.status.INVALID_ARGUMENT);
    this.name = 'ValidationError';
  }
}

/**
 * Raised when rate limit is exceeded.
 */
export class RateLimitError extends Go2Error {
  constructor(message: string = 'Rate limit exceeded') {
    super(message, grpc.status.RESOURCE_EXHAUSTED);
    this.name = 'RateLimitError';
  }
}

/**
 * Convert a gRPC error to a Go2 SDK error.
 */
export function wrapError(error: grpc.ServiceError): Go2Error {
  const message = error.details || error.message;

  switch (error.code) {
    case grpc.status.UNAUTHENTICATED:
      return new AuthenticationError(message);
    case grpc.status.NOT_FOUND:
      return new NotFoundError(message);
    case grpc.status.PERMISSION_DENIED:
      return new PermissionDeniedError(message);
    case grpc.status.INVALID_ARGUMENT:
      return new ValidationError(message);
    case grpc.status.RESOURCE_EXHAUSTED:
      return new RateLimitError(message);
    default:
      return new Go2Error(message, error.code);
  }
}
