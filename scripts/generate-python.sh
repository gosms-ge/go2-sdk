#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Use venv if available
if [ -d "$ROOT_DIR/python/.venv" ]; then
    source "$ROOT_DIR/python/.venv/bin/activate"
fi

echo "Generating Python protobuf code..."

# Create output directories
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/integrations/v1"
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/links/v1"
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/analytics/v1"
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/domains/v1"
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/qr/v1"
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/campaigns/v1"

# Generate Python code for all services
for service in integrations links analytics domains qr campaigns; do
    echo "Generating $service..."
    python3 -m grpc_tools.protoc \
        --proto_path="$ROOT_DIR/proto" \
        --python_out="$ROOT_DIR/python/go2_sdk/gen" \
        --grpc_python_out="$ROOT_DIR/python/go2_sdk/gen" \
        --pyi_out="$ROOT_DIR/python/go2_sdk/gen" \
        "$ROOT_DIR/proto/$service/v1/$service.proto"

    # Fix imports in generated files
    sed -i '' "s/from ${service}.v1/from go2_sdk.gen.${service}.v1/g" \
        "$ROOT_DIR/python/go2_sdk/gen/$service/v1/"*.py 2>/dev/null || true

    # Create __init__.py files
    touch "$ROOT_DIR/python/go2_sdk/gen/$service/__init__.py"
    touch "$ROOT_DIR/python/go2_sdk/gen/$service/v1/__init__.py"
done

echo "Python protobuf generation complete!"
