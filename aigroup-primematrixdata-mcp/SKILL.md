---
name: aigroup-primematrixdata-mcp
description: Use `aigroup-primematrixdata-mcp` for China enterprise intelligence through PrimeMatrixData. Route company-name resolution, basic profiles, judicial and operating risk, IP, shareholder, honors, statistics, listed-company, finance, and hiring-data requests here.
homepage: https://github.com/jackdark425/aigroup-openclaw-skills
---

# PrimeMatrixData MCP

Use `aigroup-primematrixdata-mcp` for structured China company-intelligence collection.

## Route

1. Resolve the exact company first with `company_name` if there is any ambiguity.
2. Pull only the narrowest datasets needed:
   - `basic_info` for company profile
   - `judicial_info` and `risk_info` for risk signals
   - `shareholder_info` for ownership context
   - `ip_info`, `honor_info`, and `statistic_info` for differentiation signals
   - `stk_company_basic_info` and `finance_info` for public-company context
   - `job_info` for hiring and expansion clues
3. Use PrimeMatrixData when the output needs to be lead-oriented:
   - screen whether a company is worth contacting
   - infer growth, financing, hiring, or expansion signals
   - create a structured company snapshot before outreach
4. Summarize the result into banker action language:
   - why this account matters now
   - what product angle might fit
   - what risks need a second look

## Common Jobs

- Confirm and normalize a Chinese company name before research.
- Build a compact company snapshot for prospecting.
- Detect hiring, financing, shareholder, and reputation signals.
- Support due diligence, banker briefing, and lead prioritization workflows.

## References

- Read [capabilities.md](./references/capabilities.md) for the exposed PrimeMatrixData tool groups and suggested routing.
