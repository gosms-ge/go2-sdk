// Package go2 provides a Go SDK for the Go2 gRPC API.
//
// Example usage:
//
//	client, err := go2.NewClient(go2.WithAPIKey("go2_your_key"))
//	if err != nil {
//	    log.Fatal(err)
//	}
//	defer client.Close()
//
//	integrations, err := client.Integrations.List(ctx)
package go2

import (
	"context"
	"crypto/tls"
	"fmt"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"

	integrationsv1 "github.com/gosms-ge/go2-sdk/go/integrations/v1"
)

const (
	// DefaultEndpoint is the default gRPC endpoint for the Go2 API.
	DefaultEndpoint = "grpc.go2.ge:443"
)

// Client is the Go2 API client.
type Client struct {
	conn *grpc.ClientConn

	// Integrations provides access to the IntegrationService.
	Integrations *IntegrationsClient
}

// NewClient creates a new Go2 API client with the given options.
func NewClient(opts ...Option) (*Client, error) {
	cfg := &clientConfig{
		endpoint: DefaultEndpoint,
	}

	for _, opt := range opts {
		opt(cfg)
	}

	if cfg.apiKey == "" {
		return nil, fmt.Errorf("go2: API key is required")
	}

	// Build dial options
	var dialOpts []grpc.DialOption

	// TLS configuration
	if cfg.insecure {
		dialOpts = append(dialOpts, grpc.WithTransportCredentials(insecure.NewCredentials()))
	} else {
		creds := credentials.NewTLS(&tls.Config{
			MinVersion: tls.VersionTLS12,
		})
		dialOpts = append(dialOpts, grpc.WithTransportCredentials(creds))
	}

	// Add auth interceptor
	dialOpts = append(dialOpts, grpc.WithUnaryInterceptor(authInterceptor(cfg.apiKey)))

	// Connect
	conn, err := grpc.NewClient(cfg.endpoint, dialOpts...)
	if err != nil {
		return nil, fmt.Errorf("go2: failed to connect: %w", err)
	}

	return &Client{
		conn:         conn,
		Integrations: newIntegrationsClient(integrationsv1.NewIntegrationServiceClient(conn)),
	}, nil
}

// Close closes the client connection.
func (c *Client) Close() error {
	return c.conn.Close()
}

// IntegrationsClient provides methods for managing integrations.
type IntegrationsClient struct {
	client integrationsv1.IntegrationServiceClient
}

func newIntegrationsClient(client integrationsv1.IntegrationServiceClient) *IntegrationsClient {
	return &IntegrationsClient{client: client}
}

// List returns all integrations for the authenticated user.
func (c *IntegrationsClient) List(ctx context.Context) ([]*integrationsv1.Integration, error) {
	resp, err := c.client.ListIntegrations(ctx, &integrationsv1.ListIntegrationsRequest{})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetIntegrations(), nil
}

// Create creates a new integration.
func (c *IntegrationsClient) Create(ctx context.Context, req *integrationsv1.CreateIntegrationRequest) (*integrationsv1.Integration, error) {
	resp, err := c.client.CreateIntegration(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Get returns an integration by ID.
func (c *IntegrationsClient) Get(ctx context.Context, id string) (*integrationsv1.Integration, error) {
	resp, err := c.client.GetIntegration(ctx, &integrationsv1.GetIntegrationRequest{Id: id})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Update updates an integration.
func (c *IntegrationsClient) Update(ctx context.Context, req *integrationsv1.UpdateIntegrationRequest) (*integrationsv1.Integration, error) {
	resp, err := c.client.UpdateIntegration(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Delete deletes an integration.
func (c *IntegrationsClient) Delete(ctx context.Context, id string) error {
	_, err := c.client.DeleteIntegration(ctx, &integrationsv1.DeleteIntegrationRequest{Id: id})
	if err != nil {
		return wrapError(err)
	}
	return nil
}

// Test sends a test notification to an integration.
func (c *IntegrationsClient) Test(ctx context.Context, id string) (*integrationsv1.TestIntegrationResponse, error) {
	resp, err := c.client.TestIntegration(ctx, &integrationsv1.TestIntegrationRequest{Id: id})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// GetTypes returns all available integration types and events.
func (c *IntegrationsClient) GetTypes(ctx context.Context) (*integrationsv1.GetIntegrationTypesResponse, error) {
	resp, err := c.client.GetIntegrationTypes(ctx, &integrationsv1.GetIntegrationTypesRequest{})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}
