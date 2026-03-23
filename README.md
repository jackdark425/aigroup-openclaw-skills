# aigroup-openclaw-skills

OpenClaw/ClawHub skill wrappers for these MCP servers maintained by `jackdark425`:

- `aigroup-fmp-mcp`
- `aigroup-finnhub-mcp`
- `aigroup-market-mcp`
- `aigroup-mdtoword-mcp`

Each skill folder contains:

- `SKILL.md` for trigger and workflow guidance
- `agents/openai.yaml` for OpenClaw/ClawHub UI metadata
- `references/capabilities.md` for the MCP capability map

Published display names use the `AIGroup` prefix to avoid implying official affiliation with upstream data providers.

## Publish

Log in to ClawHub, then publish all four skills:

```bash
cd /Users/jackdark/codex/openclaw-skills
npx -y clawhub login
./publish-all.sh 0.1.0
```
