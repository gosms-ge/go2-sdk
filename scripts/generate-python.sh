#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Generating Python protobuf code..."

# Create output directory
mkdir -p "$ROOT_DIR/python/go2_sdk/gen/integrations/v1"

# Generate Python code
python -m grpc_tools.protoc \
    --proto_path="$ROOT_DIR/proto" \
    --python_out="$ROOT_DIR/python/go2_sdk/gen" \
    --grpc_python_out="$ROOT_DIR/python/go2_sdk/gen" \
    --pyi_out="$ROOT_DIR/python/go2_sdk/gen" \
    "$ROOT_DIR/proto/integrations/v1/integrations.proto"

# Fix imports in generated files
sed -i '' 's/from integrations.v1/from go2_sdk.gen.integrations.v1/g' \
    "$ROOT_DIR/python/go2_sdk/gen/integrations/v1/"*.py 2>/dev/null || true

echo "Python protobuf generation complete!"
