#!/usr/bin/env python3
# 修正展平后遗留的失效路径引用。
# 展平把 references/ templates/ scripts/ assets/ 里的文件移到子技能根目录后，
# SKILL.md 中仍残留 `references/xxx.md`、`assets/yyy.md` 等旧路径（共 44 处），
# 会误导模型去读不存在的文件。本脚本把这类路径改写为展平后的文件名，并在
# 目标文件确实存在时才改写（否则告警，避免误改）。幂等，可反复执行。
import os, re

ROOT = "publish/ipswordmaster"
SUBS = r"(?:references|templates|scripts|assets)"
# 匹配 `subdir/file`、`@subdir/file`、以及 markdown 链接里的 (subdir/file)
PAT = re.compile(r"(?P<open>[`(@])" + SUBS + r"/(?P<path>[^`)\s]+)(?P<close>[`)])?")

def target_name(path):
    # 展平后文件位于子技能根目录，文件名即 basename
    return os.path.basename(path)

def main():
    total = 0
    unresolved = []
    for dp, _, fns in os.walk(ROOT):
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dp, fn)
            rel = os.path.relpath(fp, ROOT)
            # 引用文件所属的技能目录（入口 SKILL.md 的技能目录即根目录）
            skill = rel.split(os.sep)[0]
            skill_dir = os.path.join(ROOT, skill) if os.path.isdir(os.path.join(ROOT, skill)) else ROOT
            with open(fp, encoding="utf-8") as f:
                text = f.read()

            def repl(m):
                nonlocal total
                new = target_name(m.group("path"))
                if not os.path.exists(os.path.join(skill_dir, new)):
                    unresolved.append((rel, m.group(0)))
                    return m.group(0)
                total += 1
                close = m.group("close") or ""
                return m.group("open") + new + close

            new_text = PAT.sub(repl, text)
            if new_text != text:
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(new_text)
                print(f"  fixed paths in {rel}")

    print(f"rewrote {total} stale path references")
    if unresolved:
        print(f"UNRESOLVED ({len(unresolved)}):")
        for r, m in unresolved[:20]:
            print(f"  {r}: {m}")

if __name__ == "__main__":
    main()
