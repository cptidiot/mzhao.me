---
section: hacker-news
section_name: Hacker News
date: "2026-11-05 21:00:00 -0800"
title: "HN Daily Top 10 — 2026-11-05"
excerpt: "OpenSSH musl 密码绕过 sshole 以 2465 分登顶；Claude Code 被曝在 User-Agent 里泄露邮箱地址；Salon 宣布停刊。"
items:
  - title: "sshole"
    summary: "OpenSSH 在 musl Linux（Alpine、OpenWrt 等）上存在密码认证绕过：本应永不接受密码的账号（如 root、仅密钥登录的部署账号），输入超过 256 字符的任意密码即可登录。问题根源可追溯到 2016 年，Alpine 已发布相关说明，OpenSSH 10.6p2 亦有修复说明；2465 分、604 条评论。"
    stat: "2465 分 · 604 评论"
    url: "https://news.ycombinator.com/item?id=50378228"
    time: "11-05 04:19"
    link_label: "HN 讨论"
  - title: "Claude Code sends your email address to websites"
    summary: "用户报告 Claude Code 在联网搜索时把邮箱地址放进 User-Agent 请求头，发送给任意第三方网站，引发隐私争议；发帖者认为这不应是可开关的选项，而应彻底移除；750 分、255 条评论。"
    stat: "750 分 · 255 评论"
    url: "https://news.ycombinator.com/item?id=50385272"
    time: "11-05 14:17"
    link_label: "HN 讨论"
  - title: "Search for everyone"
    summary: "付费搜索引擎 Kagi 宣布亲友也可试用 Kagi（11 月 5 日更新日志），降低了体验门槛；讨论围绕 Kagi 的付费模式与免费试用范围展开；603 分、313 条评论。"
    stat: "603 分 · 313 评论"
    url: "https://news.ycombinator.com/item?id=50383740"
    time: "11-05 12:03"
    link_label: "HN 讨论"
  - title: "Goodbye from Salon"
    summary: "创刊 31 年的美国网络杂志 Salon 宣布停刊，2026 年 11 月 5 日发布告别信，为这家老牌网络媒体画上句号；513 分、184 条评论。"
    stat: "513 分 · 184 评论"
    url: "https://news.ycombinator.com/item?id=50383739"
    time: "11-05 12:03"
    link_label: "HN 讨论"
  - title: "Motorola Signature 27 with GrapheneOS support"
    summary: "摩托罗拉发布新旗舰 Motorola Signature 27，号称 2026 年 DXOMARK 评分最高的手机相机系统；据帖子介绍该机支持注重隐私的 GrapheneOS，引发不少讨论；427 分、317 条评论。"
    stat: "427 分 · 317 评论"
    url: "https://news.ycombinator.com/item?id=50380810"
    time: "11-05 08:01"
    link_label: "HN 讨论"
  - title: "MS Paint Remote Code Execution Vulnerability"
    summary: "微软画图（MS Paint）被曝远程代码执行漏洞，编号 CVE-2026-83844，详情见 CVE 记录；394 分、146 条评论。"
    stat: "394 分 · 146 评论"
    url: "https://news.ycombinator.com/item?id=50384233"
    time: "11-05 12:43"
    link_label: "HN 讨论"
  - title: "I wish tech companies knew more about me"
    summary: "作者吐槽科技公司的“监视”与个性化名不副实：买了床垫就反复推床垫、音乐推荐总推他会跳过的电子乐，数据收集很多，真正懂用户却很少；348 分、305 条评论。"
    stat: "348 分 · 305 评论"
    url: "https://news.ycombinator.com/item?id=50378942"
    time: "11-05 05:40"
    link_label: "HN 讨论"
  - title: "Download your favourite YouTube videos"
    summary: "作者呼吁把喜欢的 YouTube 视频下载存档，别等视频下架或频道消失才后悔，并给出实操思路；309 分、143 条评论。"
    stat: "309 分 · 143 评论"
    url: "https://news.ycombinator.com/item?id=50378571"
    time: "11-05 05:00"
    link_label: "HN 讨论"
  - title: "Window Sweaters"
    summary: "一款 macOS 小应用，给窗口加上针织毛衣风格的彩色边框，让桌面更温馨；支持 Homebrew 安装；275 分、90 条评论。"
    stat: "275 分 · 90 评论"
    url: "https://news.ycombinator.com/item?id=50381383"
    time: "11-05 08:50"
    link_label: "HN 讨论"
  - title: "MCP Explained"
    summary: "一份交互式教程，用图解讲清 Model Context Protocol（MCP）的工作方式：Host、Server 与模型之间如何分工、消息如何流转，适合想系统了解 MCP 的读者；270 分、117 条评论。"
    stat: "270 分 · 117 评论"
    url: "https://news.ycombinator.com/item?id=50379249"
    time: "11-05 06:08"
    link_label: "HN 讨论"
---

HN Daily Top 10 — 2026-11-05

来源：Hacker News 官方 API｜抓取时间：2026-11-05 约 21:00 America/Los_Angeles（取当时排名前 30 条，全部核实、无 deleted/dead，按 score 选 Top 10）

### 1. sshole

分数 2465｜评论 604

OpenSSH 在 musl Linux（Alpine、OpenWrt 等）上存在密码认证绕过：本应永不接受密码的账号（如 root、仅密钥登录的部署账号），输入超过 256 字符的任意密码即可登录。问题根源可追溯到 2016 年，Alpine 已发布相关说明，OpenSSH 10.6p2 亦有修复说明。

[原文](https://sshhole.com) · [HN 讨论](https://news.ycombinator.com/item?id=50378228)

### 2. Claude Code sends your email address to websites

分数 750｜评论 255

用户报告 Claude Code 在联网搜索时把邮箱地址放进 User-Agent 请求头，发送给任意第三方网站，引发隐私争议；发帖者认为这不应是可开关的选项，而应彻底移除。

[原文](https://github.com/anthropics/claude-code/issues/107757) · [HN 讨论](https://news.ycombinator.com/item?id=50385272)

### 3. Search for everyone

分数 603｜评论 313

付费搜索引擎 Kagi 宣布亲友也可试用 Kagi（11 月 5 日更新日志），降低了体验门槛；讨论围绕 Kagi 的付费模式与免费试用范围展开。

[原文](https://kagi.com/changelog#11820) · [HN 讨论](https://news.ycombinator.com/item?id=50383740)

### 4. Goodbye from Salon

分数 513｜评论 184

创刊 31 年的美国网络杂志 Salon 宣布停刊，2026 年 11 月 5 日发布告别信，为这家老牌网络媒体画上句号。

[原文](https://www.salon.com/2026/11/05/goodbye-from-salon/) · [HN 讨论](https://news.ycombinator.com/item?id=50383739)

### 5. Motorola Signature 27 with GrapheneOS support

分数 427｜评论 317

摩托罗拉发布新旗舰 Motorola Signature 27，号称 2026 年 DXOMARK 评分最高的手机相机系统；据帖子介绍该机支持注重隐私的 GrapheneOS，引发不少讨论。

[原文](https://motorolanews.com/motorola-signature-27-2/) · [HN 讨论](https://news.ycombinator.com/item?id=50380810)

### 6. MS Paint Remote Code Execution Vulnerability

分数 394｜评论 146

微软画图（MS Paint）被曝远程代码执行漏洞，编号 CVE-2026-83844，详情见 CVE 记录。

[原文](https://www.cve.org/CVERecord?id=CVE-2026-83844) · [HN 讨论](https://news.ycombinator.com/item?id=50384233)

### 7. I wish tech companies knew more about me

分数 348｜评论 305

作者吐槽科技公司的“监视”与个性化名不副实：买了床垫就反复推床垫、音乐推荐总推他会跳过的电子乐，数据收集很多，真正懂用户却很少。

[原文](https://rakhim.exotext.com/i-wish-tech-companies-knew-more-about-me) · [HN 讨论](https://news.ycombinator.com/item?id=50378942)

### 8. Download your favourite YouTube videos

分数 309｜评论 143

作者呼吁把喜欢的 YouTube 视频下载存档，别等视频下架或频道消失才后悔，并给出实操思路。

[原文](https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/) · [HN 讨论](https://news.ycombinator.com/item?id=50378571)

### 9. Window Sweaters

分数 275｜评论 90

一款 macOS 小应用，给窗口加上针织毛衣风格的彩色边框，让桌面更温馨；支持 Homebrew 安装。

[原文](https://github.com/saragordic/window-sweaters) · [HN 讨论](https://news.ycombinator.com/item?id=50381383)

### 10. MCP Explained

分数 270｜评论 117

一份交互式教程，用图解讲清 Model Context Protocol（MCP）的工作方式：Host、Server 与模型之间如何分工、消息如何流转，适合想系统了解 MCP 的读者。

[原文](https://mcp-explained.com/) · [HN 讨论](https://news.ycombinator.com/item?id=50379249)

趋势观察：本期安全与隐私话题占了半壁江山——OpenSSH 绕过、Claude Code 泄露邮箱、画图 RCE 三条都与安全相关，另有两条在反思科技公司对用户数据的理解，隐私议题热度明显。
