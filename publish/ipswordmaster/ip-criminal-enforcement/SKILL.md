---
name: ip-criminal-enforcement
display_name: 刑事维权报案
display_name_en: Criminal IP Enforcement
description: 知识产权刑事维权：假冒注册商标罪、销售假冒注册商标的商品罪、非法制造/销售非法制造的注册商标标识罪、侵犯著作权罪、侵犯商业秘密罪、假冒专利罪的罪名识别、立案标准与报案/自诉流程，以及刑事附带民事赔偿衔接。当用户需要"报案抓仿冒""刑事立案标准""假冒侵权够不够判刑""刑附民索赔"时使用。Also usable in English when the user mentions IP criminal enforcement, counterfeiting crime, criminal complaint, criminal-civil joinder.
description_zh: 知识产权刑事维权：假冒注册商标罪、销售假冒注册商标的商品罪、侵犯著作权罪、侵犯商业秘密罪、假冒专利罪的罪名识别、立案标准与报案/自诉流程，以及刑事附带民事赔偿衔接。
description_en: 'Criminal IP enforcement: identifies the charged offenses (counterfeiting registered trademarks, selling counterfeits, copyright infringement, trade-secret misappropriation, false patent marking), explains filing thresholds and police-report/private-prosecution procedures, and bridges criminal proceedings with ancillary civil compensation.'
version: 1.0.1
author: SamjoeYang - 上海不丁网络科技有限公司
license: MIT
agent_created: true
---

# 刑事维权（S7）

## Overview

刑事路径威慑力最强（可抓人、追赃、判刑），但门槛最高（须达立案追诉标准）且程序不可控。本技能帮助判断"够不够刑事"、准备报案材料、跟进公安立案，并与民事索赔衔接。

## Workflow

1. **罪名识别**：根据行为与权利类型对应罪名，详见 `crimes-and-thresholds.md`：
   - 假冒注册商标罪（未经许可在同一种商品上使用相同商标）。
   - 销售假冒注册商标的商品罪（明知是假冒注册商标商品而销售）。
   - 非法制造、销售非法制造的注册商标标识罪。
   - 侵犯著作权罪（未经许可复制发行/信息网络传播作品、盗版软件等）。
   - 侵犯商业秘密罪（不正当手段获取/披露/使用）。
   - 假冒专利罪（假冒他人专利，情节严重）。
2. **立案标准核对**：对照《刑法》及司法解释的立案追诉标准（非法经营数额/违法所得/复制品数量/造成损失等），判断是否达到；未达标准的明确告知"刑事不立案但可走民事/行政"，不诱导报案。
3. **证据准备**：在 S3 证据包基础上补齐刑事报案材料：
   - 报案书（犯罪事实、时间地点、金额、涉案主体）。
   - 权利证明（注册证/专利证书/著作权登记）与权利有效性证明。
   - 侵权证据（购买实物、公证/存证、销量与金额统计、生产销售链条线索）。
   - 损失/数额证据（用于认定"情节严重"）。
4. **报案与跟进**：
   - 向侵权行为地或犯罪嫌疑人所在地公安机关（经侦/食药环侦）报案。
   - 公安受理后审查，符合条件立案；对不予立案决定可申请复议或向检察院申请立案监督。
   - 权利人对部分罪名也可自诉（如侵犯著作权罪、假冒专利罪"告诉才处理"情形需注意法定例外）。
5. **刑民衔接**：
   - 提起**刑事附带民事诉讼**索赔（限直接物质损失），或待刑事判决后另行民事诉讼。
   - 追缴违法所得、退赔可减少另行执行的困难。
6. **风险提示**：刑事程序不可撤诉可控；报案材料虚假可能反致责任；涉案金额认定需证据支撑，不得夸大。

## Output Standards

- 立案标准核对必须给出具体数额/数量门槛与对应法条，不模糊表述。
- 明确区分"已达到立案标准（可报案）"与"未达到（建议民事/行政）"。
- 报案材料清单逐项核对，突出数额与情节证据。

## Resources

- `crimes-and-thresholds.md`：各罪名、立案追诉标准、报案要点与刑民衔接。

## 作者

本技能由 **知产刀客 · SamjoeYang** 设计并维护。
