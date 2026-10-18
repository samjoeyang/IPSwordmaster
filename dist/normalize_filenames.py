#!/usr/bin/env python3
# 将包内非 ASCII（中文）文件名统一改为 ASCII 文件名，并同步更新所有引用
# （@链接 与 正文提及），消除 zip 文件名编码问题导致平台无法解析引用的风险。
import os, subprocess, shutil

ROOT = "publish/ipswordmaster"

MAP = {
    "平台投诉规则矩阵.md": "platform-complaint-rules.md",
    "投诉方案书模板.md": "complaint-plan-template.md",
    "驳回原因与补救策略.md": "rejection-reasons-and-remedies.md",
    "固证方式与取证要点.md": "evidence-preservation-points.md",
    "证据目录模板.md": "evidence-inventory-template.md",
    "侵权判定标准.md": "infringement-criteria.md",
    "抗辩与免责情形.md": "defenses-and-exemptions.md",
    "研判表模板.md": "screening-table-template.md",
    "证据强度与处置路径.md": "evidence-strength-and-actions.md",
}

def git_mv(src, dst):
    r = subprocess.run(["git", "mv", "--force", src, dst], capture_output=True)
    if r.returncode != 0:
        shutil.move(src, dst)

def main():
    renamed = []
    # 1) rename files
    for dp, _, fns in os.walk(ROOT):
        for fn in fns:
            if fn in MAP:
                src = os.path.join(dp, fn)
                dst = os.path.join(dp, MAP[fn])
                if src == dst:
                    continue
                git_mv(src, dst)
                renamed.append((fn, MAP[fn]))
                print(f"  renamed {fn} -> {MAP[fn]}")

    # 2) rewrite references in all markdown (covers @links and prose mentions)
    if renamed:
        for dp, _, fns in os.walk(ROOT):
            for fn in fns:
                if not fn.endswith(".md"):
                    continue
                fp = os.path.join(dp, fn)
                with open(fp, encoding="utf-8") as f:
                    text = f.read()
                new = text
                for old, rep in renamed:
                    new = new.replace(old, rep)
                if new != text:
                    with open(fp, "w", encoding="utf-8") as f:
                        f.write(new)
                    print(f"  updated refs in {os.path.relpath(fp, ROOT)}")

    # 3) verify no non-ascii filenames remain
    bad = [os.path.join(dp, fn) for dp, _, fns in os.walk(ROOT) for fn in fns if not fn.isascii()]
    print(f"remaining non-ascii filenames: {len(bad)}")
    for b in bad:
        print("  STILL NON-ASCII:", b)

if __name__ == "__main__":
    main()
