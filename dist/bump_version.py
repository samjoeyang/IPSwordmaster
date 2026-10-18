#!/usr/bin/env python3
# 按 SkillHub「version 递增铁律」批量递增 SKILL.md 的 patch 版本号。
# 重传已提交/已上架的包时必须 bump，版本号不变直接重传会被拒收。
#
# 用法：
#   bump_version.py              # 默认 bump 聚合包（入口 + 12 子技能）及其 skills/ 源码
#   bump_version.py <路径>...    # 指定 SKILL.md 或其所在目录
#
# 只改 frontmatter 里的第一个 `version: X.Y.Z`（frontmatter 在文件开头，
# 用 count=1 保证不会误改正文中出现的同形文本）。
import os, re, sys

VERSION_RE = re.compile(r"^version: (\d+)\.(\d+)\.(\d+)$", re.M)


def collect_default():
    """默认目标：聚合包（入口 + ip-* 子技能）+ skills/ 下同名 IP 技能源码。"""
    targets = []
    entry = "publish/ipswordmaster/SKILL.md"
    if os.path.exists(entry):
        targets.append(entry)
    agg = "publish/ipswordmaster"
    if os.path.isdir(agg):
        for d in sorted(os.listdir(agg)):
            if not d.startswith("ip-"):
                continue
            p = os.path.join(agg, d, "SKILL.md")
            if os.path.exists(p):
                targets.append(p)
    # skills/ 源码与聚合包子技能同名，同步 bump，避免日后同步时版本倒退
    if os.path.isdir("skills"):
        for d in sorted(os.listdir("skills")):
            if not d.startswith("ip-"):
                continue
            p = os.path.join("skills", d, "SKILL.md")
            if os.path.exists(p):
                targets.append(p)
    return targets


def expand(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for dp, _, fns in os.walk(p):
                for fn in fns:
                    if fn == "SKILL.md":
                        out.append(os.path.join(dp, fn))
        elif os.path.isfile(p):
            out.append(p)
        else:
            print(f"  SKIP 不存在: {p}")
    return sorted(set(out))


def main():
    args = sys.argv[1:]
    targets = expand(args) if args else collect_default()

    changed = 0
    for p in sorted(set(targets)):
        with open(p, encoding="utf-8") as f:
            text = f.read()
        m = VERSION_RE.search(text)
        if not m:
            print(f"  SKIP 无 version 字段: {p}")
            continue

        def repl(mm):
            return f"version: {mm.group(1)}.{mm.group(2)}.{int(mm.group(3)) + 1}"

        old = m.group(0)
        new_text = VERSION_RE.sub(repl, text, count=1)
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_text)
        changed += 1
        print(f"  {old.split(': ')[1]} -> {repl(m).split(': ')[1]}   {p}")

    print(f"\nbumped {changed} 个 SKILL.md（patch +1）")


if __name__ == "__main__":
    main()
