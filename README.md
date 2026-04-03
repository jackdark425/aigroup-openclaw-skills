# aigroup-openclaw-skills

OpenClaw/ClawHub skill wrappers for these MCP servers maintained by `jackdark425`:

- `aigroup-fmp-mcp`
- `aigroup-finnhub-mcp`
- `aigroup-market-mcp`
- `aigroup-mdtoword-mcp`
- `aigroup-tianyancha-mcp`
- `aigroup-primematrixdata-mcp`

Each skill folder contains:

- `SKILL.md` for trigger and workflow guidance
- `agents/openai.yaml` for OpenClaw/ClawHub UI metadata
- `references/capabilities.md` for the MCP capability map
- `assets/logo.svg` for ClawHub/OpenClaw visual branding

Published display names use the `AIGroup` prefix to avoid implying official affiliation with upstream data providers.

## Publish

Log in to ClawHub, then publish all four skills:

```bash
cd aigroup-openclaw-skills
npx -y clawhub login
./publish-all.sh 0.1.0
```

## GitHub Actions

Set the repository secret `CLAWHUB_TOKEN`, then publish either by:

- running the `Publish ClawHub Skills` workflow with a semver input
- pushing a tag like `v0.1.1`

The workflow uses `scripts/publish_via_api.sh` so it does not depend on local `clawhub` CLI state.
