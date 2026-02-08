#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Generating TypeScript protobuf code..."

# Create output directory
mkdir -p "$ROOT_DIR/typescript/src/gen/integrations/v1"

# Generate TypeScript code using grpc-tools
cd "$ROOT_DIR/typescript"

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    npm install
fi

# Generate using grpc_tools_node_protoc
npx grpc_tools_node_protoc \
    --proto_path="$ROOT_DIR/proto" \
    --js_out=import_style=commonjs,binary:"$ROOT_DIR/typescript/src/gen" \
    --grpc_out=grpc_js:"$ROOT_DIR/typescript/src/gen" \
    --ts_out=grpc_js:"$ROOT_DIR/typescript/src/gen" \
    "$ROOT_DIR/proto/integrations/v1/integrations.proto"

echo "TypeScript protobuf generation complete!"
