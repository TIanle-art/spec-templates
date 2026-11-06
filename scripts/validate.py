"""检查 Trellis 规范模板仓库：index.json 格式、模板目录和 Markdown 相对链接。"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors: list[str] = []

index_path = root / "marketplace" / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))

if index.get("version") != 1:
    errors.append("index.json 的 version 必须是 1")

seen: set[str] = set()
for entry in index.get("templates", []):
    tid = entry.get("id", "<缺少 id>")
    for field in ("id", "type", "name", "path"):
        if not entry.get(field):
            errors.append(f"{tid}: 缺少字段 {field}")
    if entry.get("type") != "spec":
        errors.append(f"{tid}: type 必须是 spec")
    if tid in seen:
        errors.append(f"{tid}: id 重复")
    seen.add(tid)
    template_dir = root / entry.get("path", "")
    if not template_dir.is_dir():
        errors.append(f"{tid}: 目录不存在 {entry.get('path')}")
        continue
    if (template_dir / "spec").exists():
        errors.append(f"{tid}: 不要多套一层 spec/ 目录")

link_pattern = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")
for md in (root / "marketplace").rglob("*.md"):
    for target, _ in link_pattern.findall(md.read_text(encoding="utf-8")):
        if "://" in target:
            continue
        if not (md.parent / target).exists():
            errors.append(f"{md.relative_to(root)}: 链接无效 {target}")

if errors:
    print("检查未通过：")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"检查通过：{len(seen)} 个模板")
