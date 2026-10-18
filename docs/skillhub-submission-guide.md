# SkillHub 提交指南（ipswordmaster）

> 用途：本仓库已把技能包补到「可过审」最终形态。本文是提交到 WorkBuddy 技能市场（SkillHub）的**人工上传操作清单**。  
> 重要：当前环境**没有**「提交到技能市场」的 API，实际上传必须在 **WorkBuddy 开放平台 portal（open.workbuddy.cn）** 完成，并经过「机器扫描 + AI 审核 + 人工抽检」，约 7 个工作日。

---

## 1. 待提交资产

| 项目            | 路径 / 值                                               |
| ------------- | ---------------------------------------------------- |
| 技能包 zip（提交文件） | `dist/ipswordmaster.zip`                             |
| 聚合包源码（备查）     | `publish/ipswordmaster/`                             |
| 封面图（1 张）      | `publish/ipswordmaster/assets/cover.png`             |
| 各技能图标（12 张）   | `publish/ipswordmaster/assets/ip-<技能名>/ip-<技能名>.png` |
| 开发者主页文案       | `docs/developer-homepage-copy.md`（联系方式**只填这里**）      |



---

## 2. portal 填写字段建议

| 字段                | 建议值                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 资产类型              | Skill（技能）                                                                                                                                                                                                                                                                                                                 |
| 名称（name，小写、连字符）   | `ipswordmaster`                                                                                                                                                                                                                                                                                                           |
| 展示名（display_name） | 知识产权全链路维权技能包                                                                                                                                                                                                                                                                                                              |
| 展示名（英文）           | IP Rights Full-Chain Enforcement Skill Pack                                                                                                                                                                                                                                                                               |
| 分类                | 法律 / 知识产权（或「法律合规」）                                                                                                                                                                                                                                                                                                        |
| 标签                | 专利、商标、著作权、商业秘密、维权、下架、平台投诉、海关保护、ITC 337、跨境维权                                                                                                                                                                                                                                                                               |
| 简介（中文）            | 聚合 12 个知识产权维权 Agent 技能，覆盖确权核查、侵权研判、取证固证、平台投诉、行政保护、民事诉讼、刑事维权、裁判执行与跨境维权全链路，可被主流 AI Agent 平台作为 Skill 直接安装使用。                                                                                                                                                                                                                 |
| 简介（英文）            | An aggregated pack of 12 IP-enforcement Agent skills covering the full chain — rights audit, lead screening, evidence collection, platform complaint, administrative action, civil litigation, criminal enforcement, judgment execution and cross-border enforcement — installable as Skills on major AI Agent platforms. |
| 封面                | 上传 `assets/cover.png`                                                                                                                                                                                                                                                                                                     |
| 图标                | 各技能对应 `assets/ip-*/` 下 PNG                                                                                                                                                                                                                                                                                                |

> 上述 name / display_name / description_zh / description_en / version / author 已内置在 `dist/ipswordmaster.zip` 的 SKILL.md 中，portal 解析后通常自动带入；若 portal 另需表单填写，按上表填即可。

---

## 3. 操作步骤

1. **完善开发者信息**（首次必须）：登录 open.workbuddy.cn → 设置 → 开发者信息，上传头像（512×512）、填昵称（如「知产刀客 · SamjoeYang」）、简介（20–120 字，见 `docs/developer-homepage-copy.md`）、联系方式（官网/邮箱/公众号，1–5 项）。
2. **新建资产**：工作台 → 新建 → Skill（技能）。
3. **上传 zip**：选择 `dist/ipswordmaster.zip` 上传，等待平台解析。
4. **核对并补字段**：确认名称、分类、标签、封面/图标，按第 2 节填。
5. **提交审核**：提交后进入「安全扫描 + AI 审核 + 人工抽检」。
6. **过审上架**：通过后上架生态市场，用户可搜索/安装；后台可见安装量与评价。

---

## 4. 合规红线提醒（提交前必读）

- **同品牌单一入口**：本次只上架聚合包 `ipswordmaster` 一个入口。**不要**再单独上架 12 个子技能——否则触发「同品牌原则上单一入口」规则，需补差异化材料（功能对比表、用户群差异、选择路径、不合并理由）。
- **零外链 / 零导流**：包内已确保无任何 http/https 链接、裸域名、二维码、作者邮箱或「联系我」CTA。联系方式只放在开发者主页。
- **version 递增铁律**：凡重传必 bump `version` 且必须 > 线上最新版本；版本号不变直接重传会被拒收。
- **禁虚假能力声明**：描述不得出现「精准预测 / 必中 / 100% 准确 / 保证效果」等词（本包已规避）。
- **声明与功能相符**：技能功能须与描述一致，整改时限内不改会被下架。

---

## 5. 提交自检清单

- [ ] `dist/ipswordmaster.zip` 已生成（13 SKILL.md + 13 PNG）
- [ ] 包内零外链 / 零裸域名 / 零作者联系方式（已扫描确认）
- [ ] 13 个 SKILL.md 均含 `name`/`description`/`description_zh`/`description_en`/`version`/`author`
- [ ] 开发者主页已填昵称、简介、联系方式（联系方式仅在此处）
- [ ] 仅在 portal 上架单一聚合包 `ipswordmaster`
- [ ] 提交 version 大于此前任何线上版本
