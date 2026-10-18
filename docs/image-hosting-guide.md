# 图片资源外部托管指南

为将技能包 `dist/ipswordmaster.zip` 控制在 SkillHub 平台 **3M** 限制内，所有图片资源已从压缩包中剔除（包体由约 **10M** 降至约 **110K**），改为托管在独立域名下。

## 域名

`https://ipswordmaster.zhenzhidaole.com/`

## 托管源目录（本地）

```
publish/ipswordmaster/assets/      ← 13 张 PNG，共约 9.5M，作为外部托管源
```

目录结构（上传后需保持此结构，使 `assets/` 前缀不变）：

```
assets/
├── cover.png
├── ip-administrative-action/ip-administrative-action.png
├── ip-civil-litigation/ip-civil-litigation.png
├── ip-complaint-playbook/ip-complaint-playbook.png
├── ip-criminal-enforcement/ip-criminal-enforcement.png
├── ip-cross-border-enforcement/ip-cross-border-enforcement.png
├── ip-evidence-collection/ip-evidence-collection.png
├── ip-infringement-analysis/ip-infringement-analysis.png
├── ip-infringement-discovery/ip-infringement-discovery.png
├── ip-infringement-screening/ip-infringement-screening.png
├── ip-judgment-execution/ip-judgment-execution.png
├── ip-platform-complaint/ip-platform-complaint.png
└── ip-rights-audit/ip-rights-audit.png
```

## 上传步骤

1. 将本地 `publish/ipswordmaster/assets/` 整个目录上传到 `ipswordmaster.zhenzhidaole.com` 的网站根目录。
2. 上传后校验下列地址可正常访问（返回图片）：

| 本地文件 | 外部访问地址 |
|---|---|
| `assets/cover.png` | `https://ipswordmaster.zhenzhidaole.com/assets/cover.png` |
| `assets/ip-rights-audit/ip-rights-audit.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-rights-audit/ip-rights-audit.png` |
| `assets/ip-infringement-discovery/ip-infringement-discovery.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-infringement-discovery/ip-infringement-discovery.png` |
| `assets/ip-infringement-screening/ip-infringement-screening.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-infringement-screening/ip-infringement-screening.png` |
| `assets/ip-infringement-analysis/ip-infringement-analysis.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-infringement-analysis/ip-infringement-analysis.png` |
| `assets/ip-evidence-collection/ip-evidence-collection.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-evidence-collection/ip-evidence-collection.png` |
| `assets/ip-complaint-playbook/ip-complaint-playbook.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-complaint-playbook/ip-complaint-playbook.png` |
| `assets/ip-platform-complaint/ip-platform-complaint.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-platform-complaint/ip-platform-complaint.png` |
| `assets/ip-administrative-action/ip-administrative-action.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-administrative-action/ip-administrative-action.png` |
| `assets/ip-civil-litigation/ip-civil-litigation.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-civil-litigation/ip-civil-litigation.png` |
| `assets/ip-criminal-enforcement/ip-criminal-enforcement.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-criminal-enforcement/ip-criminal-enforcement.png` |
| `assets/ip-judgment-execution/ip-judgment-execution.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-judgment-execution/ip-judgment-execution.png` |
| `assets/ip-cross-border-enforcement/ip-cross-border-enforcement.png` | `https://ipswordmaster.zhenzhidaole.com/assets/ip-cross-border-enforcement/ip-cross-border-enforcement.png` |

## 合规说明（重要）

- 技能包 **zip 内不含任何外链、不含图片**，完全符合 SkillHub「零外链」红线。
- 图片仅作为外部资产在域名下托管，供官网 / 开发者主页 / GitHub Pages 等站内引用，**不写入任何 SKILL.md 内容**。
- 若日后需要在技能包内显示封面/图标并引用上述 URL，会引入外链，可能触发平台红线，须另行评估后再决定。

## 重新打包（剔除图片）

```bash
bash dist/build_package.sh
```

该脚本会重新生成 `dist/ipswordmaster.zip`，自动排除所有 `*.png`，确保包体持续 < 3M。
