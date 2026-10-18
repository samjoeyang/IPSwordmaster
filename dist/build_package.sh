#!/usr/bin/env bash
# 重新打包 dist/ipswordmaster.zip，自动剔除所有 *.png 图片资源。
# 图片改为外部托管：https://ipswordmaster.zhenzhidaole.com/ （见 docs/image-hosting-guide.md）
# 目的：将包体控制在 SkillHub 3M 限制内（当前约 110K）。
set -e
cd "$(dirname "$0")/.."
rm -f dist/ipswordmaster.zip
cd publish
zip -r ../dist/ipswordmaster.zip ipswordmaster -x '*.png' -q
cd ..
echo "=== 打包完成 ==="
ls -lh dist/ipswordmaster.zip
echo "=== 校验：zip 内不应含 png 或外链 ==="
unzip -l dist/ipswordmaster.zip | grep -i "\.png" && echo "警告：zip 含 png" || echo "OK：无 png"
