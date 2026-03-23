---
name: aigroup-fmp-mcp
description: Use `aigroup-fmp-mcp` for listed-equity data from Financial Modeling Prep. Route quote, profile, financial-statement, key-metric, ratio, market-mover, sector, chart, technical-indicator, analyst-target, and calendar requests here.
homepage: https://github.com/jackdark425/aigroup-fmp-mcp
---

# FMP MCP

Use `aigroup-fmp-mcp` for listed-equity quote, profile, statement, metric, and market snapshot requests.

## Route

1. Confirm the company or ticker first. If the ticker is unknown or ambiguous, resolve it with `search_symbol`.
2. Pull only the fields needed for the request:
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

## Requests

- Research a public company with current quote, profile, and recent financial statements.
- Compare a small peer set on margins, valuation, or balance-sheet strength.
- Summarize market breadth using gainers, losers, most active names, or sector performance.
- Pull earnings or economic calendar context for a near-term event.
- Add a quick chart or RSI/SMA/EMA read to an otherwise fundamentals-led answer.

## References

- Read [capabilities.md](./references/capabilities.md) for the exposed tool groups and recommended task mapping.
