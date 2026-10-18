# 知产刀客 · 知识产权全链路维权技能包

> 一套覆盖**知识产权维权全链路**的 Agent Skill 集合：从确权核查、侵权发现、侵权比对、证据固定，到平台投诉、行政保护、民事诉讼、刑事维权、判决执行，再到跨境维权。共 **10 个技能**，可被主流 AI Agent 平台作为 Skill 直接安装使用。

- **作者**：知产刀客SamjoeYang
- **状态**：10/10 技能已通过官方校验（`quick_validate.py`）
- **仓库结构**：`skills/`（技能本体）+ `docs/`（总览文档）+ 本 README（说明与安装指引）

---

## 目录

- [一、技能全景](#一技能全景)
- [二、全链路衔接](#二全链路衔接)
- [三、安装说明](#三安装说明)
- [四、使用示例（触发方式）](#四使用示例触发方式)
- [五、已验证内容](#五已验证内容)
- [六、跨平台兼容性](#六跨平台兼容性)
- [七、版本管理与贡献](#七版本管理与贡献)
- [八、版权与作者](#八版权与作者)

---

## 一、技能全景

| # | 技能目录 | 覆盖阶段 | 功能定位 | 捆绑资源 |
|---|---|---|---|---|
| 1 | `ip-rights-audit` | S0 确权与监测 | 权利有效性核查、权利清单、海关备案、监测体系 | references ×2 |
| 2 | `ip-infringement-discovery` | S1 侵权发现 | 多渠道线索收集、主体链锁定、线索分级 | references ×1 |
| 3 | `ip-infringement-analysis` | S2 侵权比对 | 专利/商标/著作权/商业秘密比对、抗辩预判、胜诉评估 | references ×4 |
| 4 | `ip-evidence-collection` | S3 证据固定 | 取证选型、公证/存证/保全、证据链、证据清单 | references ×1 + scripts ×1 |
| 5 | `ip-platform-complaint` | S4 平台投诉 | 淘天/京东/拼多多/抖音通知-删除、申诉应对 | references ×1 + assets ×1 |
| 6 | `ip-administrative-action` | S5 行政保护 | 专利行政裁决、商标/著作权查处、海关扣留 | references ×2 |
| 7 | `ip-civil-litigation` | S6 民事诉讼 | 管辖、保全/禁令、赔偿计算、起诉 | references ×1 + scripts ×1 + assets ×1 |
| 8 | `ip-criminal-enforcement` | S7 刑事维权 | 罪名识别、立案标准、报案/自诉、刑民衔接 | references ×1 |
| 9 | `ip-judgment-execution` | S8 执行监测 | 执行申请、强制措施、拒不执行应对、复发监测 | references ×1 |
| 10 | `ip-cross-border-enforcement` | 跨境贯穿 | 境外平台投诉、ITC 337、海外诉讼、出口海关、权利布局 | references ×2 |

完整功能说明见 [`docs/IP维权技能系列总览.md`](docs/IP维权技能系列总览.md)。

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

## 三、安装说明

本技能包采用通用 Skill 标准结构（`SKILL.md` + `references/` + `scripts/` + `assets/`），支持主流 Agent 平台直接安装，**无需改造**。

### 3.1 通用安装（任意平台）

1. 克隆本仓库：
   ```bash
   git clone <本仓库地址>
   cd 知产刀客
   ```
2. 将 `skills/` 下的技能目录复制到目标平台的 skills 目录（见下表）。

### 3.2 各平台安装路径

| 平台 | 安装目录 | 说明 |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` 或项目内 `.claude/skills/` | 全局或个人项目级 |
| **Claude Desktop** | 技能管理目录 | 通过设置导入技能文件夹 |
| **OpenAI Codex CLI** | `~/.codex/skills/` | 同类约定格式 |
| **通用 Agent 框架** | `.agents/skills/` | 支持该约定的框架均可 |
| **豆包 / 本工作环境** | `workspace/.user_skills/` | 已内置安装 |

以 Claude Code 为例：

```bash
# 全局安装全部技能
mkdir -p ~/.claude/skills
cp -r skills/ip-* ~/.claude/skills/

# 或仅安装需要的技能
cp -r skills/ip-civil-litigation ~/.claude/skills/
```

### 3.3 通过提示词安装（本工作环境一键安装）

若你正在使用 WorkBuddy（本套技能即为此环境打造），可**完全跳过手动复制目录**，直接用一句自然语言让 Agent 帮你安装：

```
帮我安装 IP 维权技能包里的 ip-civil-litigation 技能
```

```
把 IPSwordmaster 仓库里所有 ip- 开头的技能都装到我的工作区
```

```
我要用到平台投诉和证据固定，安装 ip-platform-complaint 和 ip-evidence-collection
```

**工作原理**：提示词安装本质是调用内置的技能安装器（skill installer）。它会根据你提到的技能名或目录，自动把对应的 `skills/<skill>/` 复制到当前工作区的技能目录（项目级 `workspace/.workbuddy/skills/` 或用户级 `~/.workbuddy/skills/`），并校验 `SKILL.md` 结构是否完整。

**要点**：
- 支持"全部安装""按名安装""按维权阶段安装（如 S4 平台投诉相关）"等多种表述，Agent 会自行匹配技能；
- 安装完成后技能立即生效，无需重启对话；
- 若技能已存在，安装器会提示覆盖或跳过，避免重复写入；
- 技能包发布到技能市场后，也可直接说"安装 skill：IPSwordmaster"从市场拉取。

### 3.4 安装后验证

每个技能目录必须包含 `SKILL.md`（YAML frontmatter 含 `name` 与 `description`），且引用资源均使用相对路径。可用本仓库自带校验脚本验证：

```bash
python3 /path/to/skill-creator-for-work/scripts/quick_validate.py skills/ip-rights-audit
# 输出 "Skill is valid!" 即安装成功
```

## 四、使用示例（触发方式）

技能通过 `description` 字段自动触发，以下为典型提问与对应技能：

| 用户提问 | 触发技能 |
|---|---|
| "帮我查一下我的专利有没有被侵权" | `ip-infringement-discovery` + `ip-infringement-analysis` |
| "淘宝上有人卖假货，帮我投诉下架" | `ip-platform-complaint` |
| "侵权人很恶劣，能告他吗？能赔多少？" | `ip-civil-litigation`（`damages_calculator.py` 计算赔偿） |
| "货物出口被海关扣了怎么办 / 亚马逊上有仿冒怎么投诉" | `ip-cross-border-enforcement` |
| "帮我盘点下我的知识产权资产 / 要维权先确权" | `ip-rights-audit` |
| "侵权证据怎么固定？要公证还是存证？" | `ip-evidence-collection` |
| "判决下来了对方不履行怎么办" | `ip-judgment-execution` |
| "假冒伪劣够不够判刑？怎么报案？" | `ip-criminal-enforcement` |

## 五、已验证内容

- 10 个 `SKILL.md` 全部通过 `quick_validate.py`（frontmatter / 命名 / 结构校验）
- `evidence_inventory.py`：正常生成证据清单 + 非法输入拦截
- `damages_calculator.py`：赔偿计算正确 + 非法参数校验；惩罚性赔偿默认不主张，主张时单列"主张项（非必得）"并输出风险提示
- `litigation-guide.md`：含惩罚性赔偿主张要点（慎用）与合理开支主张要点（律师费酌减风险、按 50%~100% 支持率测算）
- 法律依据均已标注来源：专利行政裁决、商标法诉前禁令/证据保全、知识产权海关保护条例、电子商务法通知-删除、平台投诉四要素等

## 六、跨平台兼容性

| 兼容性要素 | 状态 |
|---|---|
| frontmatter 字段 | 核心为 `name` + `description`（标准最小格式）；另含可选元数据 `version` + `license`，不影响最小格式兼容 |
| 资源引用 | 全部相对路径，目录迁移不断链 |
| 脚本依赖 | 仅 Python 标准库（argparse/json/sys），零第三方依赖 |
| 绝对路径硬编码 | 无 |

**使用前注意**：

1. **触发靠 description**：换平台后目标模型按 description 判断何时调用技能（本套已写清触发场景，可直接使用）；
2. **执行能力**：涉浏览器取证、存证平台操作的技能，目标 Agent 需具备浏览器或对应工具能力，否则需人工配合；
3. **内容时效**：`references/` 中的法条与司法解释需按版本更新，建议随平台迁移时核对。

## 七、版本管理与贡献

- 本仓库采用 Git 进行版本管理，技能目录即发布单元；
- 变更建议：每次更新 `references/` 法律依据或脚本逻辑时，同步更新 `docs/IP维权技能系列总览.md` 的"已验证内容"章节并递增版本号；
- 欢迎通过 Issue / PR 反馈问题与改进建议（如平台规则更新、新司法解释）。

## 八、版权与作者

- **作者**：知产刀客SamjoeYang
- **内容性质**：本技能包提供知识产权维权的方法论与流程指引，**不构成正式法律意见**；个案请结合专业律师意见使用。
- 法律依据以中国现行有效法律、行政法规、司法解释为准，使用时请核对最新版本。
