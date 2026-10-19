---
section: ai-builders
section_name: AI Builders
date: 2026-10-18 09:00:00 -0700
title: "AI Builders Digest — 2026-10-18"
excerpt: "Aaron Levie 谈「软件工程终结论」为何是最大误读等，24 小时内 15 条开发者观点精选。"
items:
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "他认为“软件工程将终结”是最大的误读：世界需要的软件量并没有固定上限。agent 能用工具、操作电脑、即时写软件并高速处理数据之后，过去无法数字化的工作也在被“软件化”，结果是工程在经济中的重要性不降反升——银行的新交易形态、生命科学的实验室工作、制造业的供应链自动化，都在变成工程问题。手动编码会消失，但“几乎一切都会是代码”，懂代码的人位置反而更好。"
    url: "https://x.com/levie/status/2111525362446520466"
    link_label: "X 原帖"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "他澄清自己在 TC Disrupt 的发言：Replit 仍然 model agnostic，用户可以选用 Anthropic 等多家模型；但 OpenAI 已成为驱动其 Agent 的 preferred partner，依据是性能、成本与合作关系强弱。Replit 的策略是保留用户的模型选择权，同时把默认体验优化到最佳性能与价格。"
    url: "https://x.com/amasad/status/2111494912562888939"
    link_label: "X 原帖"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "他分享了一个多 agent 协同办真实事务的案例：他的工作 agent“Burger”按他个人 agent“Dorito”的请求、通过 email 协调拿到文档，再与他的 CPA 对接处理报税事项，全程约 20 分钟。他的评论是 “We're still so early”——跨工作与个人边界的 agent 协作还很早期，但已经能跑通完整的现实流程。"
    url: "https://x.com/thsottiaux/status/2111495392559067199"
    link_label: "X 原帖"
  - title: "Peter Yang"
    role: "AI 教程与访谈作者"
    summary: "① 他给出一条审计 Google 账号连接的 prompt，针对的正是 agent 接入泛滥后的权限卫生：他自己连了 45 个 app/agent，prompt 要求逐一审查每个连接、区分“仅用 Google 登录”与 Gmail/Drive/Calendar 等数据权限、标出过宽权限与陌生提供方，先给建议、经本人明确批准才断开，最后验证确已移除。② 他评价 Claude Code app 现在明显更快、甚至比 ChatGPT 更简单易用，仍缺的是更好的 browser/computer use、覆盖所有 thread 的 remote control 和 live voice。"
    url: "https://x.com/petergyang/status/2111508293818671449"
    link_label: "X 原帖"
  - title: "Swyx"
    role: "Latent Space / AI Engineer"
    summary: "他公开了其开发者内容频道的观众数据：自今年 5 月以来每月超过 100 万 unique viewers，但 58% 是新观众、68% 没有订阅；观众集中在 PT 上午 7–11 点、下午 5 点后基本无人观看；流量是靠浏览推荐在约两年冷启动后慢慢起来的，而 CTR 依然很差。对做 AI 开发者内容的人，这是一份少见的发行侧现实数据。"
    url: "https://x.com/swyx/status/2111350966419411070"
    link_label: "X 原帖"
  - title: "The MAD Podcast with Matt Turck — What Happens When Billions of AI Agents Hit Your Database? (Andy Pavlo)（2026-10-08 发布；说明：本期是播客 feed 14 天回看窗口内本轮首次出现、此前未报告过的条目，不是今日新发布）"
    summary: "CMU 数据库教授、刚加入 ClickHouse 创立 ClickHouse Labs 的 Andy Pavlo 谈 agent 时代的数据库。agent 如今会创建、分支甚至删除数据库：branching（copy-on-write 快照）让 agent 在真实数据的副本上试错而不碰生产库；每月都有 agent 误删生产库的事故，但防护并无新意——权限与沙箱等老式 guardrails 本就存在，问题在人们把生产密码直接交给 agent。他用 dbdb.io 每晚追踪开源数据库的 commits，发现超过 60% 的开源数据库系统已有 agent 提交。vector search 已成 table stakes，专业向量库只能靠极致性价比或长成通用系统生存。LLM 约 15 分钟就能把数据库调优做到 80–85%，传统 DBA 的调参会被自动化，但 data modeling 与理解系统内部仍需要人。市场层面 OLAP 与 OLTP 正在汇合：先做分析、再补 Postgres 供给（ClickHouse、Databricks 收购 Neon）是他看好的路径。 --- 内容来源：Follow Builders — <https://github.com/zarazhangrui/follow-builders>"
    url: "https://www.youtube.com/@DataDrivenNYC/videos"
    link_label: "节目页"
---

日期：2026-10-18（America/Los_Angeles）
Feed 更新时间：X feed 生成于 2026-10-18T06:38:12Z（洛杉矶 10-17 23:38），博客 feed 生成于 2026-10-18T06:38:50Z，播客 feed 生成于 2026-10-18T06:38:49Z，均为本次运行前约 9.5 小时内的新 feed，不是旧内容冒充今日新闻。X 窗口为最近 24 小时（lookback 24 小时，共 15 条），以下条目均未在往期日报报告过。

## X 开发者观点

**Aaron Levie（CEO @ Box）**
他认为“软件工程将终结”是最大的误读：世界需要的软件量并没有固定上限。agent 能用工具、操作电脑、即时写软件并高速处理数据之后，过去无法数字化的工作也在被“软件化”，结果是工程在经济中的重要性不降反升——银行的新交易形态、生命科学的实验室工作、制造业的供应链自动化，都在变成工程问题。手动编码会消失，但“几乎一切都会是代码”，懂代码的人位置反而更好。
[X 原帖](https://x.com/levie/status/2111525362446520466)

**Amjad Masad（CEO @ Replit）**
他澄清自己在 TC Disrupt 的发言：Replit 仍然 model agnostic，用户可以选用 Anthropic 等多家模型；但 OpenAI 已成为驱动其 Agent 的 preferred partner，依据是性能、成本与合作关系强弱。Replit 的策略是保留用户的模型选择权，同时把默认体验优化到最佳性能与价格。
[X 原帖](https://x.com/amasad/status/2111494912562888939)

**Thibault Sottiaux（Codex & ChatGPT @ OpenAI）**
他分享了一个多 agent 协同办真实事务的案例：他的工作 agent“Burger”按他个人 agent“Dorito”的请求、通过 email 协调拿到文档，再与他的 CPA 对接处理报税事项，全程约 20 分钟。他的评论是 “We're still so early”——跨工作与个人边界的 agent 协作还很早期，但已经能跑通完整的现实流程。
[X 原帖](https://x.com/thsottiaux/status/2111495392559067199)

**Peter Yang（AI 教程与访谈作者）**
① 他给出一条审计 Google 账号连接的 prompt，针对的正是 agent 接入泛滥后的权限卫生：他自己连了 45 个 app/agent，prompt 要求逐一审查每个连接、区分“仅用 Google 登录”与 Gmail/Drive/Calendar 等数据权限、标出过宽权限与陌生提供方，先给建议、经本人明确批准才断开，最后验证确已移除。② 他评价 Claude Code app 现在明显更快、甚至比 ChatGPT 更简单易用，仍缺的是更好的 browser/computer use、覆盖所有 thread 的 remote control 和 live voice。
[X 原帖](https://x.com/petergyang/status/2111508293818671449)
[X 原帖](https://x.com/petergyang/status/2111496600522805624)

**Swyx（Latent Space / AI Engineer）**
他公开了其开发者内容频道的观众数据：自今年 5 月以来每月超过 100 万 unique viewers，但 58% 是新观众、68% 没有订阅；观众集中在 PT 上午 7–11 点、下午 5 点后基本无人观看；流量是靠浏览推荐在约两年冷启动后慢慢起来的，而 CTR 依然很差。对做 AI 开发者内容的人，这是一份少见的发行侧现实数据。
[X 原帖](https://x.com/swyx/status/2111350966419411070)
[X 原帖](https://x.com/swyx/status/2111353401363902573)

其余 X 条目多为无内容短帖、玩笑或私人动态（如 “Done”“Landing sometime today”、前端框架怀旧转发、一句引言转发、VC 轮次段子、StarCraft 玩笑），已按规则过滤。

## 官方博客

本次 feed-blogs.json（generatedAt 2026-10-18T06:38:50Z，lookback 72 小时）条目为 0，没有新的官方博客公告可报告。

## 播客

**The MAD Podcast with Matt Turck — What Happens When Billions of AI Agents Hit Your Database? (Andy Pavlo)（2026-10-08 发布；说明：本期是播客 feed 14 天回看窗口内本轮首次出现、此前未报告过的条目，不是今日新发布）**
CMU 数据库教授、刚加入 ClickHouse 创立 ClickHouse Labs 的 Andy Pavlo 谈 agent 时代的数据库。agent 如今会创建、分支甚至删除数据库：branching（copy-on-write 快照）让 agent 在真实数据的副本上试错而不碰生产库；每月都有 agent 误删生产库的事故，但防护并无新意——权限与沙箱等老式 guardrails 本就存在，问题在人们把生产密码直接交给 agent。他用 dbdb.io 每晚追踪开源数据库的 commits，发现超过 60% 的开源数据库系统已有 agent 提交。vector search 已成 table stakes，专业向量库只能靠极致性价比或长成通用系统生存。LLM 约 15 分钟就能把数据库调优做到 80–85%，传统 DBA 的调参会被自动化，但 data modeling 与理解系统内部仍需要人。市场层面 OLAP 与 OLTP 正在汇合：先做分析、再补 Postgres 供给（ClickHouse、Databricks 收购 Neon）是他看好的路径。
节目页：[节目页](https://www.youtube.com/@DataDrivenNYC/videos)

---
内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
