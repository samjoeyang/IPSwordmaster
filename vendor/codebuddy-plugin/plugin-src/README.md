# 维权下架官 · ip-platform-complaint

平台投诉专员（Agent 型专家）。把一批疑似侵权线索，变成能执行、能过审、能回填台账的投诉方案。

**与其他知识产权专家的区别**：市面上的专家讲「法律上能不能告」，本专家讲「这个平台这么投才过」。

## 类型

Agent 型（单个 AI 专家） · 分类 `11-SecurityCompliance`（法务安全）

## 组成

| 部分 | 内容 |
|---|---|
| `agents/ip-platform-complaint.md` | 专家人设与工作流（研判 → 固证 → 方案 → 提交 → 补救） |
| `skills/ip-infringement-screening` | 侵权线索批量研判，P0–P3 分级 |
| `skills/ip-evidence-collection` | 取证固证清单、证据目录、存证方式选择 |
| `skills/ip-complaint-playbook` | 平台投诉规则矩阵、驳回补救、申诉应对、投诉方案书模板 |

## 使用示例

- 这批链接要投诉，帮我研判并出一份投诉方案
- 投诉被平台驳回了，帮我分析驳回原因和补救方案
- 卖家提交了授权书申诉，我该怎么应对

## 使用前提

1. 需提供：权利人、投诉主体、授权链、权利基础（类别/有效期）、正品参考价、白名单
2. **未完成固证不得提交投诉** —— 投诉即惊动对方，证据会灭失
3. 输出为内部执行方案，**不构成法律意见**，对外提交前须经具备执业资格的专业人员复核

## 头像

头像已自动生成在 `avatars/` 目录下。如需替换为自定义头像，要求：
- 格式：PNG（推荐）或 JPG
- 尺寸：512×512 px
- 大小：单张不超过 500KB

## 待办

- [ ] 平台投诉规则矩阵中各平台的入口地址、审核周期需按实际核实回填（当前标注为「待填写」）
- [ ] 驳回/申诉失败案例需在实际使用中回写至 `skills/ip-complaint-playbook/SKILL.md` 的「误判与经验记录」
- [ ] references 中的法律框架内容需由律师复核

## 安装

将专家包目录放到专家目录下：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/ip-platform-complaint/
```

然后运行注册命令使其可见：

```bash
python3 scripts/register_expert.py <expert-dir>
```

## 打包分享

```bash
python3 scripts/package_expert.py <expert-dir> <output-dir>
```

> 中文文件名打包请用官方 package_expert.py 或 Python `zipfile`。
> macOS 自带 `zip -r` 不写 UTF-8 标记位，Windows 上解压中文名会乱码。
