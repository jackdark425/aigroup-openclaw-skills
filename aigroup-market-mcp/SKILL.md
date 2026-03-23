---
name: aigroup-market-mcp
description: Use the `aigroup-market-mcp` server for China-market and Tushare-oriented workflows including A-share data, index data, sector and macro snapshots, fund flows, basic company information, convertible bonds, margin trading, block trades, and 7x24 finance news. Trigger when the task is centered on mainland China market structure, local market breadth, capital flow, or China-specific securities datasets.
homepage: https://github.com/jackdark425/aigroup-market-mcp
---

# Market MCP

Route China-market data requests to `aigroup-market-mcp`.

## Route

1. Decide which market lens the user actually needs:
   - single stock
   - sector or index
   - market flow
   - macro or news
   - fund or bond data
2. Match the request to the dedicated operation:
   - `stock_data`, `stock_data_minutes`, `basic_info`, `company_performance`
   - `index_data`, `csi_index_constituents`
   - `money_flow`, `margin_trade`, `block_trade`, `dragon_tiger_inst`
   - `fund_data`, `fund_manager_by_name`
   - `convertible_bond`
   - `macro_econ`, `finance_news`, `hot_news_7x24`
3. Keep the reply localized. Name the exchange, index family, or China-market convention when relevant.
4. If the user mixes China and global assets, use this skill for the China leg and another market skill for the non-China leg.

## Common Jobs

- Pull A-share or Hong Kong or US company performance where exposed by the server.
- Explain what a CSI index contains or how an index moved.
- Check northbound-style or general market flow proxies such as money flow, margin, block trade, or dragon-tiger activity.
- Gather macro and 7x24 finance headlines for a China-market briefing.
- Retrieve fund, fund-manager, or convertible-bond context.

## References

- Read [capabilities.md](./references/capabilities.md) for the currently allowed operations and routing hints.
