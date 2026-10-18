---
name: ip-cross-border-enforcement
display_name: 跨境知识产权维权
display_name_en: Cross-border IP Enforcement
description: 知识产权跨境维权：中国出口环节海关保护、境外电商平台投诉（Amazon Brand Registry/eBay VeRO/AliExpress/TikTok Shop/Wish等）、境外侵权排查与行政司法救济（美国 ITC 337 调查、海外诉讼/仲裁、国际展会维权）、以及马德里商标/PCT 专利国际布局与跨境证据（公证认证、翻译）衔接。当用户需要"海外被仿冒怎么办""亚马逊上有人卖假货""货物出口被扣""337调查""跨境维权"时使用。Also usable in English when the user mentions cross-border IP enforcement, Amazon/eBay takedown, ITC 337 investigation, overseas litigation, Madrid/PCT layout.
description_zh: 知识产权跨境维权：中国出口环节海关保护、境外电商平台投诉（Amazon Brand Registry/eBay VeRO/AliExpress/TikTok Shop等）、境外侵权排查与行政司法救济（美国 ITC 337 调查、海外诉讼/仲裁、国际展会维权）、以及马德里商标/PCT 专利国际布局与跨境证据衔接。
description_en: 'Cross-border IP enforcement: China export customs protection; overseas e-commerce complaints (Amazon Brand Registry, eBay VeRO, AliExpress, TikTok Shop); offshore infringement investigation and administrative/judicial relief (US ITC Section 337, overseas litigation/arbitration, international trade-fair enforcement); and Madrid/PCT global layout with cross-border evidence coordination.'
version: 1.0.1
author: SamjoeYang - 上海不丁网络科技有限公司
license: MIT
agent_created: true
---

# 跨境维权（贯穿全程）

## Overview

跨境维权横跨"权利布局 → 出口拦截 → 境外平台下架 → 境外行政司法救济"多个环节。核心原则：**先在目标市场有权利（马德里/PCT/当地注册），才能在目标市场维权**。本技能按"布局核查 → 出口环节 → 境外平台 → 境外救济 → 证据衔接"组织。

## Workflow

1. **权利布局核查**：维权前先确认在目标国/地区是否享有对应权利：
   - 商标：马德里国际注册（指定缔约方）或逐一国家注册；美国可基于使用意向申请。
   - 专利：PCT 国际申请进入国家阶段/直接向目标国申请；外观设计海牙体系（如适用）。
   - 著作权：多数国家自动保护（伯尔尼公约），但登记/版权局备案可强化证明（美国版权登记是起诉前提）。
   - 无当地权利则无境外侵权救济基础，先提示布局（衔接 S0 权利清单扩展）。
2. **出口环节拦截**：对中国出口的侵权嫌疑货物：
   - 已做海关备案的（S0/S5）→ 海关依职权中止放行 → 3 个工作日内申请扣留+担保。
   - 未备案 → 向进出境地海关申请依申请扣留。
   - 出口方权利人的注意点：**定牌加工（OEM/ODM）出口**可能被目的国权利人主张侵权，出口前做目的国权属与风险排查（商标/专利/外观）。
3. **境外平台投诉**：按 `references/overseas-platforms.md` 对 Amazon、eBay、AliExpress、TikTok Shop、Wish、Shopify 等平台投诉：
   - Amazon：**Brand Registry 品牌注册**后可提交侵权报告（Report a Violation），配合 Test Buy 购买取证；未注册品牌走普通投诉。
   - eBay：VeRO（Verified Rights Owner）计划，提交产权证明+侵权 listing 链接。
   - AliExpress/全球速卖通：知产投诉系统（身份+权属+链接+初步证据）。
   - TikTok Shop：商家/达人对品牌侵权的举报入口。
   - 各平台流程共性：身份验证、权利证明、侵权链接、初步证据、申诉-反通知。
4. **境外行政与司法救济**：按 `references/overseas-litigation.md` 选择：
   - **美国 ITC 337 调查**：对进口至美国的侵权产品（专利、商标、版权、商业秘密），向美国国际贸易委员会（ITC）申请 337 调查，可获排除令（海关禁止入境），速度快、威慑强。
   - 海外民事诉讼：美国联邦法院专利/商标/版权诉讼（可主张三倍赔偿、律师费）、欧盟/东南亚等当地法院诉讼。
   - 海关行政保护：美国海关 CBP 扣押、欧盟海关行动等。
   - 域名争议：UDRP（统一域名争议解决政策）程序针对境外恶意域名。
5. **国际展会维权**：展会前查展商名录与展品；展会期间请当地执法/展会组织方处理侵权展品（德国等展会禁令制度成熟）；现场公证取证。
6. **证据与程序衔接**：
   - 境外证据：公证认证（如领事认证/海牙认证）、翻译机构翻译。
   - 境内证据涉外使用：公证+翻译；涉诉时按当地程序提交。
   - 与境内维权协同：同一侵权人境内境外同时打击（境内诉讼+境外平台投诉+海关）。

## Output Standards

- 先核查目标市场权利基础，未布局时明确提示"无权利则无法维权，先布局"。
- 境外平台流程按平台当期规则执行，标注"以平台指引为准"，不编造规则细节。
- 区分"已取得当地权利（可维权）"与"未取得（先布局）"。

## Resources

- `references/overseas-platforms.md`：主要境外电商平台投诉机制。
- `references/overseas-litigation.md`：ITC 337、海外诉讼、海关与域名争议要点。

## 作者

本技能由 **知产刀客 · SamjoeYang** 设计并维护。
