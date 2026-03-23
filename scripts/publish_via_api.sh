#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="${1:-}"
CHANGELOG="${CHANGELOG:-Initial ClawHub release}"
TAGS="${CLAWHUB_TAGS:-latest}"

if [[ -z "${VERSION}" ]]; then
  echo "Usage: $0 <version>" >&2
  exit 1
fi

if [[ -z "${CLAWHUB_TOKEN:-}" ]]; then
  echo "CLAWHUB_TOKEN is required" >&2
  exit 1
fi

publish_skill() {
  local slug="$1"
  local display_name="$2"
  local dir="${ROOT_DIR}/${slug}"

  echo "Publishing ${slug}@${VERSION}"
  curl -fsS \
    -H "Authorization: Bearer ${CLAWHUB_TOKEN}" \
    -F "payload={\"slug\":\"${slug}\",\"displayName\":\"${display_name}\",\"version\":\"${VERSION}\",\"changelog\":\"${CHANGELOG}\",\"acceptLicenseTerms\":true,\"tags\":[\"${TAGS}\"]};type=application/json" \
    -F "files=@${dir}/SKILL.md;filename=SKILL.md;type=text/markdown" \
    -F "files=@${dir}/agents/openai.yaml;filename=agents/openai.yaml;type=text/yaml" \
    -F "files=@${dir}/references/capabilities.md;filename=references/capabilities.md;type=text/markdown" \
    -F "files=@${dir}/assets/logo.svg;filename=assets/logo.svg;type=image/svg+xml" \
    https://clawhub.ai/api/v1/skills
  echo
}

publish_skill "aigroup-fmp-mcp" "AIGroup FMP MCP"
publish_skill "aigroup-finnhub-mcp" "AIGroup Finnhub MCP"
publish_skill "aigroup-market-mcp" "AIGroup Market MCP"
publish_skill "aigroup-mdtoword-mcp" "AIGroup Markdown to Word MCP"
