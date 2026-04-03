# PrimeMatrixData MCP Capabilities

## Exposed operations in this workspace

- `company_name`
- `basic_info`
- `judicial_info`
- `risk_info`
- `ip_info`
- `shareholder_info`
- `honor_info`
- `statistic_info`
- `stk_company_basic_info`
- `finance_info`
- `job_info`

## Task mapping

- Entity resolution:
  - `company_name`
- Company snapshot:
  - `basic_info`, `statistic_info`, `shareholder_info`
- Risk screen:
  - `judicial_info`, `risk_info`
- Quality and momentum signals:
  - `ip_info`, `honor_info`, `job_info`
- Listed-company overlay:
  - `stk_company_basic_info`, `finance_info`

## Dependency

- MCP server name: `PrimeMatrixData-stdio`
- Local launch pattern in this workspace: `npx prime-matrix-data`
- Required environment variable in this workspace: `PRIMEMATRIX_MCP_API_KEY`
