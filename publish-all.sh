#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION="${1:-0.1.0}"
TAGS="${CLAWHUB_TAGS:-latest}"

publish_skill() {
  local slug="$1"
  local name="$2"

  echo "Publishing ${slug} (${VERSION})"
  npx -y clawhub publish "${ROOT_DIR}/${slug}" \
    --slug "${slug}" \
    --name "${name}" \
    --version "${VERSION}" \
    --tags "${TAGS}"
}

publish_skill "aigroup-fmp-mcp" "FMP MCP"
publish_skill "aigroup-finnhub-mcp" "Finnhub MCP"
publish_skill "aigroup-market-mcp" "Market MCP"
publish_skill "aigroup-mdtoword-mcp" "Markdown to Word MCP"
