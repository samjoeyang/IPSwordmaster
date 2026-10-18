#!/usr/bin/env python3
# 将 publish/ipswordmaster 中每个子技能目录下的 references/ templates/ scripts/ assets/
# 子目录展平到子技能目录本身，消除第 3 级目录嵌套（满足 SkillHub 两级目录限制）。
# 同时把所有 @references/X @templates/X @scripts/X @assets/X 链接改写为 @X（指向展平后的文件）。
import os, re, subprocess, sys

ROOT = "publish/ipswordmaster"
SUBS = ["references", "templates", "scripts", "assets"]
LINK_RE = re.compile(r"@(references|templates|scripts|assets)/([^)\s@]+)")

def git_mv(src, dst):
    # prefers `git mv` to preserve rename history; falls back to plain rename
    # (e.g. when running outside a git worktree).
    r = subprocess.run(["git", "mv", "--force", src, dst], capture_output=True)
    if r.returncode != 0:
        import shutil
        shutil.move(src, dst)

def main():
    # mapping: skill_rel -> { "subdir/basename": newname }
    mappings = {}
    for skill in sorted(os.listdir(ROOT)):
        sdir = os.path.join(ROOT, skill)
        if not os.path.isdir(sdir) or not skill.startswith("ip-"):
            continue
        mapping = {}
        for sub in SUBS:
            sdir_sub = os.path.join(sdir, sub)
            if not os.path.isdir(sdir_sub):
                continue
            for fn in os.listdir(sdir_sub):
                src = os.path.join(sdir_sub, fn)
                if not os.path.isfile(src):
                    continue
                dst = os.path.join(sdir, fn)
                newname = fn
                if os.path.exists(dst):
                    # collision: prefix with subdir
                    base, ext = os.path.splitext(fn)
                    newname = f"{sub}-{base}{ext}"
                    dst = os.path.join(sdir, newname)
                    print(f"  COLLISION rename {skill}/{sub}/{fn} -> {skill}/{newname}")
                git_mv(src, dst)
                mapping[f"{sub}/{fn}"] = newname
            # remove empty subdir
            try:
                os.rmdir(sdir_sub)
                print(f"  removed empty dir {skill}/{sub}")
            except OSError:
                pass
        if mapping:
            mappings[skill] = mapping

    # rewrite @links in every .md under ROOT
    for dirpath, _, files in os.walk(ROOT):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            with open(fp, encoding="utf-8") as f:
                text = f.read()
            def repl(m):
                sub = m.group(1)
                rest = m.group(2)
                key = f"{sub}/{rest}"
                # find which skill this file belongs to
                rel = os.path.relpath(fp, ROOT)
                skill = rel.split(os.sep)[0]
                newname = mappings.get(skill, {}).get(key)
                if newname is None:
                    # maybe rest is just basename already; fallback to basename
                    newname = os.path.basename(rest)
                    print(f"  WARN unmatched link @{key} in {rel}")
                return "@" + newname
            new_text = LINK_RE.sub(repl, text)
            if new_text != text:
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(new_text)
                print(f"  rewrote links in {os.path.relpath(fp, ROOT)}")

    print("DONE. Mappings:")
    for k, v in mappings.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
