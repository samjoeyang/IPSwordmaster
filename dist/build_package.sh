#!/usr/bin/env bash
# 构建 SkillHub 上架包 dist/ipswordmaster.zip，一次性满足平台全部结构约束：
#   1) 展平子技能内的 references/ templates/ scripts/ assets/ 子目录 → 最多两级目录
#   2) 中文文件名改为 ASCII → 消除 zip 文件名编码问题（否则平台解析不到引用）
#   3) 从 publish/ipswordmaster 内部打包 → zip 根目录即技能根目录（含 SKILL.md）
#   4) 排除图片（*.png 等）与 assets/ → 图片外部托管，包体 < 3M
# 全部步骤幂等，可反复执行。
set -e
cd "$(dirname "$0")/.."
PY="${PY:-/Users/samjoeyang/.workbuddy/binaries/python/envs/default/bin/python}"

"$PY" dist/flatten_package.py      # 展平嵌套目录（幂等）
"$PY" dist/normalize_filenames.py  # 文件名 ASCII 化并同步引用（幂等）
"$PY" dist/zip_package.py          # 打包并校验（层级/根目录 SKILL.md/编码/体积）

ls -lh dist/ipswordmaster.zip
