---
section: ai-builders
section_name: AI Builders
date: 2026-11-02 09:52:00 -0800
title: "AI Builders Digest — 2026-11-02"
excerpt: "Karpathy 用 Claude 两小时做出 HackerTube，Levie 谈人人变 agent 团队管理者；播客里 Modal CEO 详解 GPU 市场为何仍不高效、推理平台的真正壁垒。"
items:
  - title: "Andrej Karpathy"
    summary: "周末 hack 做了 HackerTube——他嫌 YouTube 推荐不好用，就让 Claude 筛选 20 年 Hacker News 评论里的 4300 万条评论，挑出 6454 个被反复推荐的视频，做成无登录、缩略图取视频中段真实帧的观看页。他只手动做了 Google Cloud API key、开 VPS、买域名，其余部署加固全交给 Claude，约 2 小时用 Opus 5.5 完成。这说明过去几周甚至几个月量级的项目，现在可以一个早餐时间做出雏形，值得重新想还有什么没被这样做。"
    url: "https://x.com/karpathy/status/2116957135661945283"
    link_label: "X 原帖"
    time: "11-01 10:14"
  - title: "Peter Yang"
    role: "Behind the Craft"
    summary: "预告 Behind the Craft 接下来四期：OpenAI 产品 VP Ashley Alexander 谈照护患癌父母与 ChatGPT 的帮助、Anthropic 设计师 Nate Parrott 谈如何避免 AI slop 设计、AI skills 拿下 30 万 GitHub 星的 Matt Pocock 谈软件工厂、10 人团队年花 3200 万美元 Claude 的游戏公司创始人 Jacob Sansbury。他的选角标准是真正动手做事的 builder，值得按这个名单提前关注。"
    url: "https://x.com/petergyang/status/2117059131349868790"
    link_label: "X 原帖"
    time: "11-01 17:00"
  - title: "Peter Yang"
    role: "Behind the Craft"
    summary: "转引 Google Labs 产品总监的判断：要问产品是否还需要人来用——创作、学习、娱乐仍需人交互，但很多今天人必须亲自操作的工具，完全可以不用人当主要交互者。这为判断哪些产品会被 agent 吃掉、哪些仍需留给人，提供了一条清晰的分界线。"
    url: "https://x.com/petergyang/status/2116987415319740756"
    link_label: "X 原帖"
    time: "11-01 12:15"
  - title: "Peter Yang"
    role: "Behind the Craft"
    summary: "他现在分工明确：浏览器与电脑操作用 ChatGPT + Codex、设计与视频剪辑讲品味用 Claude、24/7 agent 与定时任务用 Grok Bot，Gemini 写作被低估但还在测试。这说明没有单一赢家，按任务分工具已是 builder 的现实用法，选型应按场景而非品牌忠诚。"
    url: "https://x.com/petergyang/status/2116946320674152810"
    link_label: "X 原帖"
    time: "11-01 09:31"
  - title: "Thariq"
    role: "前 Claude Code @ Anthropic"
    summary: "正在做的游戏新增格斗角色：一位会用火的跆拳道大师，并把美术从 3D 模型改成生成精灵图。这说明独立游戏开发里生成式美术已能快速换风格、推新角色，迭代成本明显下降，小团队也能靠美术风格快速试错。"
    url: "https://x.com/trq212/status/2116976789046350040"
    link_label: "X 原帖"
    time: "11-01 11:32"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "警告：现在享受补贴价 AI 订阅的人，要做好被“抽地毯”的准备——补贴不可持续，价格终会回归。这提醒 builder 与用户都别把补贴价当成长期成本基准来做预算和定价，否则涨价那天会措手不及。"
    url: "https://x.com/amasad/status/2117010858845089805"
    link_label: "X 原帖"
    time: "11-01 13:48"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "Replit 一键开启网站反馈组件后，用户反馈会直接变成 agent 的开发提示词。这等于把用户反馈回路接进 agent 构建循环，让产品迭代从“收集意见”变成“自动开工”，反馈到上线的链路被大幅缩短。"
    url: "https://x.com/amasad/status/2116998155925360965"
    link_label: "X 原帖"
    time: "11-01 12:57"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "呼吁“拥有自己的智能”：反对把智能交出去再买回来，主张本地模型继续普及、保持选择开放，拥有自己的 harness、数据、连接与运行时，拥抱开源。核心观点是 agent 时代的自主权不在模型大小，而在自己手里的那套栈。"
    url: "https://x.com/rauchg/status/2117000819623243925"
    link_label: "X 原帖"
    time: "11-01 13:08"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "角色正从个人贡献者变成 agent 团队的管理者：过去靠工时换产出，现在 agent 并行干活，产出与工时脱钩；信息密集型工作如编程、安全、法律、生物、工程受冲击最大。先按这个方式重组流程的组织，会获得复利式的效率优势。"
    url: "https://x.com/levie/status/2117134917847093491"
    link_label: "X 原帖"
    time: "11-01 22:01"
  - title: "Garry Tan"
    role: "President & CEO @ Y Combinator"
    summary: "转发称 Particle-1 在 agent 检索上媲美大得多的模型，价格只有 1/23。这说明检索这类 agent 基础设施正在出现“小模型够用、成本断崖式下降”的选项，对做 agent 产品的成本结构有直接影响，值得在选型时算一笔账。"
    url: "https://x.com/garrytan/status/2117137390016073977"
    link_label: "X 原帖"
    time: "11-01 22:11"
  - title: "Ep 95: Modal CEO on the Future of Inference, the Chaos of the GPU Market & Origins of the Sandbox Bet"
    role: "Unsupervised Learning"
    summary: "Modal CEO Eric 谈推理与 GPU 市场：算力市场远非有效市场，仍靠熟人、WhatsApp 群组撮合，且算力并非同质化合约；Modal 聚合 25 家云，沙箱产品一年增长近千倍、约占收入三分之一，推理也约三分之一。真正的壁垒不是拼 token 价，而是多产品平台；neo cloud 本质是融资工具、资金成本高，未来 12 个月 GPU 租金可能继续上涨。"
    url: "https://www.youtube.com/@RedpointAI"
    link_label: "节目页"
    time: "10-28 06:03"
---

**X 观点**

- [Andrej Karpathy](https://x.com/karpathy/status/2116957135661945283)：周末 hack 做了 HackerTube——他嫌 YouTube 推荐不好用，就让 Claude 筛选 20 年 Hacker News 评论里的 4300 万条评论，挑出 6454 个被反复推荐的视频，做成无登录、缩略图取视频中段真实帧的观看页。他只手动做了 Google Cloud API key、开 VPS、买域名，其余部署加固全交给 Claude，约 2 小时用 Opus 5.5 完成。这说明过去几周甚至几个月量级的项目，现在可以一个早餐时间做出雏形，值得重新想还有什么没被这样做。
- [Peter Yang（Behind the Craft）](https://x.com/petergyang/status/2117059131349868790)：预告 Behind the Craft 接下来四期：OpenAI 产品 VP Ashley Alexander 谈照护患癌父母与 ChatGPT 的帮助、Anthropic 设计师 Nate Parrott 谈如何避免 AI slop 设计、AI skills 拿下 30 万 GitHub 星的 Matt Pocock 谈软件工厂、10 人团队年花 3200 万美元 Claude 的游戏公司创始人 Jacob Sansbury。他的选角标准是真正动手做事的 builder，值得按这个名单提前关注。
- [Peter Yang（Behind the Craft）](https://x.com/petergyang/status/2116987415319740756)：转引 Google Labs 产品总监的判断：要问产品是否还需要人来用——创作、学习、娱乐仍需人交互，但很多今天人必须亲自操作的工具，完全可以不用人当主要交互者。这为判断哪些产品会被 agent 吃掉、哪些仍需留给人，提供了一条清晰的分界线。
- [Peter Yang（Behind the Craft）](https://x.com/petergyang/status/2116946320674152810)：他现在分工明确：浏览器与电脑操作用 ChatGPT + Codex、设计与视频剪辑讲品味用 Claude、24/7 agent 与定时任务用 Grok Bot，Gemini 写作被低估但还在测试。这说明没有单一赢家，按任务分工具已是 builder 的现实用法，选型应按场景而非品牌忠诚。
- [Thariq（前 Claude Code @ Anthropic）](https://x.com/trq212/status/2116976789046350040)：正在做的游戏新增格斗角色：一位会用火的跆拳道大师，并把美术从 3D 模型改成生成精灵图。这说明独立游戏开发里生成式美术已能快速换风格、推新角色，迭代成本明显下降，小团队也能靠美术风格快速试错。
- [Amjad Masad（CEO @ Replit）](https://x.com/amasad/status/2117010858845089805)：警告：现在享受补贴价 AI 订阅的人，要做好被“抽地毯”的准备——补贴不可持续，价格终会回归。这提醒 builder 与用户都别把补贴价当成长期成本基准来做预算和定价，否则涨价那天会措手不及。
- [Amjad Masad（CEO @ Replit）](https://x.com/amasad/status/2116998155925360965)：Replit 一键开启网站反馈组件后，用户反馈会直接变成 agent 的开发提示词。这等于把用户反馈回路接进 agent 构建循环，让产品迭代从“收集意见”变成“自动开工”，反馈到上线的链路被大幅缩短。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2117000819623243925)：呼吁“拥有自己的智能”：反对把智能交出去再买回来，主张本地模型继续普及、保持选择开放，拥有自己的 harness、数据、连接与运行时，拥抱开源。核心观点是 agent 时代的自主权不在模型大小，而在自己手里的那套栈。
- [Aaron Levie（CEO @ Box）](https://x.com/levie/status/2117134917847093491)：角色正从个人贡献者变成 agent 团队的管理者：过去靠工时换产出，现在 agent 并行干活，产出与工时脱钩；信息密集型工作如编程、安全、法律、生物、工程受冲击最大。先按这个方式重组流程的组织，会获得复利式的效率优势。
- [Garry Tan（President & CEO @ Y Combinator）](https://x.com/garrytan/status/2117137390016073977)：转发称 Particle-1 在 agent 检索上媲美大得多的模型，价格只有 1/23。这说明检索这类 agent 基础设施正在出现“小模型够用、成本断崖式下降”的选项，对做 agent 产品的成本结构有直接影响，值得在选型时算一笔账。

**播客**

- [Ep 95: Modal CEO on the Future of Inference, the Chaos of the GPU Market & Origins of the Sandbox Bet（Unsupervised Learning）](https://www.youtube.com/@RedpointAI)：Modal CEO Eric 谈推理与 GPU 市场：算力市场远非有效市场，仍靠熟人、WhatsApp 群组撮合，且算力并非同质化合约；Modal 聚合 25 家云，沙箱产品一年增长近千倍、约占收入三分之一，推理也约三分之一。真正的壁垒不是拼 token 价，而是多产品平台；neo cloud 本质是融资工具、资金成本高，未来 12 个月 GPU 租金可能继续上涨。

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
