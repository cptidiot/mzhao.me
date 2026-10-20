---
section: ai-builders
section_name: AI Builders
date: 2026-10-20 09:53:00 -0700
title: "AI Builders Digest — 2026-10-20"
excerpt: "Levie 谈模型变强后应用层分化反而扩大、Thariq 劝用 agent 时先聚焦 P0、Vercel 开源 durable HTML artifact builder、Wabi 的群聊与 episodic agent 范式受关注、Every 复盘为何从人手一个 agent 转向一个公司 agent。"
items:
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "提出应用层的一个反直觉判断：模型越强、能做越长任务和工具调用，企业落地的分化反而越大而非越小。过去模型弱时人人只能做 wrapper，如今 agent swarm 协调、领域数据、模型路由和工作流变革管理都可做深，安全、生命科学、医疗、金融、制造会出现此前做不出的专用自治系统；越靠近实验室核心场景，这条路越难走。"
    url: "https://x.com/levie/status/2112404676436222170"
    link_label: "X 原帖"
    time: "10-19 21:44"
  - title: "Thariq"
    role: "Claude Code @ Anthropic"
    summary: "提醒同时用多个 agent 多任务的人放慢节奏：手头大多数事其实不会真正产生影响，先问清自己的 P0 是什么、如果给它全部注意力会做成什么样，再决定要不要并行铺开。agent 用法的关键不在数量而在聚焦。"
    url: "https://x.com/trq212/status/2112219173288120531"
    link_label: "X 原帖"
    time: "10-19 09:27"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "Vercel 开源了一个速度极快的 HTML artifact builder，由 libfx 驱动、让 agent 具备 durable 执行能力。过去为 v0 做防服务器崩溃、防 LLM 不稳定、防函数限额的底层管道非常痛苦，如今这层能力免费开源，几分钟就能做出浮动容器之类的 HTML 效果。"
    url: "https://x.com/rauchg/status/2112247046082363821"
    link_label: "X 原帖"
    time: "10-19 11:18"
  - title: "Garry Tan"
    role: "President & CEO @ Y Combinator"
    summary: "判断 multiplayer agents 以群聊形态落地几乎不可避免，并指出 Wabi 已经把这个形态做出来了——多个 agent 在群聊里协作，而不是各自困在单人对话窗口里。"
    url: "https://x.com/garrytan/status/2112278352514162834"
    link_label: "X 原帖"
    time: "10-19 13:22"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "长文实测 Wabi 2.0 并盛赞其范式：一个 orchestrator 主 agent 加上按主题生成的一次性 episodic chats，可与家人分享、用完即归档（如纽约行程、报税），弥补了单人消息型 agent 难分区、自建多 agent 又永生不死的缺陷；唯一批评是过于主动、App 还需打磨，并声明非广告、非投资关系。"
    url: "https://x.com/nikunj/status/2112219327881761008"
    link_label: "X 原帖"
    time: "10-19 09:28"
  - title: "Why Every Traded Personal Agents for One Company Agent"
    role: "AI & I by Every · 播客"
    summary: "Dan Shipper 与平台负责人 Willie Williams 复盘：全员先一人一个 OpenClaw 个人 agent，确实学到了用法与可见性，但随之而来的是 bot 泛滥、安全与维护负担，多数人的 agent 最终停摆。团队因此把精力收敛到一个全公司共享、越用越懂公司流程的 company agent，并据此对外发布 Every Agent；他们判断职场会走向一公司一 agent，与个人侧的 Dot 类持久 agent 入口并存。"
    url: "https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL"
    link_label: "节目页"
    time: "10-07 10:11"
---

**X 观点**

- [Aaron Levie（Box CEO）](https://x.com/levie/status/2112404676436222170)：提出应用层的一个反直觉判断：模型越强、能做越长任务和工具调用，企业落地的分化反而越大而非越小。过去模型弱时人人只能做 wrapper，如今 agent swarm 协调、领域数据、模型路由和工作流变革管理都可做深，安全、生命科学、医疗、金融、制造会出现此前做不出的专用自治系统；越靠近实验室核心场景，这条路越难走。
- [Thariq（Claude Code @ Anthropic）](https://x.com/trq212/status/2112219173288120531)：提醒同时用多个 agent 多任务的人放慢节奏：手头大多数事其实不会真正产生影响，先问清自己的 P0 是什么、如果给它全部注意力会做成什么样，再决定要不要并行铺开。agent 用法的关键不在数量而在聚焦。
- [Guillermo Rauch（Vercel CEO）](https://x.com/rauchg/status/2112247046082363821)：Vercel 开源了一个速度极快的 HTML artifact builder，由 libfx 驱动、让 agent 具备 durable 执行能力。过去为 v0 做防服务器崩溃、防 LLM 不稳定、防函数限额的底层管道非常痛苦，如今这层能力免费开源，几分钟就能做出浮动容器之类的 HTML 效果。
- [Garry Tan（YC 总裁兼 CEO）](https://x.com/garrytan/status/2112278352514162834)：判断 multiplayer agents 以群聊形态落地几乎不可避免，并指出 Wabi 已经把这个形态做出来了——多个 agent 在群聊里协作，而不是各自困在单人对话窗口里。
- [Nikunj Kothari（FPV Ventures 合伙人）](https://x.com/nikunj/status/2112219327881761008)：长文实测 Wabi 2.0 并盛赞其范式：一个 orchestrator 主 agent 加上按主题生成的一次性 episodic chats，可与家人分享、用完即归档（如纽约行程、报税），弥补了单人消息型 agent 难分区、自建多 agent 又永生不死的缺陷；唯一批评是过于主动、App 还需打磨，并声明非广告、非投资关系。

**播客**

- [AI & I by Every：Why Every Traded Personal Agents for One Company Agent](https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL)：Dan Shipper 与平台负责人 Willie Williams 复盘：全员先一人一个 OpenClaw 个人 agent，确实学到了用法与可见性，但随之而来的是 bot 泛滥、安全与维护负担，多数人的 agent 最终停摆。团队因此把精力收敛到一个全公司共享、越用越懂公司流程的 company agent，并据此对外发布 Every Agent；他们判断职场会走向一公司一 agent，与个人侧的 Dot 类持久 agent 入口并存。

---
内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
