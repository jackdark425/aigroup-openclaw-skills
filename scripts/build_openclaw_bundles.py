#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
BUNDLES = ROOT / "bundles"
SUPPORTED_BUNDLES = ("lead-discovery",)
BUNDLE_PREFIX = "aigroup"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_optional_dir(src: Path, dest: Path) -> bool:
    if not src.exists():
        return False
    shutil.copytree(src, dest)
    return True


def render_manifest(pack_name: str, metadata: dict, has_mcp: bool) -> dict:
    manifest: dict[str, object] = {
        "name": f"{BUNDLE_PREFIX}-{pack_name}-openclaw",
        "description": metadata.get("description") or f"{pack_name} OpenClaw bundle",
        "version": metadata.get("version") or "0.1.0",
        "skills": "skills"
    }
    if has_mcp:
        manifest["mcpServers"] = ".mcp.json"
    return manifest


def render_readme(bundle_name: str, metadata: dict, has_mcp: bool) -> str:
    lines = [
        f"# {bundle_name}",
        "",
        metadata.get("description") or f"OpenClaw bundle for {bundle_name}.",
        "",
        "This bundle packages banker lead-discovery SOP skills together with enterprise-intelligence MCP connectors for OpenClaw.",
        "",
        "## Included",
        "",
        "- `skills/`: banker lead-discovery SOP skills"
    ]
    if has_mcp:
        lines.append("- `.mcp.json`: connector template for Tianyancha and PrimeMatrixData")
    lines.extend(
        [
            "",
            "## Install",
            "",
            "Install the bundle directory with `openclaw plugins install <path>` or copy the `skills/` directory into `~/.openclaw/workspace/skills/` for workspace use.",
            "",
            "## Environment",
            "",
            "- `PRIMEMATRIX_MCP_API_KEY`",
            "- `PRIMEMATRIX_BASE_URL`",
            "- `TIANYANCHA_MCP_URL`",
            "- `TIANYANCHA_AUTHORIZATION`",
            "",
        ]
    )
    return "\n".join(lines)


def build_bundle(pack_name: str) -> Path:
    pack_dir = PACKS / pack_name
    metadata = load_json(pack_dir / "metadata.json")
    bundle_dir = BUNDLES / f"{BUNDLE_PREFIX}-{pack_name}-openclaw"

    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True)
    (bundle_dir / ".claude-plugin").mkdir()

    copy_optional_dir(pack_dir / "skills", bundle_dir / "skills")
    copy_optional_dir(pack_dir / "scripts", bundle_dir / "scripts")

    mcp_file = pack_dir / "connectors" / ".mcp.json"
    mcp_payload = load_json(mcp_file) if mcp_file.exists() else {"mcpServers": {}}
    has_mcp = bool(mcp_payload.get("mcpServers"))
    if has_mcp:
        (bundle_dir / ".mcp.json").write_text(
            json.dumps(mcp_payload, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )

    manifest = render_manifest(pack_name, metadata, has_mcp=has_mcp)
    (bundle_dir / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    (bundle_dir / "README.md").write_text(
        render_readme(f"{BUNDLE_PREFIX}-{pack_name}-openclaw", metadata, has_mcp=has_mcp) + "\n",
        encoding="utf-8",
    )
    return bundle_dir


def main() -> None:
    BUNDLES.mkdir(parents=True, exist_ok=True)
    for pack_name in SUPPORTED_BUNDLES:
        print(build_bundle(pack_name))


if __name__ == "__main__":
    main()
