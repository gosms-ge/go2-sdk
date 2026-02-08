#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Generating all SDK protobuf code ==="

echo ""
echo "--- Go ---"
"$SCRIPT_DIR/generate-go.sh"

echo ""
echo "--- Python ---"
"$SCRIPT_DIR/generate-python.sh"

echo ""
echo "--- TypeScript ---"
"$SCRIPT_DIR/generate-typescript.sh"

echo ""
echo "=== All protobuf generation complete! ==="
