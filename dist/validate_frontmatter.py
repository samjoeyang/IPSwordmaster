#!/usr/bin/env python3
# 校验所有 SKILL.md 的 frontmatter：YAML 可解析 + 必需字段齐全。
#
# 背景：legal-lingo-translator 曾因 description 里出现 ASCII 冒号+空格
# （"Also usable in English: use when..."）导致平台报
# 「SKILL.md 格式错误 — frontmatter 无法解析」。
# 中文全角冒号（：）对 YAML 无害，ASCII 的 ": " 会被当成嵌套映射的开头。
# zip_package.py 只校验结构（层级/ASCII 文件名/包体），不校验 YAML，因此补这一道。
import os, sys, yaml

# 项目标准字段集（聚合包与单技能包都按此标准）
REQUIRED = [
    "name", "display_name", "display_name_en",
    "description", "description_zh", "description_en",
    "version", "author", "license", "agent_created",
]
MINIMAL = ["name", "description"]  # Skill 规范最小公约数


def split_frontmatter(text):
    """返回 (frontmatter_str, body)；无合法 frontmatter 时返回 (None, text)。"""
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    # 第一个 --- 之后，找下一个 ---
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def check_file(fp):
    """返回 (errors, warnings)"""
    errors, warnings = [], []
    with open(fp, encoding="utf-8") as f:
        text = f.read()
    fm, _ = split_frontmatter(text)
    if fm is None:
        errors.append("缺少 frontmatter 或未以 --- 正确包裹")
        return errors, warnings
    try:
        meta = yaml.safe_load(fm)
    except yaml.YAMLError as e:
        errors.append(f"YAML 解析失败: {str(e).splitlines()[0]}")
        return errors, warnings
    if not isinstance(meta, dict):
        errors.append(f"frontmatter 顶层不是映射，实际为 {type(meta).__name__}")
        return errors, warnings
    for k in MINIMAL:
        if k not in meta:
            errors.append(f"缺少必需字段 {k}")
    for k in REQUIRED:
        if k not in meta:
            warnings.append(f"缺项目标准字段 {k}")
    if "name" in meta:
        n = str(meta["name"])
        if n != n.lower() or " " in n or "_" in n:
            errors.append(f"name 应为小写连字符风格，当前为 '{n}'")
    return errors, warnings


def main():
    roots = sys.argv[1:] or ["skills", "publish"]
    total = 0
    bad = 0
    seen = set()
    for root in roots:
        for dp, _, fns in os.walk(root):
            for fn in fns:
                if fn != "SKILL.md":
                    continue
                fp = os.path.join(dp, fn)
                if os.path.abspath(fp) in seen:
                    continue
                seen.add(os.path.abspath(fp))
                total += 1
                errors, warnings = check_file(fp)
                if errors:
                    bad += 1
                    print(f"[FAIL] {fp}")
                    for e in errors:
                        print(f"         {e}")
                elif warnings:
                    print(f"[WARN] {fp}")
                    for w in warnings:
                        print(f"         {w}")
                else:
                    print(f"[ OK ] {fp}")
    print(f"\n扫描 {total} 个 SKILL.md：{bad} 个阻断错误")
    if bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
