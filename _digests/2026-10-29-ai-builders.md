---
section: ai-builders
section_name: AI Builders
date: 2026-10-29 09:52:50 -0700
title: "AI Builders Digest — 2026-10-29"
excerpt: "Gemini 4 Carbon 与 Strava 接入、犹他州 Claude Code 试点、Vercel 的 Agentic CI 与模型 DNS、agent token 量将涨 1000 倍的判断；播客里 Fred Graver 谈 AI 如何做“虚拟编剧室”而不替人写作。"
items:
  - title: "Swyx"
    role: "Latent Space"
    summary: "Gemini 在 AAv5 拿第一，让他时隔许久重新打开 Antigravity 试用并准备出早期评测；他认为若 Google 真做成，加上 Meta、Grok 回暖，就是前沿实验室的“回归季”，并呼应模型神经多样性——如今前沿实验室数量约为去年的两倍，成了“苦涩教训”的反例。"
    url: "https://x.com/swyx/status/2115624308567658713"
    link_label: "X 原帖"
    time: "10-28 18:58"
  - title: "Josh Woodward"
    role: "VP @ Google"
    summary: "Gemini 新功能：连接 Strava 账号，把多年原始训练记录变成个性化训练计划。重要之处在于把健身数据从记录变成教练，说明 Gemini 正从通用对话向个人数据驱动的长期陪伴延伸。"
    url: "https://x.com/joshwoodward/status/2115580552170627080"
    link_label: "X 原帖"
    time: "10-28 16:04"
  - title: "Josh Woodward"
    role: "VP @ Google"
    summary: "两周前 Gemini 4 Argon，今天 Gemini 4 Carbon；内部反响好，先向网络防御者推出，再逐步更广泛开放。前沿模型迭代速度仍在以周为单位推进，安全场景先行是值得注意的发布顺序。"
    url: "https://x.com/joshwoodward/status/2115495943948902517"
    link_label: "X 原帖"
    time: "10-28 10:28"
  - title: "Boris Cherny"
    role: "Claude @ Anthropic"
    summary: "犹他州把 Claude Code 交给 10 个州机构的 34 名开发者做四周试点：80% 在 30 分钟内搭好可用环境，71% 报告节省 20 小时以上。这是政府场景 agent 编程工具落地的可量化案例，而非轶事。"
    url: "https://x.com/bcherny/status/2115491259381072269"
    link_label: "X 原帖"
    time: "10-28 10:09"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "第 24 天分享：可以像给任何人发短信一样给 dot 发短信，转发内容、留语音备忘，甚至用 Siri 说一句“text Iggy to <疯狂请求>”就坐等结果。把 agent 藏进最日常的短信入口，降低了调用门槛。"
    url: "https://x.com/thsottiaux/status/2115622002581188681"
    link_label: "X 原帖"
    time: "10-28 18:49"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "团队正在做把 Chat 与 Work 两边能力合到一起的工作，但尚未推出，今年内某个时点会推进，且会谨慎行事。澄清了传闻，也说明 OpenAI 在统一工作流入口上仍在权衡节奏。"
    url: "https://x.com/thsottiaux/status/2115588390414581916"
    link_label: "X 原帖"
    time: "10-28 16:35"
  - title: "Peter Yang"
    role: "Practical AI 教程作者"
    summary: "世界模型仍处 GPT-3.5 时代：像早期 Will Smith 吃面条视频，画面和声音已不错、玩法还不行；他用自己 Genie 4 生成片段对比后认为，一旦到 GPT-5/6 阶段，对电影（大场面从数月 VFX 变成一帧生成）和游戏（人人可做自己的游戏）都有巨大影响。"
    url: "https://x.com/petergyang/status/2115556794076741647"
    link_label: "X 原帖"
    time: "10-28 14:30"
  - title: "Thariq"
    role: "前 Claude Code @ Anthropic"
    summary: "正在发生一件怪事：技术人觉得自己的技能变得无用而难过，非技术人却拼命希望自己更懂技术以便更好地用 agent。同一波 agent 浪潮在两群人心里投出相反的焦虑，点出了“会用 agent”正在成为新的技术门槛。"
    url: "https://x.com/trq212/status/2115544056038350960"
    link_label: "X 原帖"
    time: "10-28 13:39"
  - title: "Thariq"
    role: "前 Claude Code @ Anthropic"
    summary: "他希望能先随手画出动画创意和角色概念，再交给 agent 细化，而不是到处找参考图——“我没有那种语言”。对创作者而言，agent 的下一道门槛不是生成能力，而是让不会画画、不会写代码的人也能把脑子里的形象直接递过去。"
    url: "https://x.com/trq212/status/2115641110710419752"
    link_label: "X 原帖"
    time: "10-28 20:05"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "ViBench 2.0（prompt-to-app 基准）刚发布，GPT 6.1 Sol 拿下第一。Prompt 直接生成完整应用的能力正在被标准化衡量，OpenAI 新模型在这一项上暂时领先，值得看后续各家在同一基准上的追赶。"
    url: "https://x.com/amasad/status/2115565072734888447"
    link_label: "X 原帖"
    time: "10-28 15:03"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "这就像模型的 DNS：一个别名“解析”到某个模型，带来流量调度能力。好处一串：团队不再被锁在旧模型版本上、省成本、消除选型纠结。对把模型当基础设施用的团队，这是个很实用的抽象层。"
    url: "https://x.com/rauchg/status/2115573969369845855"
    link_label: "X 原帖"
    time: "10-28 15:38"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "宣布与 Suhail 合作，通过 Vercel AI Gateway 提供 Particle 的模型与推理。Particle 的使命是让智能像电力一样可及且充裕；两者结合是想让每个开发者和企业都用得起前沿推理。"
    url: "https://x.com/rauchg/status/2115566139447382115"
    link_label: "X 原帖"
    time: "10-28 15:07"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "Vercel CI 要解决“AI 编程瓶颈”：①更快更稳的基础设施（全球 20 个集群、每天数百万 microVM）；②Turborepo 集成（智能跳过与缓存已做过的工作）；③Agentic CI——CLI 里 agent 能查看、中止、触发、重放 CI。CI 正在从被动检查变成 agent 可操作的环节。"
    url: "https://x.com/rauchg/status/2115539426684408300"
    link_label: "X 原帖"
    time: "10-28 13:21"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "Agent 将消耗比今天多 1000 倍的 token：因为它们要跑在工作流里、处理全部数据、构建几乎所有软件、守卫企业安全。要规模化，需要同时推进闭源模型、更强的开源权重模型、更安全与更高效的大负载方案；他点名看好 Suhail 在 Particle 的工作。"
    url: "https://x.com/levie/status/2115516370695987435"
    link_label: "X 原帖"
    time: "10-28 11:49"
  - title: "Ryo Lu"
    role: "产品设计师"
    summary: "长文重提 Engelbart“增强人类智能”：计算机的意义不是替人干活，而是让人理解复杂局面、找到此前够不到的解法。他提醒：不是所有困难都是 overhead，有时摆弄部件本身就是理解；工具应让人能追问、改动、撤销、学到下一步，而不是让人变小、变依赖。"
    url: "https://x.com/ryolu_/status/2115683228027912634"
    link_label: "X 原帖"
    time: "10-28 22:52"
  - title: "Peter Steinberger"
    role: "OpenClaw 开发者"
    summary: "OpenClaw 的网页 UI 现在可离线工作，并用了智能 WebSocket 压缩与重连逻辑；他飞往维也纳途中在断断续续的机上 Wi-Fi 下仍做了不少工作。Agent 的“随时可用”正在从模型能力问题变成连接与离线工程问题。"
    url: "https://x.com/steipete/status/2115397368229060636"
    link_label: "X 原帖"
    time: "10-28 03:56"
  - title: "Aditya Agarwal"
    role: "General Partner @ SPC"
    summary: "他与 Gopal Raman 合写的 LP 信总结了十年在前沿投资中识别人才的教训：大家都说早期投资“90% 看创始人”，但这句话缺乏可证伪性、具体性与可重复性；信里试图把卓越拆成可衡量的维度，并说明这些维度如何转化成公司。"
    url: "https://x.com/adityaag/status/2115486597739430004"
    link_label: "X 原帖"
    time: "10-28 09:51"
  - title: "Claude"
    role: "Claude 官方"
    summary: "Claude for Legal 上新：现成的 artifact 画廊，覆盖合同审阅、监管动态扫描、引用核查等；可从内置示例起步，加入自己的文档与连接器，再分享给全公司业务方。法律这类高严谨场景正被做成可复用的 agent 模板。"
    url: "https://x.com/claudeai/status/2115467192276025500"
    link_label: "X 原帖"
    time: "10-28 08:34"
  - title: "Can You Use AI To Make Good Art? — With Fred Graver"
    role: "AI & I by Every"
    summary: "创意行业正处动荡，写手与制片人机会变少；Graver 的核心论点是 AI 应是“虚拟编剧室”，而不是替你写作：先向内清空——写下“我是谁”、灵感、想做的事与受众是谁，再让 AI 帮你想透；创作分构思、制作、触达受众三段并循环，专家插件把卓越做法编码成步骤；防“AI 垃圾”的关键是先有自己独特的东西，AI 只能帮你说出来，不能替你决定说什么；最难的仍是第三段——找到并养活受众。"
    url: "https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL"
    link_label: "节目页"
    time: "10-28 13:23"
---

**X 观点**

- [Swyx（Latent Space）](https://x.com/swyx/status/2115624308567658713)：Gemini 在 AAv5 拿第一，让他时隔许久重新打开 Antigravity 试用并准备出早期评测；他认为若 Google 真做成，加上 Meta、Grok 回暖，就是前沿实验室的“回归季”，并呼应模型神经多样性——如今前沿实验室数量约为去年的两倍，成了“苦涩教训”的反例。
- [Josh Woodward（VP @ Google）](https://x.com/joshwoodward/status/2115580552170627080)：Gemini 新功能：连接 Strava 账号，把多年原始训练记录变成个性化训练计划。重要之处在于把健身数据从记录变成教练，说明 Gemini 正从通用对话向个人数据驱动的长期陪伴延伸。
- [Josh Woodward（VP @ Google）](https://x.com/joshwoodward/status/2115495943948902517)：两周前 Gemini 4 Argon，今天 Gemini 4 Carbon；内部反响好，先向网络防御者推出，再逐步更广泛开放。前沿模型迭代速度仍在以周为单位推进，安全场景先行是值得注意的发布顺序。
- [Boris Cherny（Claude @ Anthropic）](https://x.com/bcherny/status/2115491259381072269)：犹他州把 Claude Code 交给 10 个州机构的 34 名开发者做四周试点：80% 在 30 分钟内搭好可用环境，71% 报告节省 20 小时以上。这是政府场景 agent 编程工具落地的可量化案例，而非轶事。
- [Thibault Sottiaux（Codex & ChatGPT @ OpenAI）](https://x.com/thsottiaux/status/2115622002581188681)：第 24 天分享：可以像给任何人发短信一样给 dot 发短信，转发内容、留语音备忘，甚至用 Siri 说一句“text Iggy to <疯狂请求>”就坐等结果。把 agent 藏进最日常的短信入口，降低了调用门槛。
- [Thibault Sottiaux（Codex & ChatGPT @ OpenAI）](https://x.com/thsottiaux/status/2115588390414581916)：团队正在做把 Chat 与 Work 两边能力合到一起的工作，但尚未推出，今年内某个时点会推进，且会谨慎行事。澄清了传闻，也说明 OpenAI 在统一工作流入口上仍在权衡节奏。
- [Peter Yang（Practical AI 教程作者）](https://x.com/petergyang/status/2115556794076741647)：世界模型仍处 GPT-3.5 时代：像早期 Will Smith 吃面条视频，画面和声音已不错、玩法还不行；他用自己 Genie 4 生成片段对比后认为，一旦到 GPT-5/6 阶段，对电影（大场面从数月 VFX 变成一帧生成）和游戏（人人可做自己的游戏）都有巨大影响。
- [Thariq（前 Claude Code @ Anthropic）](https://x.com/trq212/status/2115544056038350960)：正在发生一件怪事：技术人觉得自己的技能变得无用而难过，非技术人却拼命希望自己更懂技术以便更好地用 agent。同一波 agent 浪潮在两群人心里投出相反的焦虑，点出了“会用 agent”正在成为新的技术门槛。
- [Thariq（前 Claude Code @ Anthropic）](https://x.com/trq212/status/2115641110710419752)：他希望能先随手画出动画创意和角色概念，再交给 agent 细化，而不是到处找参考图——“我没有那种语言”。对创作者而言，agent 的下一道门槛不是生成能力，而是让不会画画、不会写代码的人也能把脑子里的形象直接递过去。
- [Amjad Masad（CEO @ Replit）](https://x.com/amasad/status/2115565072734888447)：ViBench 2.0（prompt-to-app 基准）刚发布，GPT 6.1 Sol 拿下第一。Prompt 直接生成完整应用的能力正在被标准化衡量，OpenAI 新模型在这一项上暂时领先，值得看后续各家在同一基准上的追赶。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2115573969369845855)：这就像模型的 DNS：一个别名“解析”到某个模型，带来流量调度能力。好处一串：团队不再被锁在旧模型版本上、省成本、消除选型纠结。对把模型当基础设施用的团队，这是个很实用的抽象层。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2115566139447382115)：宣布与 Suhail 合作，通过 Vercel AI Gateway 提供 Particle 的模型与推理。Particle 的使命是让智能像电力一样可及且充裕；两者结合是想让每个开发者和企业都用得起前沿推理。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2115539426684408300)：Vercel CI 要解决“AI 编程瓶颈”：①更快更稳的基础设施（全球 20 个集群、每天数百万 microVM）；②Turborepo 集成（智能跳过与缓存已做过的工作）；③Agentic CI——CLI 里 agent 能查看、中止、触发、重放 CI。CI 正在从被动检查变成 agent 可操作的环节。
- [Aaron Levie（CEO @ Box）](https://x.com/levie/status/2115516370695987435)：Agent 将消耗比今天多 1000 倍的 token：因为它们要跑在工作流里、处理全部数据、构建几乎所有软件、守卫企业安全。要规模化，需要同时推进闭源模型、更强的开源权重模型、更安全与更高效的大负载方案；他点名看好 Suhail 在 Particle 的工作。
- [Ryo Lu（产品设计师）](https://x.com/ryolu_/status/2115683228027912634)：长文重提 Engelbart“增强人类智能”：计算机的意义不是替人干活，而是让人理解复杂局面、找到此前够不到的解法。他提醒：不是所有困难都是 overhead，有时摆弄部件本身就是理解；工具应让人能追问、改动、撤销、学到下一步，而不是让人变小、变依赖。
- [Peter Steinberger（OpenClaw 开发者）](https://x.com/steipete/status/2115397368229060636)：OpenClaw 的网页 UI 现在可离线工作，并用了智能 WebSocket 压缩与重连逻辑；他飞往维也纳途中在断断续续的机上 Wi-Fi 下仍做了不少工作。Agent 的“随时可用”正在从模型能力问题变成连接与离线工程问题。
- [Aditya Agarwal（General Partner @ SPC）](https://x.com/adityaag/status/2115486597739430004)：他与 Gopal Raman 合写的 LP 信总结了十年在前沿投资中识别人才的教训：大家都说早期投资“90% 看创始人”，但这句话缺乏可证伪性、具体性与可重复性；信里试图把卓越拆成可衡量的维度，并说明这些维度如何转化成公司。
- [Claude（Claude 官方）](https://x.com/claudeai/status/2115467192276025500)：Claude for Legal 上新：现成的 artifact 画廊，覆盖合同审阅、监管动态扫描、引用核查等；可从内置示例起步，加入自己的文档与连接器，再分享给全公司业务方。法律这类高严谨场景正被做成可复用的 agent 模板。

**播客**

- [Can You Use AI To Make Good Art? — With Fred Graver（AI & I by Every）](https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL)：创意行业正处动荡，写手与制片人机会变少；Graver 的核心论点是 AI 应是“虚拟编剧室”，而不是替你写作：先向内清空——写下“我是谁”、灵感、想做的事与受众是谁，再让 AI 帮你想透；创作分构思、制作、触达受众三段并循环，专家插件把卓越做法编码成步骤；防“AI 垃圾”的关键是先有自己独特的东西，AI 只能帮你说出来，不能替你决定说什么；最难的仍是第三段——找到并养活受众。

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
