#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Generating Go protobuf code..."

# Create output directory
mkdir -p "$ROOT_DIR/go/gen/integrations/v1"

# Generate Go code
protoc \
    --proto_path="$ROOT_DIR/proto" \
    --go_out="$ROOT_DIR/go" \
    --go_opt=paths=source_relative \
    --go-grpc_out="$ROOT_DIR/go" \
    --go-grpc_opt=paths=source_relative \
    "$ROOT_DIR/proto/integrations/v1/integrations.proto"

echo "Go protobuf generation complete!"
