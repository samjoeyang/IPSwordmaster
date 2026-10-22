# SEO Meta 清单（legaldata.zhenzhidaole.com）

> 用途：交给前端，给每个路由补 `title` / `meta description` / `keywords` / OG 标签。
> 当前状态：全站仅有动态 `<title>`（`Mt(i)` 已按路由设置），但**缺 description、keywords、OG**，且 `/sitemap.xml`、`/robots.txt` 返回的是 SPA 外壳（见 `sitemap.xml` / `robots.txt` 两份交付文件）。
> 合规底线：标题/描述**不得**出现"最佳/第一/包赢/100%成功"等绝对化用语；描述中保留"不构成正式法律意见"或"仅供参考"的弱免责表述。

## 接入方式（React Router + Vite SPA）

```tsx
// 建议用 react-helmet-async 或路由级 <Helmet>
<Helmet>
  <title>{meta.title}</title>
  <meta name="description" content={meta.description} />
  <meta name="keywords" content={meta.keywords} />
  <meta property="og:title" content={meta.title} />
  <meta property="og:description" content={meta.description} />
  <meta property="og:type" content="website" />
  <meta property="og:url" content={`https://legaldata.zhenzhidaole.com${path}`} />
  <link rel="canonical" href={`https://legaldata.zhenzhidaole.com${path}`} />
</Helmet>
```

## 各页面建议

| 路由 | title | meta description | keywords |
|---|---|---|---|
| `/` | 司法资源工具 \| 公共法律服务一站式入口 | 律师/律所/公证/司法鉴定查询，商标分类、案由查询、诉讼费与社保测算，IP/婚姻/公司/税务/劳动风险免费自测，找法用法一步到位。 | 公共法律服务,法律工具,律师查询,诉讼费计算,商标分类,案由查询 |
| `/ip-risk-diagnosis` | IP风险自测 \| 商标专利著作权侵权初步诊断 | 免费自助初筛商标、专利、著作权侵权风险，给出阶段性诊断与行动路线建议，结果仅供参考、不构成正式法律意见。 | IP风险自测,侵权诊断,商标侵权,专利维权,著作权 |
| `/divorce-diagnosis` | 离婚风险自测 \| 财产分割与抚养权初步诊断 | 免费自助评估离婚中的财产分割、抚养权、债务等风险，给出行动建议，结果仅供参考、不构成正式法律意见。 | 离婚风险,财产分割,抚养权,离婚自测 |
| `/company-risk-diagnosis` | 公司法律风险自测 \| 股权合同合规初步诊断 | 免费自助评估公司股权、合同、用工等常见法律风险，给出阶段性诊断与行动路线。 | 公司法律风险,股权,合同合规,企业法务 |
| `/tax-risk-diagnosis` | 税务风险自测 \| 个税企税发票合规初步诊断 | 免费自助评估个税、企税、发票等税务合规风险，给出风险提醒与行动建议。 | 税务风险,个税,发票合规,逃税风险 |
| `/labor-risk-diagnosis` | 劳动用工风险自测 \| 劳动合同社保合规诊断 | 免费自助评估劳动合同、社保、工伤等用工风险，给出行动路线建议。 | 劳动风险,劳动合同,社保合规,工伤 |
| `/fee` | 诉讼费计算器 \| 法院案件受理费测算 | 在线测算财产/非财产案件诉讼费、保全费，输入标的额即刻得出预估费用。 | 诉讼费计算,案件受理费,法院收费,保全费 |
| `/social-insurance-calculator` | 社保计算器 \| 五险缴费基数与金额测算 | 按城市与缴费基数测算养老、医疗、失业、工伤、生育保险的缴费金额。 | 社保计算,五险,缴费基数,社保计算器 |
| `/lawyer` | 律师查询 \| 找执业律师 | 查询执业律师信息，快速找到对应专业领域的律师。 | 律师查询,找律师,执业律师 |
| `/firm` | 律所查询 \| 找律师事务所 | 查询律师事务所信息，按地域与专业领域筛选。 | 律所查询,律师事务所,找律所 |
| `/notary` | 公证机构查询 \| 找公证处 | 查询公证机构与公证事项指引，办理公证前先了解。 | 公证,公证处,公证查询 |
| `/appraisal` | 司法鉴定查询 \| 找鉴定机构 | 查询司法鉴定机构与鉴定范围。 | 司法鉴定,鉴定机构,法医鉴定 |
| `/aid` | 法律援助查询 \| 申请条件与机构 | 查询法律援助申请条件与就近援助机构。 | 法律援助,法援,免费法律帮助 |
| `/mediation` | 人民调解查询 \| 找调解组织 | 查询人民调解组织与调解流程。 | 人民调解,调解,纠纷化解 |
| `/legal-service` | 法律服务导航 \| 公共法律服务机构 | 一站式导航律师、公证、鉴定、法援、调解等公共法律服务机构。 | 法律服务,公共法律,机构导航 |
| `/arbitration` | 仲裁机构查询 \| 找仲裁委员会 | 查询仲裁委员会与仲裁流程指引。 | 仲裁,仲裁委员会,商事仲裁 |
| `/judicial` | 司法所查询 \| 基层司法服务 | 查询司法所地址与基层公共法律服务事项。 | 司法所,基层司法,公共法律 |
| `/public-service` | 公共法律服务 \| 一站式入口 | 公共法律服务资源总入口，覆盖咨询、查询、自测。 | 公共法律服务,法律咨询,法律服务 |
| `/trademark-class` | 商标分类查询 \| 45类商标类别一览 | 查询商标注册用商品与服务国际分类（45类），定位你的商标类别。 | 商标分类,商标类别,45类商标 |
| `/cause-of-action` | 案由查询 \| 民事行政刑事案由对照 | 查询民事、行政、刑事案件案由，辅助判断纠纷性质。 | 案由查询,民事案件案由,刑事案由 |
| `/fayan-fayu` | 法言法语 \| 法律术语通俗解读 | 把晦涩法律术语翻译成大白话，读懂合同与文书。 | 法言法语,法律术语,法律名词解释 |

## 额外建议（提升抓取与点击）

1. **结构化数据（JSON-LD）**：对 `/fee`、`/social-insurance-calculator`、`/trademark-class` 等工具页加 `SoftwareApplication` 或 `HowTo` 类型，争取搜索结果富媒体展示。
2. **百度适配**：纯 JS SPA 对百度抓取不友好。若中文流量为主，建议对工具页做**预渲染（prerender）或 SSR**，或至少保证 sitemap 可被百度站长平台提交。
3. **提交入口**：上线后到 **百度搜索资源平台** 与 **Google Search Console** 分别提交 sitemap.xml。
4. **内链**：在科普文章页（若后续建站内含文章）用锚文本互链到对应工具，提升权重与停留。
