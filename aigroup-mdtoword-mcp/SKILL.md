---
name: aigroup-mdtoword-mcp
description: Use the `aigroup-mdtoword-mcp` server to convert Markdown into polished Word documents with `.docx` output, advanced styling, tables, formulas, page layout, headers and footers, and template-like resources. Trigger when the user wants a report, memo, brief, proposal, or other Markdown-authored content delivered as a professional Word file.
---

# Markdown to Word MCP

Use this skill when the user wants Word output and the source content is already in Markdown or can be drafted in Markdown first.

## Quick Start

1. Confirm the deliverable:
   - existing Markdown file to convert
   - Markdown content generated in the session
   - tabular data that should become Markdown before conversion
2. Choose the right operation:
   - `markdown_to_docx` for primary conversion
   - `table_data_to_markdown` when the raw input is structured table data
3. Ask or infer the output style only when it matters:
   - technical memo
   - business report
   - academic-style document
   - minimal document
4. If formulas, tables, headers, footers, or local images are important, mention that explicitly before conversion.
5. Return the path to the generated `.docx` and summarize any formatting assumptions.

## Best-Fit Tasks

- Convert a finished Markdown note, report, or memo into `.docx`.
- Produce a polished Word deliverable from generated Markdown in the same run.
- Preserve formulas, structured tables, and page furniture such as headers or page numbers.
- Turn extracted or CSV-like table data into Markdown and then into Word.

## Working Style

- Draft in Markdown first if the content still needs editing; convert only once the structure is stable.
- Keep formatting assumptions explicit when the user cares about template feel or document class.
- Prefer local-file workflows when the user already has a Markdown source.
- If the output is intended for clients or leadership, mention any inferred style choice.

## References

- Read [capabilities.md](./references/capabilities.md) for the server features and delivery checklist.
