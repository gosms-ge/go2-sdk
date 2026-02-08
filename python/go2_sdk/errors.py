"""Go2 SDK Errors."""

from typing import Any
import grpc


class Go2Error(Exception):
    """Base exception for Go2 SDK errors."""

    def __init__(self, message: str, code: grpc.StatusCode = grpc.StatusCode.UNKNOWN):
        super().__init__(message)
        self.code = code
        self.message = message


class AuthenticationError(Go2Error):
    """Raised when authentication fails (invalid API key)."""

    def __init__(self, message: str = "Invalid or missing API key"):
        super().__init__(message, grpc.StatusCode.UNAUTHENTICATED)


class NotFoundError(Go2Error):
    """Raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, grpc.StatusCode.NOT_FOUND)


class PermissionDeniedError(Go2Error):
    """Raised when permission is denied."""

    def __init__(self, message: str = "Permission denied"):
        super().__init__(message, grpc.StatusCode.PERMISSION_DENIED)


class ValidationError(Go2Error):
    """Raised when input validation fails."""

    def __init__(self, message: str = "Invalid input"):
        super().__init__(message, grpc.StatusCode.INVALID_ARGUMENT)


class RateLimitError(Go2Error):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str = "Rate limit exceeded"):
        super().__init__(message, grpc.StatusCode.RESOURCE_EXHAUSTED)


def wrap_error(error: Any) -> Go2Error:
    """Convert a gRPC error to a Go2 SDK error."""
    if not isinstance(error, grpc.RpcError):
        return Go2Error(str(error))

    code = error.code()
    message = error.details() or str(error)

    if code == grpc.StatusCode.UNAUTHENTICATED:
        return AuthenticationError(message)
    elif code == grpc.StatusCode.NOT_FOUND:
        return NotFoundError(message)
    elif code == grpc.StatusCode.PERMISSION_DENIED:
        return PermissionDeniedError(message)
    elif code == grpc.StatusCode.INVALID_ARGUMENT:
        return ValidationError(message)
    elif code == grpc.StatusCode.RESOURCE_EXHAUSTED:
        return RateLimitError(message)
    else:
        return Go2Error(message, code)
