---
name: aigroup-fmp-mcp
description: Use Financial Modeling Prep market data through the `aigroup-fmp-mcp` server for public-company research, quote checks, market breadth snapshots, sector performance, historical charts, basic technical indicators, analyst targets, and financial statement retrieval. Trigger when the task is about listed equities, company profiles, fundamentals, market movers, S&P 500 constituents, earnings calendars, or quick valuation context.
---

# FMP MCP

Use this skill when the user needs fast public-market context from Financial Modeling Prep and the `aigroup-fmp-mcp` MCP server is available.

## Quick Start

1. Confirm the company or ticker first. If the ticker is unknown or ambiguous, resolve it with `search_symbol`.
2. Pull the minimum set of facts needed for the request:
   - `get_quote` for live price context
   - `get_company_profile` for issuer overview
   - `get_income_statement`, `get_balance_sheet`, `get_cash_flow` for financials
   - `get_key_metrics` and `get_financial_ratios` for quick benchmarking
3. Add market context only if it improves the answer:
   - `get_market_gainers`, `get_market_losers`, `get_most_active`
   - `get_sector_performance`
   - `get_sp500_constituents`
4. Add estimate or technical context only when asked:
   - `get_analyst_estimates`, `get_price_target`, `get_analyst_ratings`
   - `get_technical_indicator_rsi`, `get_technical_indicator_sma`, `get_technical_indicator_ema`
5. State dates clearly for quotes, charts, and calendars.

## Best-Fit Tasks

- Research a public company with current quote, profile, and recent financial statements.
- Compare a small peer set on margins, valuation, or balance-sheet strength.
- Summarize market breadth using gainers, losers, most active names, or sector performance.
- Pull earnings or economic calendar context for a near-term event.
- Add a quick chart or RSI/SMA/EMA read to an otherwise fundamentals-led answer.

## Working Style

- Prefer FMP for quick issuer overviews and statement retrieval.
- Keep the first pass lightweight; expand only if the user wants deeper modeling or broader peer work.
- Say when a datapoint is current-market data versus trailing financial-report data.
- If symbol resolution is uncertain, say so and show the inferred ticker before using it.
- If the user asks for intraday or latest data, mention the exact date used in the response.

## References

- Read [capabilities.md](./references/capabilities.md) for the exposed tool groups and recommended task mapping.
