# 知产刀客 · 知识产权全链路技能系列

> 安装目录：`/home/user/.doubao/agent_mode/workspace/.user_skills/`
> 构建工具：`skill-creator-for-work`（init_skill.py 初始化 + quick_validate.py 校验）
> 状态：12/12 技能已创建并通过官方校验
> 作者：**知产刀客 · SamjoeYang**

## 一、技能全景（按维权链路排序）

| # | 技能目录 | 覆盖阶段 | 功能定位 | 捆绑资源 |
|---|---|---|---|---|
| 1 | `ip-rights-audit` | S0 确权与监测 | 权利有效性核查、权利清单、海关备案、监测体系 | references ×2（核查清单、监测渠道） |
| 2 | `ip-infringement-discovery` | S1 侵权发现 | 多渠道线索收集、主体链锁定、线索分级 | references ×1（渠道与台账） |
| 3 | `ip-infringement-screening` | S1–S2 侵权研判 | 批量线索研判：侵权类型/近似度/证据强度，输出 P0–P3 风险分级与处置建议 | references ×3 + templates ×1 |
| 4 | `ip-infringement-analysis` | S2 侵权比对 | 专利/商标/著作权/商业秘密比对、抗辩预判、胜诉评估 | references ×4（四类比对规则） |
| 5 | `ip-evidence-collection` | S3 证据固定 | 取证选型、公证/存证/保全、证据链、证据清单（含 `evidence_inventory.py` 批量生成） | references ×1 + templates ×1 + scripts ×1 |
| 6 | `ip-complaint-playbook` | S4 平台投诉方案 | 投诉通道/案由/材料清单/对比说明/提交节奏/驳回补救与申诉应对 | references ×2 + templates ×1 |
| 7 | `ip-platform-complaint` | S4 平台投诉执行 | 淘天/京东/拼多多/抖音通知-删除、申诉应对 | references ×1 + assets ×1（投诉材料模板） |
| 8 | `ip-administrative-action` | S5 行政保护 | 专利行政裁决、商标/著作权查处、海关扣留 | references ×2（裁决、海关） |
| 9 | `ip-civil-litigation` | S6 民事诉讼 | 管辖、保全/禁令、赔偿计算（补偿性为主、惩罚性为"主张项"）、起诉 | references ×1 + scripts ×1（赔偿计算）+ assets ×1（起诉状模板） |
| 10 | `ip-criminal-enforcement` | S7 刑事维权 | 罪名识别、立案标准、报案/自诉、刑民衔接 | references ×1（罪名与门槛） |
| 11 | `ip-judgment-execution` | S8 执行监测 | 执行申请、强制措施、拒不执行应对、复发监测 | references ×1（执行要点） |
| 12 | `ip-cross-border-enforcement` | 跨境贯穿 | 境外平台投诉、ITC 337、海外诉讼、出口海关、权利布局 | references ×2（境外平台、境外救济） |

> 平台投诉专用子链路（源自 CodeBuddy 插件「维权下架官」）：`ip-infringement-screening` → `ip-evidence-collection` → `ip-complaint-playbook` → `ip-platform-complaint`，已融合进本包 S1–S4 阶段。

## 二、全链路衔接

```
S0 确权监测 → S1 发现线索 → S2 侵权比对 → S3 证据固定
        │                                        │
        ▼                                        ▼
S4 路径决策（函件协商 / 平台投诉 / 展会投诉）◀── 证据包
        │
        ├──→ S5 行政保护（裁决/查处/海关）
        ├──→ S6 民事诉讼（禁令/保全/赔偿）────┐
        ├──→ S7 刑事维权（报案/自诉）───────┤
        └──→ 跨境维权（境外平台/337/海外诉讼）──┤
                                             ▼
                                        S8 执行 → 复发监测 → 回到 S0/S1
```

## 三、使用示例（触发方式）

- "帮我查一下我的专利有没有被侵权" → `ip-infringement-discovery` + `ip-infringement-analysis`
- "淘宝上有人卖假货，帮我投诉下架" → `ip-platform-complaint`
- "侵权人很恶劣，能告他吗？能赔多少？" → `ip-civil-litigation`（`damages_calculator.py` 算赔偿）
- "货物出口被海关扣了怎么办 / 亚马逊上有仿冒怎么投诉" → `ip-cross-border-enforcement`

## 四、已验证内容

- 12 个 SKILL.md 全部通过 `quick_validate.py`（frontmatter/命名/结构校验）
- `evidence_inventory.py`：正常生成证据清单 + 非法输入拦截（缺必填字段报错）
- `damages_calculator.py`：赔偿计算正确 + 非法参数校验；惩罚性赔偿默认不主张，主张时单列"主张项（非必得）"并输出风险提示（法院认定标准高，支持存在不确定性）
- `litigation-guide.md`：含惩罚性赔偿主张要点（慎用）与合理开支主张要点（律师费酌减风险、按50%~100%支持率测算）
- 法律依据：专利行政裁决（局令81号）、商标法第65/66条（诉前禁令/证据保全）、知识产权海关保护条例（3个工作日扣留申请）、电子商务法通知-删除、平台投诉四要素等均已在 references 中标注来源

## 五、待迭代方向

- 按真实案件复盘校准 references（如平台规则更新、新司法解释）
- 可扩展：商标/专利的国际布局技能、侵权监测自动化脚本、诉讼文书批量生成
