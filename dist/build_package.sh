#!/usr/bin/env bash
# 构建 SkillHub 上架包，一次性满足平台全部结构约束。
# 产出：
#   dist/ipswordmaster.zip          —— 聚合包（12 合 1）
#   dist/ip-platform-complaint.zip  —— 平台投诉单技能包
#   dist/legal-lingo-translator.zip —— 法言法语翻译器单技能包
#
# 流水线（全部幂等，可反复执行）：
#   1) flatten_package.py      展平子技能内的 references/ templates/ scripts/ assets/ → 最多两级目录
#   2) normalize_filenames.py  中文文件名改 ASCII，并同步引用
#   3) fix_stale_paths.py      修正展平后残留的失效路径（`references/x.md` → `x.md`）
#   4) validate_frontmatter.py 校验 frontmatter 的 YAML 可解析 + 字段齐全（不满足即退出）
#   5) zip_package.py          Python zipfile 打包 + 自动校验
#      （根目录含 SKILL.md / 层级<=2 / 文件名全 ASCII / 包体<3M，不满足即报错退出）
set -e
cd "$(dirname "$0")/.."
PY="${PY:-/Users/samjoeyang/.workbuddy/binaries/python/envs/default/bin/python}"
QV="${QV:-/Applications/WorkBuddy.app/Contents/Resources/app.asar.unpacked/resources/plugins/workbuddy-builtin/skills/skill-creator/scripts/quick_validate.py}"

# 同步两个共享的内容文件到单技能包源目录。
# 注意：不要覆盖 publish/ip-platform-complaint/SKILL.md ——
# 它是单技能包自己的入口，带单场景定位描述与 @ 引用，与聚合包内的版本不同。
mkdir -p publish/ip-platform-complaint
for f in platform-guides.md complaint-materials.md; do
  cp "publish/ipswordmaster/ip-platform-complaint/$f" "publish/ip-platform-complaint/$f"
done

# 法言法语翻译器：源码已是扁平结构（符合两级限制），直接整体同步为独立包源
mkdir -p publish/legal-lingo-translator
for f in SKILL.md terminology.md templates.md; do
  cp "skills/legal-lingo-translator/$f" "publish/legal-lingo-translator/$f"
done

"$PY" dist/flatten_package.py
"$PY" dist/normalize_filenames.py
"$PY" dist/fix_stale_paths.py

echo "--- frontmatter 校验（源码 + 包源）---"
"$PY" dist/validate_frontmatter.py skills publish | tail -3

echo "--- 聚合包 ---"
"$PY" dist/zip_package.py publish/ipswordmaster dist/ipswordmaster.zip

echo "--- 平台投诉单技能包 ---"
"$PY" dist/zip_package.py publish/ip-platform-complaint dist/ip-platform-complaint.zip

echo "--- 法言法语翻译器单技能包 ---"
"$PY" dist/zip_package.py publish/legal-lingo-translator dist/legal-lingo-translator.zip

echo "--- quick_validate（所有含 SKILL.md 的目录）---"
qfail=0
while IFS= read -r d; do
  out=$("$PY" "$QV" "$d" 2>&1 | tail -1)
  case "$out" in
    *valid*) ;;
    *) qfail=1; echo "  FAIL $d -> $out" ;;
  esac
done < <(find publish -name SKILL.md -exec dirname {} \; | sort -u)
[ "$qfail" -eq 0 ] && echo "  quick_validate 全部通过"

ls -lh dist/ipswordmaster.zip dist/ip-platform-complaint.zip dist/legal-lingo-translator.zip
