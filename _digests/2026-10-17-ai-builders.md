---
section: ai-builders
section_name: AI Builders
date: 2026-10-17 09:00:00 -0700
title: "AI Builders Digest — 2026-10-17"
excerpt: "Aaron Levie 谈递归自我改进飞轮、Boris Cherny 谈 Claude Code Review、Sam Altman 晒 Navier-Stokes 纪念衫等 24 小时内开发者观点精选。"
items:
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "他认为行业已经越过一个门槛：AI 比人更擅长训练模型这件事正在变得现实可行。模型能力超过多数人类工程师、long-running agent 的 harness 与基础设施成熟、可并行调用的 agent 数量大增，三者叠加形成 recursive self-improvement 的飞轮——前沿进步的速度可能远超以往，低估 RSI 的后果是定价错误。"
    url: "https://x.com/levie/status/2111312141609586862"
    link_label: "X 原帖"
  - title: "Boris Cherny"
    role: "Claude @ Anthropic"
    summary: "① 他说自己已经离不开 Claude Code Review：它跑在他所有的 PR 上，能在合入前抓到几乎每一个 bug，这是团队既能快速推进又能抬高质量门槛的“secret sauce”之一。② 他现在用 Claude Slides 做幻灯片，不再像过去那样到处搜 “iphone frame svg” 之类的素材——生成式工具正在把做 deck 这类杂活整段吞掉。"
    url: "https://x.com/bcherny/status/2111158313463525518"
    link_label: "X 原帖"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "① ChatGPT 刚加上 slides 支持，目前先向 Pro、Business 和 Enterprise 开放，边收集反馈边迭代——文档生成之后，演示文稿成了各家必争的下一个产物形态。② 他介绍了 ChatGPT Space，并直接向用户征集“接下来想看到什么”，属于产品团队公开共创的信号。"
    url: "https://x.com/thsottiaux/status/2111249810502353152"
    link_label: "X 原帖"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "① 数据主权成为卖点：Replit 可以部署到客户自己的云里，数据不出门，明确瞄准政府、金融、医疗等高风险环境——企业级 AI coding 的竞争点正从模型能力转向部署与合规。② 他观察到数学家群体对 AI 解题正在压缩经历否认、愤怒、讨价还价、沮丧到接受的完整过程，目前已接近接受阶段，与本周 AI 数学成果的舆论氛围互为印证。"
    url: "https://x.com/amasad/status/2111267314012496121"
    link_label: "X 原帖"
  - title: "Dan Shipper"
    role: "CEO @ Every"
    summary: "一句话点出能力瓶颈的迁移：generation 已经便宜且高质量，现在真正缺的大跃升是 editing 和 oversight——会生成不再稀缺，会审、会改、会把关才是。"
    url: "https://x.com/danshipper/status/2111174407637139668"
    link_label: "X 原帖"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "他转发并点评了一个 TypeScript 编译实验：经 scriptc 编译后，运行速度比 tsgo 快 2–4 倍，配文 “TypeScript is the new TypeScript”——语言生态的性能竞赛还在继续，编译路径本身成了变量。"
    url: "https://x.com/rauchg/status/2111274408706965898"
    link_label: "X 原帖"
  - title: "Garry Tan"
    role: "President & CEO @ Y Combinator"
    summary: "他分享自己开新项目的工作流：用 Capy + Aside 让 agent 同时写出第一版代码并把 DevOps 一并搭好——在他看来，创始人起步阶段的“写代码 + 部署环境”已经可以打包交给 agent 一次完成。"
    url: "https://x.com/garrytan/status/2111235500568969451"
    link_label: "X 原帖"
  - title: "Sam Altman"
    role: "OpenAI"
    summary: "他晒出 Navier-Stokes 里程碑纪念衫的背面：印的是解题 chain-of-thought 的最后一行。用一件周边把“AI 解出经典数学难题”做成团队文化符号，也侧面确认 OpenAI 正把数学成果当作本阶段的标志性进展在传播（具体的解与验证细节以官方发布为准，本条只记其表态）。"
    url: "https://x.com/sama/status/2111139227761266699"
    link_label: "X 原帖"
  - title: "No Priors — The Changing Physics of Cybersecurity and Drug Development with OpenAI President Greg Brockman（2026-10-15 发布）"
    summary: "Brockman 的核心判断有三层。一是 AI 已能产出真正的新知识：约 400 个百年数学开放问题被解出，关键不在给出答案，而在证明里出现了专家认为有启发的思路连接；把同一套方法迁向生物与药物时，瓶颈不在模型，而在数据、湿实验室与监管申报等流程环节。二是网络安全正处在 “defender's window”：前沿能力先握在防御方手里，应趁其扩散前用模型查漏、做形式化验证、偿还技术债；他由此断言 security spend 终将远超 software spend，并透露 OpenAI 内部曾抽调约 25 名工程师专职用峰值模型自查基础设施，直到该模型能发现的问题饱和为止。三是产品形态上 “best UI is no UI”：主动型 agent（如内部工具 DOTS）常驻后台，跨 inbox、Slack 与日历替人盯待办和日程冲突；consumer 与 enterprise 的区别主要只剩算力成本，而非物种之分。贯穿全程的前提是 human agency——能力再强，人也要坐在驾驶座上。 --- 内容来源：Follow Builders — https://github.com/zarazhangrui/follow-builders"
    url: "https://www.youtube.com/@NoPriorsPodcast"
    link_label: "X 原帖"
---

日期：2026-10-17（America/Los_Angeles）
Feed 更新时间：X feed 生成于 2026-10-17T06:37:54Z（洛杉矶 10-16 23:37），博客与播客 feed 生成于 2026-10-17T06:38:30Z，均为本次运行前约 9.5 小时的新 feed，不是旧内容冒充今日新闻。X 窗口为最近 24 小时，以下条目均未在往期日报报告过。

## X 开发者观点

**Aaron Levie（CEO @ Box）**
他认为行业已经越过一个门槛：AI 比人更擅长训练模型这件事正在变得现实可行。模型能力超过多数人类工程师、long-running agent 的 harness 与基础设施成熟、可并行调用的 agent 数量大增，三者叠加形成 recursive self-improvement 的飞轮——前沿进步的速度可能远超以往，低估 RSI 的后果是定价错误。
[X 原帖](https://x.com/levie/status/2111312141609586862)

**Boris Cherny（Claude @ Anthropic）**
① 他说自己已经离不开 Claude Code Review：它跑在他所有的 PR 上，能在合入前抓到几乎每一个 bug，这是团队既能快速推进又能抬高质量门槛的“secret sauce”之一。② 他现在用 Claude Slides 做幻灯片，不再像过去那样到处搜 “iphone frame svg” 之类的素材——生成式工具正在把做 deck 这类杂活整段吞掉。
[X 原帖](https://x.com/bcherny/status/2111158313463525518)
[X 原帖](https://x.com/bcherny/status/2111158659971699136)

**Thibault Sottiaux（Codex & ChatGPT @ OpenAI）**
① ChatGPT 刚加上 slides 支持，目前先向 Pro、Business 和 Enterprise 开放，边收集反馈边迭代——文档生成之后，演示文稿成了各家必争的下一个产物形态。② 他介绍了 ChatGPT Space，并直接向用户征集“接下来想看到什么”，属于产品团队公开共创的信号。
[X 原帖](https://x.com/thsottiaux/status/2111249810502353152)
[X 原帖](https://x.com/thsottiaux/status/2111249534072529256)

**Amjad Masad（CEO @ Replit）**
① 数据主权成为卖点：Replit 可以部署到客户自己的云里，数据不出门，明确瞄准政府、金融、医疗等高风险环境——企业级 AI coding 的竞争点正从模型能力转向部署与合规。② 他观察到数学家群体对 AI 解题正在压缩经历否认、愤怒、讨价还价、沮丧到接受的完整过程，目前已接近接受阶段，与本周 AI 数学成果的舆论氛围互为印证。
[X 原帖](https://x.com/amasad/status/2111267314012496121)
[X 原帖](https://x.com/amasad/status/2111206044416500159)

**Dan Shipper（CEO @ Every）**
一句话点出能力瓶颈的迁移：generation 已经便宜且高质量，现在真正缺的大跃升是 editing 和 oversight——会生成不再稀缺，会审、会改、会把关才是。
[X 原帖](https://x.com/danshipper/status/2111174407637139668)

**Guillermo Rauch（CEO @ Vercel）**
他转发并点评了一个 TypeScript 编译实验：经 scriptc 编译后，运行速度比 tsgo 快 2–4 倍，配文 “TypeScript is the new TypeScript”——语言生态的性能竞赛还在继续，编译路径本身成了变量。
[X 原帖](https://x.com/rauchg/status/2111274408706965898)

**Garry Tan（President & CEO @ Y Combinator）**
他分享自己开新项目的工作流：用 Capy + Aside 让 agent 同时写出第一版代码并把 DevOps 一并搭好——在他看来，创始人起步阶段的“写代码 + 部署环境”已经可以打包交给 agent 一次完成。
[X 原帖](https://x.com/garrytan/status/2111235500568969451)

**Sam Altman（OpenAI）**
他晒出 Navier-Stokes 里程碑纪念衫的背面：印的是解题 chain-of-thought 的最后一行。用一件周边把“AI 解出经典数学难题”做成团队文化符号，也侧面确认 OpenAI 正把数学成果当作本阶段的标志性进展在传播（具体的解与验证细节以官方发布为准，本条只记其表态）。
[X 原帖](https://x.com/sama/status/2111139227761266699)

其余 X 条目多为纯宣传、玩笑、无内容转发或私人动态（如 ASCII 艺术、诗、Roadster 演示、活动 RSVP），已按规则过滤。

## 官方博客

本次 feed-blogs.json（generatedAt 2026-10-17T06:38:30Z，lookback 72 小时）条目为 0，没有新的官方博客公告可报告。

## 播客

**No Priors — The Changing Physics of Cybersecurity and Drug Development with OpenAI President Greg Brockman（2026-10-15 发布）**
Brockman 的核心判断有三层。一是 AI 已能产出真正的新知识：约 400 个百年数学开放问题被解出，关键不在给出答案，而在证明里出现了专家认为有启发的思路连接；把同一套方法迁向生物与药物时，瓶颈不在模型，而在数据、湿实验室与监管申报等流程环节。二是网络安全正处在 “defender's window”：前沿能力先握在防御方手里，应趁其扩散前用模型查漏、做形式化验证、偿还技术债；他由此断言 security spend 终将远超 software spend，并透露 OpenAI 内部曾抽调约 25 名工程师专职用峰值模型自查基础设施，直到该模型能发现的问题饱和为止。三是产品形态上 “best UI is no UI”：主动型 agent（如内部工具 DOTS）常驻后台，跨 inbox、Slack 与日历替人盯待办和日程冲突；consumer 与 enterprise 的区别主要只剩算力成本，而非物种之分。贯穿全程的前提是 human agency——能力再强，人也要坐在驾驶座上。
节目页：[节目页](https://www.youtube.com/@NoPriorsPodcast)

---
内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
