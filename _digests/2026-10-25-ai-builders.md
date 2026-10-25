---
section: ai-builders
section_name: AI Builders
date: 2026-10-25 09:49:00 -0700
title: "AI Builders Digest — 2026-10-25"
excerpt: "Levie 预判网络安全 agent 的 token 量将达今天的 1000 倍，Rauch 谈指导 AI 的分寸与模型的工程黑话，Ryo Lu 长文反思失去共同挣扎的代价，MAD Podcast 对谈 Jev 创始人谈用决策与概率取代文本生成。"
items:
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "预判流经网络安全 agent 的 token 量很快会达到今天的 1000 倍。风险面不断扩大、多数公司已跟不上新风险，agent 集群可扇出调用各种安全工具、测试攻击排列、读日志并评估企业数据风险——这依赖长时运行 agent、computer use 与模型网络安全训练近几个月才成熟。他认为身份、防火墙、网络、代码扫描、数据保护全栈都是机会，也是对攻防平衡保持乐观的理由。"
    url: "https://x.com/levie/status/2114187326406766604"
    link_label: "X 原帖"
    time: "10-24 19:48"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "指出用 AI 时既会过度指导（它其实比你更懂）、也会指导不足（跑偏、带错偏见、缺上下文），如何管理好这份「超能力」是他考察人的第 0 号技能。这把提示与委派能力从技巧提升为核心判断力。"
    url: "https://x.com/rauchg/status/2114085432749347086"
    link_label: "X 原帖"
    time: "10-24 13:03"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "喜欢模型自带的工程黑话——gate、evidence、culprit、durable、provenance、contract——认为这源于大部分工程本质是调试与理解既有系统、做侦探与审计式的取证。他由此追问：高效工作所需的「最小可行英语」到底有多小，甚至可能远少于约 900 词的简化技术英语标准。"
    url: "https://x.com/rauchg/status/2114164830403989880"
    link_label: "X 原帖"
    time: "10-24 18:19"
  - title: "Ryo Lu"
    role: "设计师 @ Cursor"
    summary: "长文《struggle together》反思 AI 抹去「挣扎」后的代价：他靠反复试错学会编程与设计，挣扎沉淀为直觉；如今向机器提问即可得结果，容易跳过理解与提问能力的养成。更深的担忧是人际层面——agent 永远耐心在线，可能让人避开与他人磨合，而最好的合作与友谊正来自共同挣扎；他主张做能让人更多走进世界、找到同伴的工具。"
    url: "https://x.com/ryolu_/status/2114187405251219954"
    link_label: "X 原帖"
    time: "10-24 19:48"
  - title: "Peter Yang"
    role: "Practical AI 教程作者"
    summary: "对 Claude 团队人事变动消息表示难以置信又遗憾，称 Anthony 与 Thariq 是最擅长倾听用户的两个人、对 Claude 用户是重大损失。结合昨日 Thariq 已宣布离开 Anthropic，Claude 核心团队的变动值得用户持续关注。"
    url: "https://x.com/petergyang/status/2114001125636768121"
    link_label: "X 原帖"
    time: "10-24 07:28"
  - title: "Swyx"
    role: "Latent Space"
    summary: "为 Latent Space 新组建的编辑团队招聘写作者、审稿人与记者，并称会把一份材料放入每位新人的入职欢迎包。头部 AI 媒体把编辑团队正规化，显示 AI 内容生产正从个人播客走向机构化。"
    url: "https://x.com/swyx/status/2114145315196711194"
    link_label: "X 原帖"
    time: "10-24 17:01"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "称一篇分享更 eloquent 地表达了他此前提出的演进路径——从 context（上下文）到 harnesses（脚手架/运行框架）再到 judgement（判断力），并公开征集该方向的产品讨论。对在做 agent 基础设施的创业者，这是一个明确的投资兴趣信号。"
    url: "https://x.com/nikunj/status/2113994081345126486"
    link_label: "X 原帖"
    time: "10-24 07:00"
  - title: "Jev: The AI That Makes Decisions, Not Text - and Why It Changes Everything (Diogo Almeida)"
    role: "The MAD Podcast with Matt Turck · 播客"
    summary: "TypeSafe CEO Diogo Almeida 介绍 Jev：它不生成文本，而是输出决策与概率分数，由开发者设阈值触发动作。其主张是把 System-1 式模型与代码、类型安全结合——代码像轨道防止 agent 脱轨，系统可读、可加 eval，因而能可信地在后台运行自动化；高层决策应不断拆解到最低层问题。他还直言预训练是巨大的资源浪费、当前并不在递归自我改进路径上，但 AI 寒冬已被避免，因为不可靠的自动化这一关键短板正在被补上。"
    url: "https://www.youtube.com/@DataDrivenNYC/videos"
    link_label: "节目页"
    time: "10-15 04:30"
---

**X 观点**

- [Aaron Levie（CEO @ Box）](https://x.com/levie/status/2114187326406766604)：预判流经网络安全 agent 的 token 量很快会达到今天的 1000 倍。风险面不断扩大、多数公司已跟不上新风险，agent 集群可扇出调用各种安全工具、测试攻击排列、读日志并评估企业数据风险——这依赖长时运行 agent、computer use 与模型网络安全训练近几个月才成熟。他认为身份、防火墙、网络、代码扫描、数据保护全栈都是机会，也是对攻防平衡保持乐观的理由。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2114085432749347086)：指出用 AI 时既会过度指导（它其实比你更懂）、也会指导不足（跑偏、带错偏见、缺上下文），如何管理好这份「超能力」是他考察人的第 0 号技能。这把提示与委派能力从技巧提升为核心判断力。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2114164830403989880)：喜欢模型自带的工程黑话——gate、evidence、culprit、durable、provenance、contract——认为这源于大部分工程本质是调试与理解既有系统、做侦探与审计式的取证。他由此追问：高效工作所需的「最小可行英语」到底有多小，甚至可能远少于约 900 词的简化技术英语标准。
- [Ryo Lu（设计师 @ Cursor）](https://x.com/ryolu_/status/2114187405251219954)：长文《struggle together》反思 AI 抹去「挣扎」后的代价：他靠反复试错学会编程与设计，挣扎沉淀为直觉；如今向机器提问即可得结果，容易跳过理解与提问能力的养成。更深的担忧是人际层面——agent 永远耐心在线，可能让人避开与他人磨合，而最好的合作与友谊正来自共同挣扎；他主张做能让人更多走进世界、找到同伴的工具。
- [Peter Yang（Practical AI 教程作者）](https://x.com/petergyang/status/2114001125636768121)：对 Claude 团队人事变动消息表示难以置信又遗憾，称 Anthony 与 Thariq 是最擅长倾听用户的两个人、对 Claude 用户是重大损失。结合昨日 Thariq 已宣布离开 Anthropic，Claude 核心团队的变动值得用户持续关注。
- [Swyx（Latent Space）](https://x.com/swyx/status/2114145315196711194)：为 Latent Space 新组建的编辑团队招聘写作者、审稿人与记者，并称会把一份材料放入每位新人的入职欢迎包。头部 AI 媒体把编辑团队正规化，显示 AI 内容生产正从个人播客走向机构化。
- [Nikunj Kothari（Partner @ FPV Ventures）](https://x.com/nikunj/status/2113994081345126486)：称一篇分享更 eloquent 地表达了他此前提出的演进路径——从 context（上下文）到 harnesses（脚手架/运行框架）再到 judgement（判断力），并公开征集该方向的产品讨论。对在做 agent 基础设施的创业者，这是一个明确的投资兴趣信号。

**播客**

- [The MAD Podcast with Matt Turck — Jev: The AI That Makes Decisions, Not Text (Diogo Almeida)](https://www.youtube.com/@DataDrivenNYC/videos)：TypeSafe CEO Diogo Almeida 介绍 Jev：它不生成文本，而是输出决策与概率分数（如某封邮件是否紧急、是否升级，给出 0.85 这类分数），由开发者设阈值触发动作。其主张是把 System-1 式模型与代码、类型安全结合——代码像轨道防止 agent 脱轨，系统可读、可加 eval，因而能可信地在后台运行自动化；高层决策应不断拆解到最低层问题。他还直言预训练是巨大的资源浪费、当前并不在递归自我改进（RSI）路径上，但 AI 寒冬已被避免，因为不可靠的自动化这一关键短板正在被补上；团队隐身两年、坚持少承诺多交付，是其发布走红的原因。

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
