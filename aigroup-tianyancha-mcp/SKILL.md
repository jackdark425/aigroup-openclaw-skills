---
name: aigroup-tianyancha-mcp
description: Use `aigroup-tianyancha-mcp` for China company registration, legal-risk, and business-risk lookups through Tianyancha. Trigger when the user needs enterprise registration details, legal disputes, risk events, or a fast工商+风险核验 pass.
homepage: https://github.com/jackdark425/aigroup-openclaw-skills
---

# Tianyancha MCP

Use `aigroup-tianyancha-mcp` for China enterprise verification and risk screening.

## Route

1. Start with the exact company name whenever possible.
2. Use `companyBaseInfo` first to confirm entity identity:
   - legal representative
   - registered capital
   - establishment date
   - operating status
   - unified social credit code or equivalent registration identifiers
3. Use `risk` when the task is about:
   - judicial disputes
   - operating abnormalities
   - enforcement or penalty signals
   - general adverse-risk checks before outreach or onboarding
4. Summarize what the result means for customer acquisition:
   - whether the company is active and reachable
   - whether there are obvious red flags
   - whether follow-up should continue, pause, or escalate

## Common Jobs

- Verify a Chinese company's registration before first outreach.
- Run a quick risk screen before adding a company to a lead list.
- Cross-check web-discovered company names against authoritative registration data.
- Add legal-risk context to a banker briefing or client-screening workflow.

## Dependency

- Server name: `Tianyancha`
- Expected transport: `streamable-http`
- Required environment variable: `TIANYANCHA_AUTHORIZATION`
