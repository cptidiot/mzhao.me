---
section: ai-builders
section_name: AI Builders
date: 2026-10-21 09:52:16 -0700
title: "AI Builders Digest — 2026-10-21"
excerpt: "Levie 谈面向领域的自治系统新形态、OpenAI 缓存升级与用量口径致歉、Vercel 把 harness durability 开源、Steinberger 的多 agent 工作流实测。"
items:
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "一种新形态正在成形——面向特定任务或领域的自治系统，远超 LLM wrapper 时代。三股力量在汇合：工具与 computer use 让 agent 能细粒度接入外部系统、没现成软件就自己造；模型在法律、生物研究、代码安全、供应链等垂直领域的判断力在变强；sandbox、文件系统、数据管道等 harness 基础设施让长时运行与大规模处理成为可能。配上 UX 与变革管理，这类系统将进入 IT 自动化、网络作战、药物发现、制造、AI 研究等场景，几乎每个岗位都会有对应系统。"
    url: "https://x.com/levie/status/2112769686798832013"
    link_label: "X 原帖"
    time: "10-20 21:55"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "缓存升级——API 现可缓存 12 小时；登录用户在 Codex 与 Work 里的缓存永久保留，隔几小时回来、恢复旧对话都保证命中缓存、不再有惩罚。对长会话与断点续跑的成本和延迟是直接利好。"
    url: "https://x.com/thsottiaux/status/2112712984644784534"
    link_label: "X 原帖"
    time: "10-20 18:10"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "周末有用户反映用量掉得比预期快，OpenAI 查出约 4 万个账户的用量口径不一致——实际适用的用量与用户所选套餐不符。问题已修正，团队正逐一联系受影响用户并补 credits，他为此公开致歉。"
    url: "https://x.com/thsottiaux/status/2112592264686149749"
    link_label: "X 原帖"
    time: "10-20 10:10"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "Vercel 要把 harness durability 做成像 AI SDK 那样真正开源、与 runtime 无关：把支撑 eve 与 Workflows 的持久化基础设施开放给 Pi、OpenCode 等所有 harness，本地、Vercel 或自托管都行。连 Claude Code 和 Codex 也能这样变得 durable 且可观测，只是它们并非为嵌入而设计，效率与便携性较差，还多一层 sandbox 要求。"
    url: "https://x.com/rauchg/status/2112658577110520122"
    link_label: "X 原帖"
    time: "10-20 14:33"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "谈 AI 教育的终局：AI 能精确算出你懂与不懂之间的 delta，据此循序渐进地教你任何想法、解开任何谜题；只要你愿意，就能达到自身能力与智力的上限——这是终极教育，而且免费。"
    url: "https://x.com/rauchg/status/2112638107749355867"
    link_label: "X 原帖"
    time: "10-20 13:12"
  - title: "Sam Altman"
    role: "OpenAI"
    summary: "表示很感激 Aleksander 接受 OpenAI 的邀请来接手这件事：在迈向超级智能的路上，安全与安保挑战巨大，而 Aleksander 的技能组合正适合应对这些挑战。"
    url: "https://x.com/sama/status/2112652656602923366"
    link_label: "X 原帖"
    time: "10-20 14:10"
  - title: "Josh Woodward"
    role: "VP @ Google Labs / Gemini App"
    summary: "Gemini App 的 Trusted Tester 社区刚跨过一个里程碑——想在 Web、Android、iOS 上抢先试新功能的人很多；此前报过名的已全部进入，没报名的可新登记。对想跟 Gemini 新功能灰度节奏的人，这是一个开放的早鸟通道。"
    url: "https://x.com/joshwoodward/status/2112676777290248675"
    link_label: "X 原帖"
    time: "10-20 15:46"
  - title: "Swyx"
    role: "Latent Space"
    summary: "吐槽模型护栏对生产力的伤害：Opus 写东西很好，前提是 prompt 里别碰巧出现随机的「禁词」；他认同「give me prod, not god」，直言没法把这种不可预测的拦截放在 AI 媒体组织的关键路径上——内容型产品选型时，拒答的不确定性本身就是成本。"
    url: "https://x.com/swyx/status/2112772374823407870"
    link_label: "X 原帖"
    time: "10-20 22:06"
  - title: "Peter Steinberger"
    role: "OpenClaw"
    summary: "分享多 agent 工作流实测：让 Astra 做规划、Sol 6.1 写代码，提示 Astra 在 worktrees 里跑 Codex CLI，效果远好于依赖 subagents；再加一个监督 agent 专门挑战、防止跑偏，类似 /goal 但审查者是独立 agent 而非同一 agent 读文本文件。他为此写了一个叫「smart goal」的 OpenClaw 插件。"
    url: "https://x.com/steipete/status/2112605703219347503"
    link_label: "X 原帖"
    time: "10-20 11:03"
  - title: "Aditya Agarwal"
    role: "General Partner @ SPC"
    summary: "一个类比：Inference-time scaling → Subagents → Agent Swarms 的演进，像极了 CPU Threads → 多核 CPU → 多节点分布式系统的历史——架构史在 agent 领域重演，多 agent 协调终将面对分布式系统的老问题。"
    url: "https://x.com/adityaag/status/2112579526379401408"
    link_label: "X 原帖"
    time: "10-20 09:19"
  - title: "Zara Zhang"
    role: "Builder"
    summary: "早期产品 builder 手握自有受众的最大优势其实不是分发，而是信号：能快速测试不同想法和角度、看什么能引起共鸣，并找到第一批 100 个早期用户。Signals > distribution。"
    url: "https://x.com/zarazhangrui/status/2112530473994072225"
    link_label: "X 原帖"
    time: "10-20 06:04"
---

**X 观点**

- [Aaron Levie（Box CEO）](https://x.com/levie/status/2112769686798832013)：一种新形态正在成形——面向特定任务或领域的自治系统，远超 LLM wrapper 时代。三股力量在汇合：工具与 computer use 让 agent 能细粒度接入外部系统、没现成软件就自己造；模型在法律、生物研究、代码安全、供应链等垂直领域的判断力在变强；sandbox、文件系统、数据管道等 harness 基础设施让长时运行与大规模处理成为可能。配上 UX 与变革管理，这类系统将进入 IT 自动化、网络作战、药物发现、制造、AI 研究等场景，几乎每个岗位都会有对应系统。
- [Thibault Sottiaux（OpenAI，Codex & ChatGPT）](https://x.com/thsottiaux/status/2112712984644784534)：缓存升级——API 现可缓存 12 小时；登录用户在 Codex 与 Work 里的缓存永久保留，隔几小时回来、恢复旧对话都保证命中缓存、不再有惩罚。对长会话与断点续跑的成本和延迟是直接利好。
- [Thibault Sottiaux（OpenAI，Codex & ChatGPT）](https://x.com/thsottiaux/status/2112592264686149749)：周末有用户反映用量掉得比预期快，OpenAI 查出约 4 万个账户的用量口径不一致——实际适用的用量与用户所选套餐不符。问题已修正，团队正逐一联系受影响用户并补 credits，他为此公开致歉。
- [Guillermo Rauch（Vercel CEO）](https://x.com/rauchg/status/2112658577110520122)：Vercel 要把 harness durability 做成像 AI SDK 那样真正开源、与 runtime 无关：把支撑 eve 与 Workflows 的持久化基础设施开放给 Pi、OpenCode 等所有 harness，本地、Vercel 或自托管都行。连 Claude Code 和 Codex 也能这样变得 durable 且可观测，只是它们并非为嵌入而设计，效率与便携性较差，还多一层 sandbox 要求。
- [Guillermo Rauch（Vercel CEO）](https://x.com/rauchg/status/2112638107749355867)：谈 AI 教育的终局：AI 能精确算出你懂与不懂之间的 delta，据此循序渐进地教你任何想法、解开任何谜题；只要你愿意，就能达到自身能力与智力的上限——这是终极教育，而且免费。
- [Sam Altman（OpenAI）](https://x.com/sama/status/2112652656602923366)：表示很感激 Aleksander 接受 OpenAI 的邀请来接手这件事：在迈向超级智能的路上，安全与安保挑战巨大，而 Aleksander 的技能组合正适合应对这些挑战。
- [Josh Woodward（Google VP，Google Labs / Gemini App）](https://x.com/joshwoodward/status/2112676777290248675)：Gemini App 的 Trusted Tester 社区刚跨过一个里程碑——想在 Web、Android、iOS 上抢先试新功能的人很多；此前报过名的已全部进入，没报名的可新登记。对想跟 Gemini 新功能灰度节奏的人，这是一个开放的早鸟通道。
- [Swyx（Latent Space）](https://x.com/swyx/status/2112772374823407870)：吐槽模型护栏对生产力的伤害：Opus 写东西很好，前提是 prompt 里别碰巧出现随机的「禁词」；他认同「give me prod, not god」，直言没法把这种不可预测的拦截放在 AI 媒体组织的关键路径上——内容型产品选型时，拒答的不确定性本身就是成本。
- [Peter Steinberger（OpenClaw）](https://x.com/steipete/status/2112605703219347503)：分享多 agent 工作流实测：让 Astra 做规划、Sol 6.1 写代码，提示 Astra 在 worktrees 里跑 Codex CLI，效果远好于依赖 subagents；再加一个监督 agent 专门挑战、防止跑偏，类似 /goal 但审查者是独立 agent 而非同一 agent 读文本文件。他为此写了一个叫「smart goal」的 OpenClaw 插件。
- [Aditya Agarwal（SPC 合伙人、前 Dropbox CTO）](https://x.com/adityaag/status/2112579526379401408)：一个类比：Inference-time scaling → Subagents → Agent Swarms 的演进，像极了 CPU Threads → 多核 CPU → 多节点分布式系统的历史——架构史在 agent 领域重演，多 agent 协调终将面对分布式系统的老问题。
- [Zara Zhang（Builder）](https://x.com/zarazhangrui/status/2112530473994072225)：早期产品 builder 手握自有受众的最大优势其实不是分发，而是信号：能快速测试不同想法和角度、看什么能引起共鸣，并找到第一批 100 个早期用户。Signals > distribution。

---
内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
