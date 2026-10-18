# SkillHub 提交指南（ipswordmaster）

> 用途：本仓库已把技能包补到「可过审」最终形态。本文是提交到 WorkBuddy 技能市场（SkillHub）的**人工上传操作清单**。  
> 重要：当前环境**没有**「提交到技能市场」的 API，实际上传必须在 **WorkBuddy 开放平台 portal（open.workbuddy.cn）** 完成，并经过「机器扫描 + AI 审核 + 人工抽检」，约 7 个工作日。

---

## 1. 待提交资产

| 项目 | 路径 / 值 |
|---|---|
| 聚合包 zip（已提交审核） | `dist/ipswordmaster.zip` |
| 平台投诉单技能 zip | `dist/ip-platform-complaint.zip` |
| 法言法语翻译器 zip（**备用，当前不提交**） | `dist/legal-lingo-translator.zip` |
| 聚合包源码（备查） | `publish/ipswordmaster/` |
| 单技能源码（备查） | `publish/ip-platform-complaint/`、`publish/legal-lingo-translator/` |
| 封面图 / 技能图标 | 已移出 zip，外部托管于 `https://ipswordmaster.zhenzhidaole.com/`（见 `docs/image-hosting-guide.md`），portal 提交表单里单独上传 |
| 开发者主页文案 | `docs/developer-homepage-copy.md`（联系方式**只填这里**） |

> 三个包都**不含 PNG**：图片已外部托管，包体分别为 96K（聚合）、5K（平台投诉）、12K（法言法语翻译器），远低于 3M 限制。



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

### 2.1 平台投诉单技能（ip-platform-complaint）填写字段

| 字段 | 建议值 |
|---|---|
| 资产类型 | Skill（技能） |
| 名称（name） | `ip-platform-complaint` |
| 展示名 | 电商平台投诉 |
| 展示名（英文） | E-commerce Platform Complaint |
| 分类 | 法律 / 知识产权 |
| 标签 | 电商平台投诉、通知-删除、下架侵权链接、假货仿品、卖家申诉、淘天IPP、京东、拼多多、抖音 |
| 简介（中文） | 单场景专项技能，只做电商平台知识产权投诉（通知-删除）与申诉应对：覆盖淘天（淘宝/天猫IPP）、京东、拼多多、抖音等平台的投诉流程、合格通知四要素、材料准备、提交跟进、卖家申诉应对与平台介入申请。仅聚焦平台投诉环节，不含取证、行政查处、民事诉讼等其他维权环节。 |
| 简介（英文） | A single-scenario skill focused solely on e-commerce platform IP complaints (notice-and-takedown) and appeal handling, covering Taobao/Tmall IPP, JD, Pinduoduo and Douyin. Scoped to the platform-complaint stage only. |
| 差异化说明（**必填**） | 与聚合包 `ipswordmaster` 的差异：聚合包覆盖确权→取证→投诉→行政→诉讼→刑事→执行→跨境全链路的 12 个环节；本技能只做其中「平台投诉」**一个**环节，面向只想快速下架侵权链接、不需要全链路方案的用户，体积小、触发精准。两者使用场景与用户群不同，非功能重复。 |

### 2.2 法言法语翻译器（legal-lingo-translator）填写字段

> **状态**：该技能**默认只存放于项目目录 `skills/legal-lingo-translator/`**，不并入聚合包，
> 当前也未单独提交。本节为**备用**——若日后决定单独上架，按此填写即可。

| 字段 | 建议值 |
|---|---|
| 资产类型 | Skill（技能） |
| 名称（name） | `legal-lingo-translator` |
| 展示名 | 法言法语翻译器 |
| 展示名（英文） | Legal Lingo Translator |
| 分类 | 法律 / 法律工具（或「效率工具」） |
| 标签 | 法言法语、法律文书、起诉状、判决书解读、律师函、法律术语、口语转书面语、大白话解释 |
| 简介（中文） | 法律语言双向翻译工具。正向把日常口语/白话改写为庭审陈述、起诉状、报案材料、劳动仲裁申请书等法律文书可用的规范书面语；反向把判决书、律师函、合同条款、法条翻译成大白话，并点明实际影响与关键期限。覆盖民事纠纷、刑事报案、劳动争议、婚姻家事等场景。 |
| 简介（英文） | Two-way translator between everyday spoken Chinese and formal legal writing. Converts casual speech into courtroom-ready formal wording; explains judgments, demand letters, contract clauses and statutes in plain language with key deadlines flagged. |
| 差异化说明（**必填**） | 与知识产权类技能包（`ipswordmaster`、`ip-platform-complaint`）的差异：本技能是**通用法律语言工具**，面向普通大众的民事、刑事、劳动、婚姻家事日常法律场景；IP 类技能面向企业/权利人的知识产权维权，属专业垂类。两者**用户群不同（C 端个人 vs B 端权利人）、解决的问题不同（语言转换 vs 维权方案）、场景不重叠**，非功能重复。本技能不做侵权判定、不输出维权方案。 |

---

## 3. 操作步骤

1. **完善开发者信息**（首次必须）：登录 open.workbuddy.cn → 设置 → 开发者信息，上传头像（512×512）、填昵称（如「知产刀客 · SamjoeYang」）、简介（20–120 字，见 `docs/developer-homepage-copy.md`）、联系方式（官网/邮箱/公众号，1–5 项）。
2. **新建资产**：工作台 → 新建 → Skill（技能）。
3. **上传 zip**：
   - 提交**聚合包** → 选择 `dist/ipswordmaster.zip`（已提交审核）。
   - 提交**平台投诉单技能** → 选择 `dist/ip-platform-complaint.zip`，并在表单里填好 2.1 节的「差异化说明」。
   - 提交**法言法语翻译器**（可选，当前默认不提交）→ 选择 `dist/legal-lingo-translator.zip`，并在表单里填好 2.2 节的「差异化说明」。
4. **核对并补字段**：确认名称、分类、标签、封面/图标，按第 2 节填。
5. **提交审核**：提交后进入「安全扫描 + AI 审核 + 人工抽检」。
6. **过审上架**：通过后上架生态市场，用户可搜索/安装；后台可见安装量与评价。

---

## 4. 合规红线提醒（提交前必读）

- **同品牌单一入口（重点）**：平台要求同品牌原则上单一入口。因此**不要**把 12 个子技能逐个单独上架。目前安排如下：
  - **已单独上架**：`ip-platform-complaint`（IP 垂类内部单环节 vs 聚合包全链路，见 2.1 节）。
  - **暂不单独上架**：`legal-lingo-translator` —— 仅存放于项目目录 `skills/`，不进聚合包也不单独提交。若日后要上架，必须随附 2.2 节的差异化说明（通用法律工具 vs IP 维权，不同品类、不同用户群）。
  
  若审核追问，按对应说明应答。**再新增单技能前先评估是否会构成重复入口。**
- **零外链 / 零导流**：包内已确保无任何 http/https 链接、裸域名、二维码、作者邮箱或「联系我」CTA。联系方式只放在开发者主页。
- **version 递增铁律**：凡重传必 bump `version` 且必须 > 线上最新版本；版本号不变直接重传会被拒收。
- **禁虚假能力声明**：描述不得出现「精准预测 / 必中 / 100% 准确 / 保证效果」等词（本包已规避）。
- **声明与功能相符**：技能功能须与描述一致，整改时限内不改会被下架。

---

## 5. 提交自检清单

提交前用 `bash dist/build_package.sh` 一键重建，脚本会自动校验并报错：

- [ ] zip 均已生成：`dist/ipswordmaster.zip`（96K）、`dist/ip-platform-complaint.zip`（5K）；`dist/legal-lingo-translator.zip`（12K，备用）
- [ ] 自动校验通过：zip 根目录含 SKILL.md、目录层级 ≤2、文件名全 ASCII、无 PNG、包体 <3M
- [ ] 包内零外链 / 零裸域名 / 零作者联系方式
- [ ] 所有 SKILL.md 均含 `name`/`description`/`description_zh`/`description_en`/`version`/`author`
- [ ] 开发者主页已填昵称、简介、联系方式（联系方式仅在此处）
- [ ] 单技能提交时已附「差异化说明」（同品牌单一入口要求）
- [ ] 提交 version 大于此前任何线上版本（凡重传必 bump）
