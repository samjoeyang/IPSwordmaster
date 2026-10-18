---
name: ipswordmaster
display_name: 知识产权全链路维权技能包
display_name_en: IP Rights Full-Chain Enforcement Skill Pack
description: 知识产权全链路维权技能包（聚合版）。一套覆盖确权核查、侵权发现、侵权比对、证据固定、平台投诉、行政保护、民事诉讼、刑事维权、判决执行与跨境维权的 12 个 Agent 技能集合，可被主流 AI Agent 平台作为 Skill 直接安装使用。当用户涉及"知识产权维权""专利/商标/著作权/商业秘密被侵权""下架假货链接""起诉侵权""行政投诉/海关扣货""刑事报案""跨境维权/亚马逊投诉/ITC 337"等场景时使用。Also usable in English when the user mentions IP enforcement, IP litigation, takedown, counterfeiting, customs seizure, ITC 337, or intellectual-property rights protection.
description_zh: 聚合 12 个知识产权维权 Agent 技能，覆盖确权核查、侵权研判、取证固证、平台投诉、行政保护、民事诉讼、刑事维权、裁判执行与跨境维权全链路，可被主流 AI Agent 平台作为 Skill 直接安装使用。
description_en: An aggregated pack of 12 IP-enforcement Agent skills covering the full chain - rights audit, lead screening, evidence collection, platform complaint, administrative action, civil litigation, criminal enforcement, judgment execution and cross-border enforcement - installable as Skills on major AI Agent platforms.
version: 1.0.0
author: SamjoeYang - 上海不丁网络科技有限公司
license: MIT
agent_created: true
---

# 知产刀客 · 知识产权全链路维权技能包（聚合版）

本技能包将 12 个独立技能聚合为单一安装单元。安装后，以下子技能会被一并放入技能目录，由对应场景自动触发：

| 阶段 | 子技能 | 功能 |
|---|---|---|
| S0 确权与监测 | `ip-rights-audit` | 权利有效性核查、权利清单、海关备案、监测体系 |
| S1 侵权发现 | `ip-infringement-discovery` | 多渠道线索收集、主体链锁定、线索分级 |
| S1–S2 侵权研判 | `ip-infringement-screening` | 批量线索研判：侵权类型/近似度/证据强度，输出 P0–P3 风险分级与处置建议 |
| S2 侵权比对 | `ip-infringement-analysis` | 专利/商标/著作权/商业秘密比对、抗辩预判、胜诉评估 |
| S3 证据固定 | `ip-evidence-collection` | 取证选型、公证/存证/保全、证据链、证据清单（含 `evidence_inventory.py`） |
| S4 平台投诉方案 | `ip-complaint-playbook` | 投诉通道/案由/材料清单/对比说明/提交节奏/驳回补救与申诉应对 |
| S4 平台投诉执行 | `ip-platform-complaint` | 淘天/京东/拼多多/抖音通知-删除、申诉应对 |
| S5 行政保护 | `ip-administrative-action` | 专利行政裁决、商标/著作权查处、海关扣留 |
| S6 民事诉讼 | `ip-civil-litigation` | 管辖、保全/禁令、赔偿计算、起诉 |
| S7 刑事维权 | `ip-criminal-enforcement` | 罪名识别、立案标准、报案/自诉、刑民衔接 |
| S8 执行监测 | `ip-judgment-execution` | 执行申请、强制措施、拒不执行应对、复发监测 |
| 跨境贯穿 | `ip-cross-border-enforcement` | 境外平台投诉、ITC 337、海外诉讼、出口海关、权利布局 |

## 使用方式

- 直接将本包安装到目标平台的 skills 目录（如 `~/.claude/skills/`、`~/.workbuddy/skills/`、`.agents/skills/`），或在 WorkBuddy 中用提示词「安装 skill: ipswordmaster」。
- 安装后，按用户自然语言提问，对应子技能会依据其 `description` 自动触发；也可显式点名某个子技能。
- 各子技能均为标准 `SKILL.md` + `references/` + `scripts/` + `assets/` 结构，相对路径引用、脚本仅依赖 Python 标准库，可独立使用。

## 说明

- 内容为中国现行知识产权法律框架下的维权方法论与流程指引，不构成正式法律意见；个案请结合专业律师意见。
- 子技能 `ip-civil-litigation` 含 `damages_calculator.py`、`ip-evidence-collection` 含 `evidence_inventory.py`，运行需 Python 3 与代码执行环境。
