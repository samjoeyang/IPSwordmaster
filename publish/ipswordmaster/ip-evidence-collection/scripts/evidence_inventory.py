#!/usr/bin/env python3
"""生成知识产权维权证据清单（Markdown）。

用法:
    python3 evidence_inventory.py <evidence.json> [--out evidence-list.md]

输入 JSON 结构（列表）:
[
  {
    "id": "E001",
    "date": "2026-10-18",
    "type": "侵权证据|权利证据|损害证据",
    "method": "公证|时间戳|区块链|自行取证|诉前保全|购买凭证",
    "source": "URL/文件路径/卷宗号/存证编号",
    "holder": "保存人/位置",
    "purpose": "证明目的",
    "status": "已固定|待补|已提交"
  }
]
"""
import json
import sys
import argparse

REQUIRED = ["id", "date", "type", "method", "source", "holder", "purpose", "status"]
TYPES = ("侵权证据", "权利证据", "损害证据")


def main() -> int:
    ap = argparse.ArgumentParser(description="生成证据清单 Markdown")
    ap.add_argument("input", help="证据 JSON 文件")
    ap.add_argument("--out", default="evidence-list.md", help="输出 Markdown 路径")
    args = ap.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            items = json.load(f)
    except Exception as e:
        print(f"[错误] 读取 JSON 失败: {e}", file=sys.stderr)
        return 1

    if not isinstance(items, list):
        print("[错误] JSON 顶层必须是数组", file=sys.stderr)
        return 1

    errors = []
    for i, it in enumerate(items):
        for k in REQUIRED:
            if k not in it or str(it[k]).strip() == "":
                errors.append(f"第 {i + 1} 条缺少必填字段: {k}")
        if it.get("type") not in TYPES:
            errors.append(f"第 {i + 1} 条 type 非法: {it.get('type')}（应为 {TYPES} 之一）")

    if errors:
        print("[校验失败]", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    lines = ["# 证据清单", "", f"生成时间：{args.input}", "", "| 编号 | 日期 | 类型 | 取证方式 | 来源 | 保存人/位置 | 证明目的 | 状态 |",
             "|---|---|---|---|---|---|---|---|"]
    for it in items:
        lines.append(f"| {it['id']} | {it['date']} | {it['type']} | {it['method']} | {it['source']} | {it['holder']} | {it['purpose']} | {it['status']} |")

    lines.append("")
    lines.append(f"共 {len(items)} 项证据。")
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[完成] 证据清单已生成: {args.out}（{len(items)} 项）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
