#!/usr/bin/env bash
# 重新打包 dist/ipswordmaster.zip。两点关键约束：
#  1) 从 publish/ipswordmaster 内部打包，使 zip 根目录即技能根目录（无外层包裹目录），
#     满足 SkillHub 两级目录限制：根目录 / 二级目录 / 文件。
#  2) 剔除所有 *.png —— 图片改为外部托管（见 docs/image-hosting-guide.md），
#     使包体保持在 3M 限制内（当前约 105K）。
set -e
cd "$(dirname "$0")/.."
rm -f dist/ipswordmaster.zip

# 先展平子技能内的 references/ templates/ scripts/ assets/ 子目录，消除第 3 级嵌套。
# 幂等：已展平时无子目录可动，直接跳过；重新从 skills/ 同步后再次运行也能自动修正。
PY="${PY:-/Users/samjoeyang/.workbuddy/binaries/python/envs/default/bin/python}"
"$PY" dist/flatten_package.py

cd publish/ipswordmaster
zip -r ../../dist/ipswordmaster.zip . -x '*.png' -x 'assets/*' -q
cd ../..
echo "=== 打包完成 ==="
ls -lh dist/ipswordmaster.zip
