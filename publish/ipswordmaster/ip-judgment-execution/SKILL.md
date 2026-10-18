---
name: ip-judgment-execution
display_name: 裁判执行与监测
display_name_en: IP Judgment Execution & Monitoring
description: 知识产权裁判执行与复发监测：申请强制执行（金钱给付/停止侵权）、执行异议与追加被执行人、拒不执行处置（限高/失信/罚款拘留/拒不执行判决裁定罪）、维权复盘与重复侵权监测闭环。当用户需要"申请执行""判决后怎么拿到钱""对方不履行""被执行人转移财产""防止再次侵权"时使用。Also usable in English when the user mentions IP judgment enforcement, executing a ruling, contempt of court, recurring-infringement monitoring.
description_zh: 知识产权裁判执行与复发监测：申请强制执行（金钱给付/停止侵权）、执行异议与追加被执行人、拒不执行处置（限高/失信/罚款拘留/拒执罪）、维权复盘与重复侵权监测闭环。
description_en: 'IP judgment enforcement and recurrence monitoring: applies for compulsory execution (monetary payment / cessation of infringement), handles execution objections and adding judgment debtors, addresses non-compliance (travel restriction, dishonesty listing, fines/detention, contempt of court), and closes the loop with case review and repeat-infringement monitoring.'
version: 1.0.1
author: SamjoeYang - 上海不丁网络科技有限公司
license: MIT
agent_created: true
---

# 判决执行与复发监测（S8）

## Overview

判决/裁决/行政处罚决定只是"纸面权利"，执行才是落袋。本技能覆盖执行申请、财产线索、拒不执行应对，以及"执行完防止再犯"的监测闭环。

## Workflow

1. **执行依据与期限**：明确可执行依据（生效民事判决/调解书、行政裁决书、仲裁裁决、公证债权文书等）。申请执行期间一般为 **2 年**（自法律文书规定履行期间最后一日起算）；逾期可能无法启动强制执行。
2. **申请执行**：向第一审法院（或同级被执行的财产所在地法院）提交执行申请：
   - 执行申请书（申请人/被执行人信息、执行依据、请求执行内容）。
   - 生效法律文书及送达证明。
   - 被执行人财产线索（银行账户、房产、车辆、股权、应收账款、知识产权许可收益、电商店铺资金等）。
   - 执行依据内容需明确（金钱数额/停止行为/交付财产），不明确的先申请执行异议或补正。
3. **财产查控与追加**：
   - 法院依职权网络查控（银行存款、不动产、车辆、证券、网络资金）。
   - 权利人补充线索：被执行人电商店铺结算账户、平台资金、境外资产（配合跨境执行）。
   - 符合法定情形时申请追加被执行人（如一人公司股东、未实缴出资股东等，视执行依据与公司法规定）。
4. **拒不执行应对**：按 `execution-guide.md`：
   - 申请纳入失信被执行人名单（老赖名单）、限制高消费（限高）。
   - 对转移/隐匿财产行为：申请罚款、拘留；涉嫌拒不执行判决、裁定罪的，向法院/公安移送追究刑事责任。
   - 执行异议（案外人异议、执行行为异议）与执行监督程序按需使用。
5. **执行到账与结案**：执行款到账核对（本金+迟延履行利息+执行费）；确认执行完毕或终本（终结本次执行）程序，保留恢复执行权利。
6. **复发监测闭环**：执行完毕后回到 S0/S1 持续监测：
   - 盯侵权人是否换马甲（新店铺、新公司、关联主体）再犯。
   - 再犯证据固定后，可主张重复侵权加重赔偿/请求法院从重处理，或再次行政/刑事维权。

## Output Standards

- 执行申请材料逐项核对，执行依据与履行期说明准确。
- 明确提示 2 年申请执行期间，过期风险不得淡化。
- 财产线索按"已掌握/需调查"区分，不编造财产状况。

## Resources

- `execution-guide.md`：执行流程、强制措施、拒不执行处置与恢复执行要点。

## 作者

本技能由 **知产刀客 · SamjoeYang** 设计并维护。
