package go2

import (
	"errors"
	"fmt"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// Common errors returned by the SDK.
var (
	ErrNotFound       = errors.New("go2: resource not found")
	ErrUnauthenticated = errors.New("go2: invalid or missing API key")
	ErrPermissionDenied = errors.New("go2: permission denied")
	ErrInvalidArgument = errors.New("go2: invalid argument")
	ErrRateLimited    = errors.New("go2: rate limit exceeded")
	ErrInternal       = errors.New("go2: internal server error")
)

// Error represents an API error with additional context.
type Error struct {
	Code    codes.Code
	Message string
	Err     error
}

func (e *Error) Error() string {
	return fmt.Sprintf("go2: %s: %s", e.Code, e.Message)
}

func (e *Error) Unwrap() error {
	return e.Err
}

// wrapError converts a gRPC error to a Go2 SDK error.
func wrapError(err error) error {
	if err == nil {
		return nil
	}

	st, ok := status.FromError(err)
	if !ok {
		return &Error{
			Code:    codes.Unknown,
			Message: err.Error(),
			Err:     err,
		}
	}

	var baseErr error
	switch st.Code() {
	case codes.NotFound:
		baseErr = ErrNotFound
	case codes.Unauthenticated:
		baseErr = ErrUnauthenticated
	case codes.PermissionDenied:
		baseErr = ErrPermissionDenied
	case codes.InvalidArgument:
		baseErr = ErrInvalidArgument
	case codes.ResourceExhausted:
		baseErr = ErrRateLimited
	case codes.Internal:
		baseErr = ErrInternal
	default:
		baseErr = err
	}

	return &Error{
		Code:    st.Code(),
		Message: st.Message(),
		Err:     baseErr,
	}
}
