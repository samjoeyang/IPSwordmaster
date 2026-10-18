#!/usr/bin/env python3
"""知识产权侵权损害赔偿金额计算（按法定顺序，含惩罚性赔偿与合理开支）。

用法:
    python3 damages_calculator.py --mode actual-loss|infringer-profit|license|statutory --data '<json>'

JSON 数据字段（按模式）:
- actual-loss: { "lost_sales": 0, "unit_profit": 0, "license_loss": 0 }
- infringer-profit: { "infringing_sales": 0, "unit_profit": 0, "profit_margin": 0 }  # unit_profit 或 profit_margin 二选一
- license: { "license_fee": 0, "multiple": 1 }        # 许可费合理倍数，一般 1~3 倍
- statutory: { "statutory_cap": 5000000 }             # 法定赔偿上限，默认 500 万
- 通用: { "punitive_multiple": 1, "reasonable_costs": 0 }  # 惩罚性倍数 1~5；合理开支单列
"""
import argparse
import json
import sys

CAP = 5_000_000  # 商标/专利/著作权法定赔偿上限（元），各法具体上限按届行法

def calc(mode: str, d: dict) -> dict:
    base = 0.0
    basis = ""
    if mode == "actual-loss":
        base = (d.get("lost_sales") or 0) * (d.get("unit_profit") or 0) + (d.get("license_loss") or 0)
        basis = "实际损失 = 减少销量×单位利润 + 许可费损失"
    elif mode == "infringer-profit":
        if d.get("unit_profit"):
            base = (d.get("infringing_sales") or 0) * d["unit_profit"]
            basis = "侵权获利 = 侵权销量×单位利润"
        elif d.get("profit_margin"):
            revenue = d.get("infringing_sales") or 0
            base = revenue * d["profit_margin"] / 100.0 if d.get("profit_margin_scale") == "percent" else revenue * d["profit_margin"]
            basis = "侵权获利 = 销售额×利润率"
        else:
            raise ValueError("infringer-profit 模式需提供 unit_profit 或 profit_margin")
    elif mode == "license":
        base = (d.get("license_fee") or 0) * (d.get("multiple") or 1)
        basis = "许可费合理倍数 = 许可费×倍数"
    elif mode == "statutory":
        base = min(d.get("statutory_cap") or CAP, CAP)
        basis = f"法定赔偿（酌定，上限 {CAP:,} 元）"
    else:
        raise ValueError(f"未知模式: {mode}")

    pm = d.get("punitive_multiple") or 1
    if pm < 1 or pm > 5:
        raise ValueError("惩罚性倍数须在 1~5 之间")
    if pm > 1:
        punitive = base * (pm - 1)
        punitive_note = "惩罚性赔偿为主张项（非必得）：须同时满足故意+情节严重+基数可确定，实务认定标准高，法院支持与否存在较大不确定性"
    else:
        punitive = 0.0
        punitive_note = "未主张惩罚性赔偿（默认）。如需主张，须有故意（如通知后仍侵权、假冒注册商标）与情节严重（如再犯、以侵权为业、拒不履行保全）的证据"
    costs = d.get("reasonable_costs") or 0.0
    total = base + punitive + costs

    return {
        "basis": basis,
        "compensation_base": round(base, 2),
        "punitive_damages": round(punitive, 2),
        "reasonable_costs": round(costs, 2),
        "total_claim": round(total, 2),
        "punitive_note": punitive_note,
        "notes": "惩罚性赔偿是主张项而非必得项：法院认定标准高，举证不足时通常仅支持补偿性赔偿+合理开支",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="知识产权赔偿金额计算")
    ap.add_argument("--mode", required=True, choices=["actual-loss", "infringer-profit", "license", "statutory"])
    ap.add_argument("--data", required=True, help="JSON 字符串")
    args = ap.parse_args()
    try:
        d = json.loads(args.data)
        r = calc(args.mode, d)
    except Exception as e:
        print(f"[错误] {e}", file=sys.stderr)
        return 1
    print("计算口径:", r["basis"])
    print(f"补偿性赔偿基数（较有把握）: {r['compensation_base']:,.2f} 元")
    if r["punitive_damages"]:
        print(f"惩罚性赔偿（主张项，非必得）: +{r['punitive_damages']:,.2f} 元")
    if r["reasonable_costs"]:
        print(f"合理维权开支: +{r['reasonable_costs']:,.2f} 元")
    print(f"合计主张（含主张项）: {r['total_claim']:,.2f} 元")
    print("惩罚性赔偿说明:", r["punitive_note"])
    print("风险提示:", r["notes"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
