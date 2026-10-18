---
name: ip-civil-litigation
display_name: 知识产权民事诉讼
display_name_en: IP Civil Litigation
description: 知识产权民事诉讼：管辖确定、诉前/诉中行为保全（禁令）与财产/证据保全、起诉与举证、损害赔偿计算（实际损失/侵权获利/许可费合理倍数/法定赔偿、恶意侵权惩罚性赔偿）、一审二审程序。当用户需要"起诉侵权""申请禁令""诉前保全""计算赔偿金额""写起诉状/证据目录"时使用。Also usable in English when the user mentions IP civil litigation, injunction, preliminary injunction, evidence preservation, damages calculation, filing a complaint.
description_zh: 知识产权民事诉讼：管辖确定、诉前/诉中行为保全（禁令）与财产/证据保全、起诉与举证、损害赔偿计算（实际损失/侵权获利/许可费合理倍数/法定赔偿、恶意侵权惩罚性赔偿）、一审二审程序。
description_en: 'IP civil litigation: jurisdiction, pre-trial/in-trial injunctions and property/evidence preservation, pleading and proof, damages calculation (actual loss / infringer''s profit / reasonable multiple of license fee / statutory damages, plus punitive damages for wilful infringement), and first/second-instance procedure.'
version: 1.0.0
author: SamjoeYang - 上海不丁网络科技有限公司
license: MIT
agent_created: true
---

# 民事诉讼（S6 主路径）

## Overview

民事诉讼是维权链条中唯一能同时获得"停止侵权+赔偿+确定责任"的路径，也是周期最长、成本最高的路径。本技能按"管辖 → 保全 → 起诉 → 举证 → 赔偿计算 → 程序跟进"组织，输出可直接立案的材料。

## Workflow

1. **管辖确定**：按 `references/litigation-guide.md` 确定管辖法院：
   - 侵权行为地（实施地+结果发生地，信息网络侵权包括服务器/设备所在地、被侵权人住所地）或被告住所地。
   - 专利：发明/实用新型/外观设计的管辖有专门规定（外观一审可基层，发明/实用新型一般中院或指定基层）。
   - 商标/著作权：基层法院为主，重大复杂案件可提级；可关注互联网法院（涉网案件）。
2. **保全策略**（按需，防"赢了官司拿不到钱/证据没了"）：
   - **行为保全（禁令）**：证据证明正在实施或即将实施侵权且不及时制止将受难以弥补损害的，可申请诉前/诉中责令停止行为（商标法、专利法、著作权法、反不正当竞争法均有依据）。
   - **财产保全**：查封、扣押、冻结侵权人财产，防转移；需提供担保。
   - **证据保全**：证据可能灭失或以后难以取得时申请（网页、实物、服务器数据）。
3. **起诉材料**：起诉状（模板见 `assets/complaint-template.md`）+ 证据清单（衔接 S3）+ 权利证明（衔接 S0）+ 主体资格证明。起诉状须明确：当事人、诉讼请求（停止侵权、赔偿、承担维权合理开支、诉讼费）、事实与理由、证据清单。
4. **举证与庭审**：围绕"权利有效+被告实施被控行为+落入保护范围（衔接 S2 比对）+损害数额"组织证据；对被告抗辩（合法来源、现有技术、合理使用等）逐项准备反驳（衔接 S2 抗辩预判）。
5. **赔偿计算**：用 `scripts/damages_calculator.py` 按序计算：
   - 补偿性赔偿基数：实际损失（权利人因侵权减少的销量×单位利润+许可费损失）→ 侵权获利（侵权销量×单位利润，可参考平台销量、评价数）→ 许可使用费合理倍数 → 法定赔偿（商标/专利/著作权上限 500 万元，由法院酌定）。
   - **惩罚性赔偿（主张项，非必得项）**：仅在"故意+情节严重+基数可确定"三项同时满足时方可主张 1–5 倍。实务认定标准高：故意须有明确证据（如通知后仍侵权、假冒注册商标、关系人接触过权利等），情节严重须达司法解释列举情形（再犯、以侵权为业、拒不履行保全、隐匿证据、获利巨大等）。默认按不主张计算；主张时必须在输出中单列并标注"主张金额，存在不被支持的风险"，不得将惩罚性赔偿作为必然可得金额。
   - 合理开支：公证费、律师费、购买费、差旅费按实际票据单列主张；律师费存在被法院酌减支持比例的风险，须向用户提示预期支持率区间（详见 `references/litigation-guide.md` 合理开支要点）。
6. **程序跟进**：立案（7 日内决定）→ 举证期限 → 开庭 → 判决/调解；一审不服 15 日内上诉；二审终审。诉前保全后须在法定期限内起诉。

## Output Standards

- 起诉状诉讼请求必须具体可执行（停止侵权+赔偿+费用），赔偿金额有计算依据（脚本输出+口径说明）。
- 惩罚性赔偿金额一律标注"主张项（非必得）"，并提示需故意+情节严重证据、法院支持存在不确定性；不得将惩罚性赔偿计入"较有把握"的获赔金额。
- 管辖结论给出法律依据与法院名称，不确定时说明备选管辖。
- 保全申请明确"必要性理由+担保安排"，不夸大紧急程度。

## Resources

- `references/litigation-guide.md`：管辖规则、保全要点、程序时限。
- `scripts/damages_calculator.py`：赔偿金额计算脚本。
- `assets/complaint-template.md`：知识产权民事起诉状模板。

## 作者

本技能由 **知产刀客 · SamjoeYang** 设计并维护。
