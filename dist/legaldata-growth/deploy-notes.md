# 部署须知：sitemap.xml / robots.txt 必须为真静态文件

## 现状问题
当前访问 `https://legaldata.zhenzhidaole.com/sitemap.xml` 与 `/robots.txt`，服务器返回的是 **SPA 的 HTML 外壳**（`<title>司法资源工具</title>` + `<div id="root">`），并非真正的站点地图/爬虫协议。原因是前端路由的 catch-all 把未知路径都兜底成了 `index.html`。

→ 后果：搜索引擎抓不到任何工具页 URL，本交付的 sitemap 等于没用。

## 修复方式（二选一）

### A. 静态托管（推荐，最简单）
把本目录的 `sitemap.xml` 和 `robots.txt` 放到**网站根目录的静态文件区**，并确保它们**不被 SPA catch-all 拦截**（优先于 index.html 命中）。

- **Nginx**：
  ```nginx
  location = /sitemap.xml { root /var/www/legaldata; }
  location = /robots.txt  { root /var/www/legaldata; }
  # 其余走 SPA
  location / { try_files $uri $uri/ /index.html; }
  ```
- **Vercel / Netlify**：把这两个文件放在 `public/` 或 `static/` 根，平台会优先返回静态文件。
- **对象存储 + CDN**：上传到桶根，配置为公开可读。

### B. 后端动态生成
若站点有后端，在 `/sitemap.xml`、`/robots.txt` 路由直接返回 `application/xml` / `text/plain` 内容，绕开前端兜底。

## 上线后必做
1. 浏览器直接访问 `https://legaldata.zhenzhidaole.com/sitemap.xml`，确认返回的是 XML（不是 HTML）。
2. 到 **百度搜索资源平台** 与 **Google Search Console** 提交 sitemap。
3. 在站长平台用"抓取诊断/URL 检查"验证工具页可被正常抓取与索引。
4. 各路由补好 `seo-meta-checklist.md` 里的 title/description 后再提交，效果最佳。

## 验证命令（本地）
```bash
curl -s -H "Accept: application/xml" https://legaldata.zhenzhidaole.com/sitemap.xml | head -c 200
# 应看到 <?xml ...><urlset ...>，而不是 <!doctype html>
```
