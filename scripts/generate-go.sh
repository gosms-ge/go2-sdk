#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Generating Go protobuf code..."

# Create output directories
mkdir -p "$ROOT_DIR/go/integrations/v1"
mkdir -p "$ROOT_DIR/go/links/v1"
mkdir -p "$ROOT_DIR/go/analytics/v1"
mkdir -p "$ROOT_DIR/go/domains/v1"
mkdir -p "$ROOT_DIR/go/qr/v1"

# Generate Go code for all services
for service in integrations links analytics domains qr; do
    echo "Generating $service..."
    protoc \
        --proto_path="$ROOT_DIR/proto" \
        --go_out="$ROOT_DIR/go" \
        --go_opt=paths=source_relative \
        --go-grpc_out="$ROOT_DIR/go" \
        --go-grpc_opt=paths=source_relative \
        "$ROOT_DIR/proto/$service/v1/$service.proto"
done

echo "Go protobuf generation complete!"
