#!/usr/bin/env python3
# 用 Python zipfile 构建 dist/ipswordmaster.zip（替代 macOS zip，保证文件名编码正确）。
# 约束：
#  - zip 根目录即技能根目录（入口 SKILL.md 必须位于根）
#  - 最多两级：根目录 / 二级目录 / 文件
#  - 排除图片（*.png 等，已外部托管）与 assets/、__MACOSX、.DS_Store
# 构建后自动校验，任一约束不满足即报错退出。
import os, sys, zipfile

ROOT = "publish/ipswordmaster"
OUT = "dist/ipswordmaster.zip"
EXCLUDE_DIRS = {"assets", "__MACOSX"}
EXCLUDE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
MAX_DEPTH = 2          # 根目录/二级目录/文件
MAX_SIZE = 3 * 1024 * 1024

def main():
    entries = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = sorted(d for d in dns if d not in EXCLUDE_DIRS)
        for fn in sorted(fns):
            if fn == ".DS_Store":
                continue
            if os.path.splitext(fn)[1].lower() in EXCLUDE_EXT:
                continue
            full = os.path.join(dp, fn)
            arc = os.path.relpath(full, ROOT)
            entries.append((full, arc))
    entries.sort()

    if os.path.exists(OUT):
        os.remove(OUT)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for full, arc in entries:
            zf.write(full, arc)

    # ---- 校验 ----
    errs = []
    names = [a for _, a in entries]
    if "SKILL.md" not in names:
        errs.append("zip 根目录缺少 SKILL.md")
    depth = max((a.count("/") + 1) for a in names) if names else 0
    if depth > MAX_DEPTH:
        errs.append(f"目录层级 {depth} 超过上限 {MAX_DEPTH}")
    bad = [a for a in names if not a.isascii()]
    if bad:
        errs.append(f"存在非 ASCII 文件名: {bad[:3]}")
    size = os.path.getsize(OUT)
    if size > MAX_SIZE:
        errs.append(f"包体 {size} 超过 3M")

    print(f"entries={len(names)}  max_depth={depth}  size={size/1024:.0f}K  non_ascii={len(bad)}")
    print(f"root SKILL.md present: {'SKILL.md' in names}")
    if errs:
        print("校验失败:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print("校验通过：SKILL.md 在根目录、层级<=2、文件名全 ASCII、包体<3M")

if __name__ == "__main__":
    main()
