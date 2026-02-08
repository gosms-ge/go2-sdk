package go2

// clientConfig holds the client configuration.
type clientConfig struct {
	endpoint string
	apiKey   string
	insecure bool
}

// Option configures the client.
type Option func(*clientConfig)

// WithEndpoint sets a custom gRPC endpoint.
// Default: grpc.go2.ge:443
func WithEndpoint(endpoint string) Option {
	return func(c *clientConfig) {
		c.endpoint = endpoint
	}
}

// WithAPIKey sets the API key for authentication.
// Required.
func WithAPIKey(apiKey string) Option {
	return func(c *clientConfig) {
		c.apiKey = apiKey
	}
}

// WithInsecure disables TLS.
// Use only for local development.
func WithInsecure() Option {
	return func(c *clientConfig) {
		c.insecure = true
	}
}
