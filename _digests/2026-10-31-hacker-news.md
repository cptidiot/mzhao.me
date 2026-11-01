---
section: hacker-news
section_name: Hacker News
date: "2026-10-31 21:00:00 -0700"
title: "HN Daily Top 10 — 2026-10-31"
excerpt: "Karpathy 的 HackerTube 以 880 分断层登顶，Linux 内核 9.8 分漏洞与 ChatGPT 账号接管披露分列二、三名。"
items:
  - title: "HackerTube: YouTube built from videos recommended by HN"
    summary: "Karpathy 用 Claude Code 花约两小时搭了一个 YouTube 替代品：片源全部来自 2007–2026 年间 HN 评论里推荐过的视频，共 6,454 条、覆盖 150 个话题，另配无账号的个性化推荐；880 分、278 条评论。"
    stat: "880 分 · 278 评论"
    url: "https://news.ycombinator.com/item?id=50319510"
    time: "10-31 12:56"
    link_label: "HN 讨论"
  - title: "TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8"
    summary: "Linux 内核 IPv4 TCP 握手中的 use-after-free 漏洞，CVSS 9.8；上游修复已发布，但截至 10 月 31 日 Ubuntu 与 RHEL 仍无修复，Anthropic 称其模型已写出针对 MPTCP 监听器的远程 root 概念验证；389 分、182 条评论。"
    stat: "389 分 · 182 评论"
    url: "https://news.ycombinator.com/item?id=50319143"
    time: "10-31 12:16"
    link_label: "HN 讨论"
  - title: "Do the math: How we took over ChatGPT accounts"
    summary: "Parameter 的研究披露：攻击者可通过一条普通的公开 ChatGPT 分享链接，在受害者已登录会话中执行 JavaScript、读取私人对话；OpenAI 已于 10 月 26 日修复并定为 P1；311 分、153 条评论。"
    stat: "311 分 · 153 评论"
    url: "https://news.ycombinator.com/item?id=50314699"
    time: "10-31 03:30"
    link_label: "HN 讨论"
  - title: "Anthropic blocks users for anything touching training larger models"
    summary: "一条帖子称，Anthropic 会因用户内容涉及训练更大模型而封禁账号；讨论聚焦封禁边界与申诉空间，帖文说法本身未经 Anthropic 官方证实；247 分、132 条评论。"
    stat: "247 分 · 132 评论"
    url: "https://news.ycombinator.com/item?id=50319358"
    time: "10-31 12:39"
    link_label: "HN 讨论"
  - title: "An Italian farmer found some unknown seeds in his attic and planted them"
    summary: "史密森尼杂志的奇闻：一名意大利农夫在阁楼发现不知名种子，抱着没什么可失去的心态种了下去，结果出乎意料；226 分、65 条评论。"
    stat: "226 分 · 65 评论"
    url: "https://news.ycombinator.com/item?id=50320963"
    time: "10-31 15:41"
    link_label: "HN 讨论"
  - title: "Simple circuits can create complex behaviors"
    summary: "一篇交互式科普：用简单的电路一步步搭出复杂行为，讲清楚复杂系统如何从简单规则里长出来；224 分、69 条评论。"
    stat: "224 分 · 69 评论"
    url: "https://news.ycombinator.com/item?id=50261253"
    time: "10-27 09:01"
    link_label: "HN 讨论"
  - title: "Jepsen: ParticleDB 1.1.4"
    summary: "Jepsen 对分布式数据库 ParticleDB 1.1.4 的一致性分析报告，评论区围绕测试发现与数据库可靠性展开；219 分、122 条评论。"
    stat: "219 分 · 122 评论"
    url: "https://news.ycombinator.com/item?id=50316100"
    time: "10-31 06:39"
    link_label: "HN 讨论"
  - title: "It's the memory latency, stupid"
    summary: "一篇性能主题文章：论点是内存延迟才是真正的瓶颈，提醒优化时别只盯着算力或带宽；153 分、43 条评论。"
    stat: "153 分 · 43 评论"
    url: "https://news.ycombinator.com/item?id=50318720"
    time: "10-31 11:38"
    link_label: "HN 讨论"
  - title: "Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard"
    summary: "一个多模型协作项目：5 个 Qwen3.8-27B 模型组队，在 LiveCodeBench Hard 上击败了 Fable 5，讨论集中在小模型协作能否顶替大模型；121 分、65 条评论。"
    stat: "121 分 · 65 评论"
    url: "https://news.ycombinator.com/item?id=50320995"
    time: "10-31 15:46"
    link_label: "HN 讨论"
  - title: "The Duty of a Scholar"
    summary: "一篇随笔：谈学者应尽的责任，偏观点与自省，适合睡前慢慢读；98 分、29 条评论。"
    stat: "98 分 · 29 评论"
    url: "https://news.ycombinator.com/item?id=50319061"
    time: "10-31 12:07"
    link_label: "HN 讨论"
---

HN Daily Top 10 — 2026-10-31

来源：Hacker News 官方 API｜抓取时间：2026-10-31 21:00 America/Los_Angeles（取当时排名前 30 条，30 条全部核实、无 deleted/dead，按 score 选 Top 10）

### 1. HackerTube: YouTube built from videos recommended by HN

分数 880｜评论 278

Karpathy 用 Claude Code 花约两小时搭了一个 YouTube 替代品：片源全部来自 2007–2026 年间 HN 评论里推荐过的视频，共 6,454 条、覆盖 150 个话题，另配无账号的个性化推荐。

[原文](https://karpathy.bearblog.dev/hacker-tube/) · [HN 讨论](https://news.ycombinator.com/item?id=50319510)

### 2. TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8

分数 389｜评论 182

Linux 内核 IPv4 TCP 握手中的 use-after-free 漏洞，CVSS 9.8；上游修复已发布，但截至 10 月 31 日 Ubuntu 与 RHEL 仍无修复，Anthropic 称其模型已写出针对 MPTCP 监听器的远程 root 概念验证。

[原文](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf) · [HN 讨论](https://news.ycombinator.com/item?id=50319143)

### 3. Do the math: How we took over ChatGPT accounts

分数 311｜评论 153

Parameter 的研究披露：攻击者可通过一条普通的公开 ChatGPT 分享链接，在受害者已登录会话中执行 JavaScript、读取私人对话；OpenAI 已于 10 月 26 日修复并定为 P1。

[原文](https://www.parameter.ai/labs/we-found-a-gap-at-openai) · [HN 讨论](https://news.ycombinator.com/item?id=50314699)

### 4. Anthropic blocks users for anything touching training larger models

分数 247｜评论 132

一条帖子称，Anthropic 会因用户内容涉及训练更大模型而封禁账号；讨论聚焦封禁边界与申诉空间，帖文说法本身未经 Anthropic 官方证实。

[原文](https://twitter.com/jiahaoshao1/status/2116475922190922088) · [HN 讨论](https://news.ycombinator.com/item?id=50319358)

### 5. An Italian farmer found some unknown seeds in his attic and planted them

分数 226｜评论 65

史密森尼杂志的奇闻：一名意大利农夫在阁楼发现不知名种子，抱着没什么可失去的心态种了下去，结果出乎意料。

[原文](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/) · [HN 讨论](https://news.ycombinator.com/item?id=50320963)

### 6. Simple circuits can create complex behaviors

分数 224｜评论 69

一篇交互式科普：用简单的电路一步步搭出复杂行为，讲清楚复杂系统如何从简单规则里长出来。

[原文](https://aatishb.com/myriad/lets-build-a-brain/) · [HN 讨论](https://news.ycombinator.com/item?id=50261253)

### 7. Jepsen: ParticleDB 1.1.4

分数 219｜评论 122

Jepsen 对分布式数据库 ParticleDB 1.1.4 的一致性分析报告，评论区围绕测试发现与数据库可靠性展开。

[原文](https://jepsen.io/analyses/particledb-1.1.4) · [HN 讨论](https://news.ycombinator.com/item?id=50316100)

### 8. It's the memory latency, stupid

分数 153｜评论 43

一篇性能主题文章：论点是内存延迟才是真正的瓶颈，提醒优化时别只盯着算力或带宽。

[原文](https://pivotlake.io/blog/its-the-memory-latency-stupid/) · [HN 讨论](https://news.ycombinator.com/item?id=50318720)

### 9. Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard

分数 121｜评论 65

一个多模型协作项目：5 个 Qwen3.8-27B 模型组队，在 LiveCodeBench Hard 上击败了 Fable 5，讨论集中在小模型协作能否顶替大模型。

[原文](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve) · [HN 讨论](https://news.ycombinator.com/item?id=50320995)

### 10. The Duty of a Scholar

分数 98｜评论 29

一篇随笔：谈学者应尽的责任，偏观点与自省，适合睡前慢慢读。

[原文](https://www.daemonology.net/blog/2026-10-31-The-Duty-of-a-Scholar.html) · [HN 讨论](https://news.ycombinator.com/item?id=50319061)

趋势观察：今日榜单安全主线突出——Linux 内核 9.8 分漏洞与 ChatGPT 分享链接接管账号分列第 2、3 名；与此同时，Karpathy 的 HackerTube 以 880 分断层登顶，AI 辅助“一人造产品”仍是社区最热的话题。
