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
//	// Create a smart link
//	link, err := client.Links.Create(ctx, &linksv1.CreateLinkRequest{
//	    Slug: "myapp",
//	    Title: "My App",
//	    IosUrl: "https://apps.apple.com/...",
//	    AndroidUrl: "https://play.google.com/...",
//	})
//
//	// Get analytics
//	stats, err := client.Analytics.GetStats(ctx, link.Id, "7d")
//
//	// Generate QR code
//	qr, err := client.QR.Generate(ctx, link.Id, 256, "png")
package go2

import (
	"context"
	"crypto/tls"
	"fmt"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"

	analyticsv1 "github.com/gosms-ge/go2-sdk/go/analytics/v1"
	campaignsv1 "github.com/gosms-ge/go2-sdk/go/campaigns/v1"
	domainsv1 "github.com/gosms-ge/go2-sdk/go/domains/v1"
	integrationsv1 "github.com/gosms-ge/go2-sdk/go/integrations/v1"
	linksv1 "github.com/gosms-ge/go2-sdk/go/links/v1"
	qrv1 "github.com/gosms-ge/go2-sdk/go/qr/v1"
)

const (
	// DefaultEndpoint is the default gRPC endpoint for the Go2 API.
	DefaultEndpoint = "grpc.go2.ge:443"
)

// Client is the Go2 API client.
type Client struct {
	conn *grpc.ClientConn

	// Links provides access to the LinkService for managing smart links.
	Links *LinksClient

	// Analytics provides access to the AnalyticsService for link statistics.
	Analytics *AnalyticsClient

	// Integrations provides access to the IntegrationService.
	Integrations *IntegrationsClient

	// Domains provides access to the DomainService for custom domains.
	Domains *DomainsClient

	// QR provides access to the QRService for QR code generation.
	QR *QRClient

	// Campaigns provides access to the CampaignService for marketing campaigns.
	Campaigns *CampaignsClient
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
		Links:        newLinksClient(linksv1.NewLinkServiceClient(conn)),
		Analytics:    newAnalyticsClient(analyticsv1.NewAnalyticsServiceClient(conn)),
		Integrations: newIntegrationsClient(integrationsv1.NewIntegrationServiceClient(conn)),
		Domains:      newDomainsClient(domainsv1.NewDomainServiceClient(conn)),
		QR:           newQRClient(qrv1.NewQRServiceClient(conn)),
		Campaigns:    newCampaignsClient(campaignsv1.NewCampaignServiceClient(conn)),
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

// LinksClient provides methods for managing smart links.
type LinksClient struct {
	client linksv1.LinkServiceClient
}

func newLinksClient(client linksv1.LinkServiceClient) *LinksClient {
	return &LinksClient{client: client}
}

// List returns all links for the authenticated user.
func (c *LinksClient) List(ctx context.Context) ([]*linksv1.Link, error) {
	resp, err := c.client.ListLinks(ctx, &linksv1.ListLinksRequest{})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetLinks(), nil
}

// Create creates a new smart link.
func (c *LinksClient) Create(ctx context.Context, req *linksv1.CreateLinkRequest) (*linksv1.Link, error) {
	resp, err := c.client.CreateLink(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Get returns a link by ID.
func (c *LinksClient) Get(ctx context.Context, id string) (*linksv1.Link, error) {
	resp, err := c.client.GetLink(ctx, &linksv1.GetLinkRequest{Id: id})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Update updates a link.
func (c *LinksClient) Update(ctx context.Context, req *linksv1.UpdateLinkRequest) (*linksv1.Link, error) {
	resp, err := c.client.UpdateLink(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Delete deletes a link.
func (c *LinksClient) Delete(ctx context.Context, id string) error {
	_, err := c.client.DeleteLink(ctx, &linksv1.DeleteLinkRequest{Id: id})
	if err != nil {
		return wrapError(err)
	}
	return nil
}

// CheckSlug checks if a slug is available.
func (c *LinksClient) CheckSlug(ctx context.Context, slug string) (bool, error) {
	resp, err := c.client.CheckSlug(ctx, &linksv1.CheckSlugRequest{Slug: slug})
	if err != nil {
		return false, wrapError(err)
	}
	return resp.GetAvailable(), nil
}

// AnalyticsClient provides methods for link analytics.
type AnalyticsClient struct {
	client analyticsv1.AnalyticsServiceClient
}

func newAnalyticsClient(client analyticsv1.AnalyticsServiceClient) *AnalyticsClient {
	return &AnalyticsClient{client: client}
}

// GetStats returns overview statistics for a link.
func (c *AnalyticsClient) GetStats(ctx context.Context, linkID string, period string) (*analyticsv1.GetStatsResponse, error) {
	resp, err := c.client.GetStats(ctx, &analyticsv1.GetStatsRequest{LinkId: linkID, Period: period})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// GetTimeseries returns click data over time.
func (c *AnalyticsClient) GetTimeseries(ctx context.Context, linkID string, period string) ([]*analyticsv1.TimeseriesPoint, error) {
	resp, err := c.client.GetTimeseries(ctx, &analyticsv1.GetTimeseriesRequest{LinkId: linkID, Period: period})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetPoints(), nil
}

// GetPlatforms returns click breakdown by platform.
func (c *AnalyticsClient) GetPlatforms(ctx context.Context, linkID string, period string) ([]*analyticsv1.PlatformStats, error) {
	resp, err := c.client.GetPlatforms(ctx, &analyticsv1.GetPlatformsRequest{LinkId: linkID, Period: period})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetPlatforms(), nil
}

// GetCountries returns click breakdown by country.
func (c *AnalyticsClient) GetCountries(ctx context.Context, linkID string, period string, limit int32) ([]*analyticsv1.CountryStats, error) {
	resp, err := c.client.GetCountries(ctx, &analyticsv1.GetCountriesRequest{LinkId: linkID, Period: period, Limit: limit})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetCountries(), nil
}

// GetReferrers returns click breakdown by referrer.
func (c *AnalyticsClient) GetReferrers(ctx context.Context, linkID string, period string, limit int32) ([]*analyticsv1.ReferrerStats, error) {
	resp, err := c.client.GetReferrers(ctx, &analyticsv1.GetReferrersRequest{LinkId: linkID, Period: period, Limit: limit})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetReferrers(), nil
}

// DomainsClient provides methods for managing custom domains.
type DomainsClient struct {
	client domainsv1.DomainServiceClient
}

func newDomainsClient(client domainsv1.DomainServiceClient) *DomainsClient {
	return &DomainsClient{client: client}
}

// List returns all custom domains for the authenticated user.
func (c *DomainsClient) List(ctx context.Context) ([]*domainsv1.Domain, error) {
	resp, err := c.client.ListDomains(ctx, &domainsv1.ListDomainsRequest{})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp.GetDomains(), nil
}

// Create adds a new custom domain.
func (c *DomainsClient) Create(ctx context.Context, domain string) (*domainsv1.CreateDomainResponse, error) {
	resp, err := c.client.CreateDomain(ctx, &domainsv1.CreateDomainRequest{Domain: domain})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Get returns a domain by ID.
func (c *DomainsClient) Get(ctx context.Context, id string) (*domainsv1.Domain, error) {
	resp, err := c.client.GetDomain(ctx, &domainsv1.GetDomainRequest{Id: id})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Verify triggers domain verification.
func (c *DomainsClient) Verify(ctx context.Context, id string) (*domainsv1.Domain, error) {
	resp, err := c.client.VerifyDomain(ctx, &domainsv1.VerifyDomainRequest{Id: id})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Delete removes a custom domain.
func (c *DomainsClient) Delete(ctx context.Context, id string) error {
	_, err := c.client.DeleteDomain(ctx, &domainsv1.DeleteDomainRequest{Id: id})
	if err != nil {
		return wrapError(err)
	}
	return nil
}

// QRClient provides methods for QR code generation.
type QRClient struct {
	client qrv1.QRServiceClient
}

func newQRClient(client qrv1.QRServiceClient) *QRClient {
	return &QRClient{client: client}
}

// Generate creates a QR code for a link.
func (c *QRClient) Generate(ctx context.Context, req *qrv1.GenerateQRRequest) (*qrv1.GenerateQRResponse, error) {
	resp, err := c.client.GenerateQR(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// CampaignsClient provides methods for managing marketing campaigns.
type CampaignsClient struct {
	client campaignsv1.CampaignServiceClient
}

func newCampaignsClient(client campaignsv1.CampaignServiceClient) *CampaignsClient {
	return &CampaignsClient{client: client}
}

// List returns all campaigns for the authenticated user.
func (c *CampaignsClient) List(ctx context.Context, limit, offset int32, status, search string) (*campaignsv1.ListCampaignsResponse, error) {
	resp, err := c.client.ListCampaigns(ctx, &campaignsv1.ListCampaignsRequest{
		Limit:  limit,
		Offset: offset,
		Status: status,
		Search: search,
	})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Create creates a new campaign.
func (c *CampaignsClient) Create(ctx context.Context, req *campaignsv1.CreateCampaignRequest) (*campaignsv1.Campaign, error) {
	resp, err := c.client.CreateCampaign(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Get returns a campaign by ID.
func (c *CampaignsClient) Get(ctx context.Context, id string) (*campaignsv1.Campaign, error) {
	resp, err := c.client.GetCampaign(ctx, &campaignsv1.GetCampaignRequest{Id: id})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Update updates a campaign.
func (c *CampaignsClient) Update(ctx context.Context, req *campaignsv1.UpdateCampaignRequest) (*campaignsv1.Campaign, error) {
	resp, err := c.client.UpdateCampaign(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// Delete deletes a campaign.
func (c *CampaignsClient) Delete(ctx context.Context, id string) error {
	_, err := c.client.DeleteCampaign(ctx, &campaignsv1.DeleteCampaignRequest{Id: id})
	if err != nil {
		return wrapError(err)
	}
	return nil
}

// GenerateLinks generates links for campaign recipients in bulk.
func (c *CampaignsClient) GenerateLinks(ctx context.Context, req *campaignsv1.GenerateLinksRequest) (*campaignsv1.GenerateLinksResponse, error) {
	resp, err := c.client.GenerateLinks(ctx, req)
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// ListLinks returns campaign links with pagination.
func (c *CampaignsClient) ListLinks(ctx context.Context, campaignID string, limit, offset int32, clickedOnly bool, search string) (*campaignsv1.ListCampaignLinksResponse, error) {
	resp, err := c.client.ListCampaignLinks(ctx, &campaignsv1.ListCampaignLinksRequest{
		CampaignId:  campaignID,
		Limit:       limit,
		Offset:      offset,
		ClickedOnly: clickedOnly,
		Search:      search,
	})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// GetStats returns campaign statistics.
func (c *CampaignsClient) GetStats(ctx context.Context, campaignID string) (*campaignsv1.CampaignStats, error) {
	resp, err := c.client.GetCampaignStats(ctx, &campaignsv1.GetCampaignStatsRequest{CampaignId: campaignID})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}

// ExportLinks exports all campaign links.
func (c *CampaignsClient) ExportLinks(ctx context.Context, campaignID string) (*campaignsv1.ExportLinksResponse, error) {
	resp, err := c.client.ExportLinks(ctx, &campaignsv1.ExportLinksRequest{CampaignId: campaignID, Format: "json"})
	if err != nil {
		return nil, wrapError(err)
	}
	return resp, nil
}
