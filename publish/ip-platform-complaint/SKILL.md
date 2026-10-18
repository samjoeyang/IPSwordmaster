---
name: ip-platform-complaint
display_name: 电商平台投诉
display_name_en: E-commerce Platform Complaint
description: 电商平台知识产权投诉（通知-删除）与申诉应对——单场景专项技能，只处理平台投诉这一个环节。用于向淘天（淘宝/天猫IPP平台）、京东、拼多多、抖音等平台发起商标/专利/著作权投诉、提交合格通知、跟进平台处理、应对卖家申诉、申请平台小二介入。当用户需要"下架侵权链接""投诉盗图/假货/仿品""平台投诉材料""处理卖家申诉"时使用。Also usable in English when the user mentions e-commerce IP complaint, notice-and-takedown, platform takedown or seller appeal.
description_zh: 单场景专项技能，只做电商平台知识产权投诉（通知-删除）与申诉应对：覆盖淘天（淘宝/天猫IPP）、京东、拼多多、抖音等平台的投诉流程、合格通知四要素、材料准备、提交跟进、卖家申诉应对与平台介入申请。仅聚焦平台投诉环节，不含取证、行政查处、民事诉讼等其他维权环节。
description_en: 'A single-scenario skill focused solely on e-commerce platform IP complaints (notice-and-takedown) and appeal handling: covers complaint workflows for Taobao/Tmall IPP, JD, Pinduoduo and Douyin, the four required elements of a valid notice, evidence preparation, submission tracking, seller-appeal responses and platform escalation. Scoped to the platform-complaint stage only.'
version: 1.0.0
author: SamjoeYang - 上海不丁网络科技有限公司
license: MIT
agent_created: true
---

# 电商平台投诉

## Overview

平台投诉是成本最低、见效最快的维权动作：凭合格"通知"要求平台删除侵权链接（通知-删除机制）。本技能只覆盖平台投诉这一个环节——投诉前评估、材料准备、各平台提交流程、申诉应对与跟进闭环。

## Workflow

1. **投诉前评估**：先确认权利有效性（权利核查环节）与侵权初步证据（证据固定环节），判断侵权类型（商标/专利/著作权/其他），对 A 级线索优先投诉。注意：平台投诉不等于法律确权，投诉失败不影响后续行政/诉讼路径。
2. **准备合格通知**：合格通知需含四项要素（缺一可能被平台/法院认为不合格）：
   - 权利人真实身份信息（个人身份证件/营业执照；委托投诉的另附授权书）。
   - 知识产权权利证明（商标注册证/专利证书及年费凭证/著作权登记或底稿）。
   - 涉嫌侵权商品/服务信息（商品链接、店铺名称、截图）。
   - 初步侵权证据（比对说明、实物照片、公证书/存证）。
   模板见 @complaint-materials.md。
3. **按平台提交**：按 @platform-guides.md 的流程操作：
   - 淘天：注册 IPP 平台 → 身份与权属验证 → 发起投诉（选站点、选权利类型、填链接）→ 提交后平台审核。
   - 京东：京东知识产权维权平台，首次投诉需备份权属信息。
   - 拼多多：知产保护平台，创建投诉账号 → 上传身份+权属材料 → 提供侵权信息 → 平台处理反馈。
   - 抖音/其他：各平台知产投诉入口，流程类似（身份+权属+侵权信息+初步证据）。
4. **跟进与申诉应对**：
   - 平台删除后卖家可申诉（提交不侵权说明/授权证明）。
   - 收到申诉后评估：认可则撤销投诉；不认可则提交反证并申请平台小二/审核介入。
   - 关注平台处理时限，逾期未处理可向平台催办，并保留"已发合格通知"的证据（对后续诉讼中主张平台责任有利）。
5. **记录与升级**：投诉结果（成立/不成立/申诉恢复）记入台账；对反复上架、换店重犯的侵权人，升级走行政查处或民事诉讼路径。

## Output Standards

- 通知材料必须四要素齐备，缺要素时明确提示补齐后再提交。
- 每平台流程按 @platform-guides.md 指引执行，不编造平台规则。
- 投诉全过程留痕（提交时间、单号、平台反馈），用于后续升级维权。

## Resources

- @platform-guides.md：淘天/京东/拼多多等平台投诉流程要点与时限。
- @complaint-materials.md：合格通知/投诉材料模板。

## 作者

本技能由 **知产刀客 · SamjoeYang** 设计并维护。
