---
section: ai-builders
section_name: AI Builders
date: 2026-11-03 09:51:00 -0800
title: "AI Builders Digest — 2026-11-03"
excerpt: "Agent 安全与多模型路由是今日主线：权限按任务切分、模型按任务路由；播客里 Legora CTO 详解在看不到客户数据时如何做法务 agent。"
items:
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "你的“dot”（个人助手）会按任务分工调用不同模型，而不是一个模型包打天下。这说明多模型路由正在从实验变成产品形态：选型标准从“哪个模型最强”转向“哪段工作配哪个模型”，做 agent 产品要把路由和回退当成一等设计。"
    url: "https://x.com/thsottiaux/status/2117283355427495983"
    link_label: "X 原帖"
    time: "11-02 07:51"
  - title: "Peter Yang"
    role: "Behind the Craft"
    summary: "他同时让 ChatGPT 和 Gemini 给同一篇帖子提文案修改建议：ChatGPT 的建议几乎全不行，Gemini 的却很好；但 Antigravity 没有可用的浏览器操作，他只能把 Gemini 的修改粘回 ChatGPT 里改。说明写作上模型差距仍大，且真正卡住人的往往不是模型本身，而是工具链（harness）是否顺手。"
    url: "https://x.com/petergyang/status/2117333424403042330"
    link_label: "X 原帖"
    time: "11-02 11:10"
  - title: "Nan Yu"
    role: "产品，Codex @ OpenAI"
    summary: "除极少数例外，群聊是糟糕的多人 AI 体验，注定产出 slop。这提醒做多人协作 AI 产品时，别把单人助手直接塞进群聊——群聊的上下文、轮次和注意力结构本身就不适合，需要另起一套交互设计。"
    url: "https://x.com/thenanyu/status/2117432599559716940"
    link_label: "X 原帖"
    time: "11-02 17:44"
  - title: "Thariq"
    role: "前 Claude Code @ Anthropic"
    summary: "用了一周后的体会：不需要无限 token 也能做出好东西，$200 档位的套餐已经很好，而且“这是智能最贵的时候”。这对 builder 的成本心态有直接意义：别等更便宜，先用现有档位把东西做出来。"
    url: "https://x.com/trq212/status/2117305792923889731"
    link_label: "X 原帖"
    time: "11-02 09:20"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "AI agent 应该跑在组织可控的专用环境里，每项任务只给完成它所需的最小资源权限。这是对企业部署 agent 的安全底线：权限按任务切分，而不是给 agent 一个万能钥匙。"
    url: "https://x.com/amasad/status/2117499074496872882"
    link_label: "X 原帖"
    time: "11-02 22:08"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "无状态沙箱是错误的评测基准——agent 只有带着自己的工作区（身份、技能、仓库、记忆）才真正有用；同时称赞 Vercel Sandbox 团队在延迟与吞吐 SLO、可靠性和安全性上的交付，19 个全球区域、每周上新、需求每周双位数百分比增长。这说明评测 agent 不能只看裸模型能力，带状态的工作区才是生产力来源。"
    url: "https://x.com/rauchg/status/2117338179535810957"
    link_label: "X 原帖"
    time: "11-02 11:28"
  - title: "Garry Tan"
    role: "President & CEO @ Y Combinator"
    summary: "Capy Captains 让他修 issue 的吞吐一夜提升约 5 倍，能跨 captain 与子线程协调是关键解锁。这说明多 agent 编排的收益不在单个 agent 更强，而在协调结构——能并行分工的团队式 agent 正在拉开效率差距。"
    url: "https://x.com/garrytan/status/2117410016730964358"
    link_label: "X 原帖"
    time: "11-02 16:14"
  - title: "Garry Tan"
    role: "President & CEO @ Y Combinator"
    summary: "转发一种小模型的新用法：直接操作权重。这提示小模型路线不止是“便宜版大模型”，权重层面的直接干预可能开出新的产品与微调玩法，值得做模型产品的 builder 跟进原文。"
    url: "https://x.com/garrytan/status/2117384926052135106"
    link_label: "X 原帖"
    time: "11-02 14:34"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "新办线下活动系列 Slice for Thought：首期 11 月 4 日周三中午在旧金山，嘉宾是 OpenRouter 洞察负责人 Peter J. Walker；60 分钟线下、45 分钟他问嘉宾辛辣问题、15 分钟嘉宾反问他，全程 off the record、Chatham House 规则，每周一次、限 10–12 位旁听嘉宾。想去旧金山线下交流的 builder 可报名。"
    url: "https://x.com/nikunj/status/2117413490256433207"
    link_label: "X 原帖"
    time: "11-02 16:28"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "调侃式观察：创业公司（或 CEO）从含糊发营收数字到正式启动融资，间隔约 11 天（样本 n=17，用 Grok bot token 做的分析）。半开玩笑半是信号：含糊晒数字往往是融资启动的前奏，读融资信号时可把这个节奏当参考。"
    url: "https://x.com/nikunj/status/2117362283223687621"
    link_label: "X 原帖"
    time: "11-02 13:04"
  - title: "Dan Shipper"
    role: "CEO @ Every"
    summary: "一半因为 Argon 本身确实好，一半因为 Antigravity 还停留在 2025，没有那些疯狂的新功能和复杂性。这说明新工具的窗口期常常来自对手的停滞：功能少、跟上最新能力，有时比功能全更能赢得 builder。"
    url: "https://x.com/danshipper/status/2117363007340609556"
    link_label: "X 原帖"
    time: "11-02 13:07"
  - title: "Aditya Agarwal"
    role: "General Partner @ South Park Commons"
    summary: "欢迎 SPC 校友回归：四次创业者、IOI 奖牌得主 Tankots 现为 WisprFlow 联合创始人兼 CEO，该公司刚完成 2.8 亿美元 B 轮、估值 20 亿美元，他将于 11 月 12 日加入 SPC 活动。说明该赛道仍在高估值快速融资，值得关注其产品动向。"
    url: "https://x.com/adityaag/status/2117313674981355761"
    link_label: "X 原帖"
    time: "11-02 09:51"
  - title: "Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora"
    role: "Latent Space"
    summary: "Legora CTO 谈在看不到客户数据的情况下做法务 agent：数据高度保密，团队基本看不到真实使用轨迹，只能靠改写脱敏的合成轨迹学习；律所早期只信任已过安全审查的微软/Azure。产品从 ChatGPT 加瑞典法律搜索起步，演进为起草、编辑 Word、批量审阅的 Tabular Review 与工作编排；约 60% 法务工作现有模型已能做好，剩下拼成本、延迟与复杂分析。团队按领域与任务建 eval 热力图，发现新模型常部分提升、部分回退，故按任务路由不同模型。"
    url: "https://www.youtube.com/@LatentSpacePod"
    link_label: "节目页"
    time: "11-02 12:50"
---

**X 观点**

- [Thibault Sottiaux（Codex & ChatGPT @ OpenAI）](https://x.com/thsottiaux/status/2117283355427495983)：你的“dot”（个人助手）会按任务分工调用不同模型，而不是一个模型包打天下。这说明多模型路由正在从实验变成产品形态：选型标准从“哪个模型最强”转向“哪段工作配哪个模型”，做 agent 产品要把路由和回退当成一等设计。
- [Peter Yang（Behind the Craft）](https://x.com/petergyang/status/2117333424403042330)：他同时让 ChatGPT 和 Gemini 给同一篇帖子提文案修改建议：ChatGPT 的建议几乎全不行，Gemini 的却很好；但 Antigravity 没有可用的浏览器操作，他只能把 Gemini 的修改粘回 ChatGPT 里改。说明写作上模型差距仍大，且真正卡住人的往往不是模型本身，而是工具链（harness）是否顺手。
- [Nan Yu（产品，Codex @ OpenAI）](https://x.com/thenanyu/status/2117432599559716940)：除极少数例外，群聊是糟糕的多人 AI 体验，注定产出 slop。这提醒做多人协作 AI 产品时，别把单人助手直接塞进群聊——群聊的上下文、轮次和注意力结构本身就不适合，需要另起一套交互设计。
- [Thariq（前 Claude Code @ Anthropic）](https://x.com/trq212/status/2117305792923889731)：用了一周后的体会：不需要无限 token 也能做出好东西，$200 档位的套餐已经很好，而且“这是智能最贵的时候”。这对 builder 的成本心态有直接意义：别等更便宜，先用现有档位把东西做出来。
- [Amjad Masad（CEO @ Replit）](https://x.com/amasad/status/2117499074496872882)：AI agent 应该跑在组织可控的专用环境里，每项任务只给完成它所需的最小资源权限。这是对企业部署 agent 的安全底线：权限按任务切分，而不是给 agent 一个万能钥匙。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2117338179535810957)：无状态沙箱是错误的评测基准——agent 只有带着自己的工作区（身份、技能、仓库、记忆）才真正有用；同时称赞 Vercel Sandbox 团队在延迟与吞吐 SLO、可靠性和安全性上的交付，19 个全球区域、每周上新、需求每周双位数百分比增长。这说明评测 agent 不能只看裸模型能力，带状态的工作区才是生产力来源。
- [Garry Tan（President & CEO @ Y Combinator）](https://x.com/garrytan/status/2117410016730964358)：Capy Captains 让他修 issue 的吞吐一夜提升约 5 倍，能跨 captain 与子线程协调是关键解锁。这说明多 agent 编排的收益不在单个 agent 更强，而在协调结构——能并行分工的团队式 agent 正在拉开效率差距。
- [Garry Tan（President & CEO @ Y Combinator）](https://x.com/garrytan/status/2117384926052135106)：转发一种小模型的新用法：直接操作权重。这提示小模型路线不止是“便宜版大模型”，权重层面的直接干预可能开出新的产品与微调玩法，值得做模型产品的 builder 跟进原文。
- [Nikunj Kothari（Partner @ FPV Ventures）](https://x.com/nikunj/status/2117413490256433207)：新办线下活动系列 Slice for Thought：首期 11 月 4 日周三中午在旧金山，嘉宾是 OpenRouter 洞察负责人 Peter J. Walker；60 分钟线下、45 分钟他问嘉宾辛辣问题、15 分钟嘉宾反问他，全程 off the record、Chatham House 规则，每周一次、限 10–12 位旁听嘉宾。想去旧金山线下交流的 builder 可报名。
- [Nikunj Kothari（Partner @ FPV Ventures）](https://x.com/nikunj/status/2117362283223687621)：调侃式观察：创业公司（或 CEO）从含糊发营收数字到正式启动融资，间隔约 11 天（样本 n=17，用 Grok bot token 做的分析）。半开玩笑半是信号：含糊晒数字往往是融资启动的前奏，读融资信号时可把这个节奏当参考。
- [Dan Shipper（CEO @ Every）](https://x.com/danshipper/status/2117363007340609556)：一半因为 Argon 本身确实好，一半因为 Antigravity 还停留在 2025，没有那些疯狂的新功能和复杂性。这说明新工具的窗口期常常来自对手的停滞：功能少、跟上最新能力，有时比功能全更能赢得 builder。
- [Aditya Agarwal（General Partner @ South Park Commons）](https://x.com/adityaag/status/2117313674981355761)：欢迎 SPC 校友回归：四次创业者、IOI 奖牌得主 Tankots 现为 WisprFlow 联合创始人兼 CEO，该公司刚完成 2.8 亿美元 B 轮、估值 20 亿美元，他将于 11 月 12 日加入 SPC 活动。说明该赛道仍在高估值快速融资，值得关注其产品动向。

**播客**

- [Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora（Latent Space）](https://www.youtube.com/@LatentSpacePod)：Legora CTO 谈在看不到客户数据的情况下做法务 agent：数据高度保密，团队基本看不到真实使用轨迹，只能靠改写脱敏的合成轨迹学习；律所早期只信任已过安全审查的微软/Azure。产品从 ChatGPT 加瑞典法律搜索起步，演进为起草、编辑 Word、批量审阅的 Tabular Review 与工作编排；约 60% 法务工作现有模型已能做好，剩下拼成本、延迟与复杂分析。团队按领域与任务建 eval 热力图，发现新模型常部分提升、部分回退，故按任务路由不同模型。

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
