---
section: ai-builders
section_name: AI Builders
date: 2026-10-23 09:49:00 -0700
title: "AI Builders Digest — 2026-10-23"
excerpt: "Anthropic 将 Agent Skills 捐给 Agentic AI Foundation、Claude 下周默认开启 auto mode 并在 Google Cloud GA，Vercel 呼吁终结静态凭据，David Silver 谈从经验中学习的 superlearner。"
items:
  - title: "Boris Cherny"
    role: "Claude Code @ Anthropic"
    summary: "Agent Skills 最初只是 Claude Code 里的一个实验，如今已被业界广泛采用，Anthropic 因此决定把它捐给 Agentic AI Foundation，与 MCP 并列。这意味着 Skills 正从单一产品功能变成开放生态的公共基础设施，agent 能力的封装与分发开始标准化。"
    url: "https://x.com/bcherny/status/2113333859907747871"
    link_label: "X 原帖"
    time: "10-22 11:17"
  - title: "Claude"
    role: "Anthropic 官方"
    summary: "从下周起，Claude 网页、桌面与移动端在 Pro、Max 与 Team 套餐上将默认开启 auto mode——不再逐步请用户批准，而是由自动检查拦截有风险的操作，用户随时可切回手动。这把 agent 的默认交互从「每步确认」推向「放手执行、风险兜底」。"
    url: "https://x.com/claudeai/status/2113360845409583307"
    link_label: "X 原帖"
    time: "10-22 13:04"
  - title: "Claude"
    role: "Anthropic 官方"
    summary: "Claude Models on Google Cloud（Anthropic 托管）正式 GA，可在 Google Cloud 上用全套 Claude Platform 功能，并使用 Google Cloud 的 IAM 凭据、计费与承诺抵扣；同线程还称新功能与 beta 会在原生平台上线当天同步到达，包括 Opus 5.5 的 Fast mode、代码执行与 Skills API。企业上云的采购与合规路径因此更顺。"
    url: "https://x.com/claudeai/status/2113380122468454765"
    link_label: "X 原帖"
    time: "10-22 14:21"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "在他的「Day 18」清单里，Decisions API 已 GA、OpenResponses 加入 Linux Foundation、团队发布了性能改进，Uber 正全面采用 Codex 与 Work。清单之外他还预告当天有一次 reset，并另发帖称次日上午 10 点（PST）前会有新品落地——具体内容帖中未说明。"
    url: "https://x.com/thsottiaux/status/2113492187770175603"
    link_label: "X 原帖"
    time: "10-22 21:46"
  - title: "Swyx"
    role: "Latent Space"
    summary: "称 Opus 5.5 是他用过的最好的工作量估算模型，并强调这种「校准」在人类越来越多地把工作委派给 AI 时愈发重要——不要按人类要花 2–3 个工作日的口径报时，一个不知疲倦且可大规模并行的系统应该能在 2–3 小时内完成。估算口径不改，委派的排期就会系统性失真。"
    url: "https://x.com/swyx/status/2113283272130412684"
    link_label: "X 原帖"
    time: "10-22 07:56"
  - title: "Swyx"
    role: "Latent Space"
    summary: "对 AI 找出代码 bug 的态度表态：不要怪 AI 发现了 bug，而是立刻锁定、尽快把 bug 全部清掉。在他看来，AI 扩大了可发现的问题面，团队的瓶颈随之从「发现问题」转向「处理问题的速度与决心」。"
    url: "https://x.com/swyx/status/2113359027682050352"
    link_label: "X 原帖"
    time: "10-22 12:57"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "主张终结「静态凭据」：攻击与泄露难以避免，但如果窃贼偷到的只是会自毁的短期密钥，损失就能被大幅限制。他呼吁业界像当年合力让每个网站都用上 TLS（绿色锁）一样，再合力把 OIDC 推进到同样普及的位置。"
    url: "https://x.com/rauchg/status/2113399539227136084"
    link_label: "X 原帖"
    time: "10-22 15:38"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "用本周一桩安全事件作对比：普通人把密码「P4ssword!」写在厨房便利贴上，而守护互联网加密的 steward 们用的密钥口令竟只是「4」——这把密钥可被用来针对并解密近乎一切内容，残余风险仍在清理中。他以此提醒，关键基础设施的密钥管理薄弱程度可能远超外界想象。"
    url: "https://x.com/rauchg/status/2113462657059639505"
    link_label: "X 原帖"
    time: "10-22 19:48"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "称一个 Generative UI 案例是他见过最酷的真实应用之一，并点出 Vercel AI Gateway 本身就是一个工具市场：在 AI SDK 里加一行代码接入一个 tool，就能得到「Google」——不只是搜索，还包括天气、体育、股票与选举等结构化能力。工具分发正被平台化、商品化。"
    url: "https://x.com/rauchg/status/2113451268316205515"
    link_label: "X 原帖"
    time: "10-22 19:03"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "断言任何形式的「以隐蔽求安全」（security through obscurity）都已彻底终结——自治系统会翻遍每个角落、试尽每种攻击排列。后果是多年积压的企业遗留基础设施必须升级、安全实践现代化、数据管道清理、访问控制收紧；agent 在防御侧能加速这项工作并模拟风险向量，但他提醒准备期很长，这也是 AI 扩散时间线会比一些人预期的更久的原因之一。"
    url: "https://x.com/levie/status/2113499900399034689"
    link_label: "X 原帖"
    time: "10-22 22:16"
  - title: "Alex Albert"
    role: "Research @ Anthropic"
    summary: "提出一个他很想试的副线：用 AI 帮着经营一批本地小生意。他判断像 Claude Duet 这类产品对小生意的意义，最终可能比 Square 或 Google Maps 还大——AI 从「工具供应商」变成小微经营者的实际运营帮手，值得持续观察。"
    url: "https://x.com/alexalbert__/status/2113386454907007444"
    link_label: "X 原帖"
    time: "10-22 14:46"
  - title: "Matt Turck"
    role: "Partner @ FirstMark Capital"
    summary: "发布与 Mistral AI 研究负责人 Pierre Stock 的对话，主线是「Mistral 强势回归」：其开放模型 Le Chonk 被称为西方最大的开放模型，节目谈到 Mistral 在自有数据中心用 3,800 张 GPU 训练、Meta 把最强模型保持闭源而 Mistral 选择开放 Chonk，以及与 Beam、Muse Spark Open 和中国模型的对比。西方开放权重的竞争格局值得跟踪。"
    url: "https://x.com/mattturck/status/2113311361639829673"
    link_label: "X 原帖"
    time: "10-22 09:47"
  - title: "Matt Turck"
    role: "Partner @ FirstMark Capital"
    summary: "一句话概括 AI 产业的竞争形态：所有人都在与所有人竞争——芯片厂商与推理商竞争，推理商与 neo-cloud 和后训练竞争，模型与应用和芯片竞争，应用又与模型竞争；只有 NVIDIA 是卖给所有人的。理解任何一家 AI 公司的处境，都要放在这张全向竞争的图里看。"
    url: "https://x.com/mattturck/status/2113263905950568730"
    link_label: "X 原帖"
    time: "10-22 06:39"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "自述他见过的种子公司里约有 10% 在初次见面后几个月内就被收购，并判断 seed 到 Series A 的挤压已达历史最高、短期不会缓解——「从未如此容易做梦，也从未如此难以规模化」。他预告下周将就此发表长文，对早期创业的融资预期是一记提醒。"
    url: "https://x.com/nikunj/status/2113405034826477910"
    link_label: "X 原帖"
    time: "10-22 16:00"
  - title: "Aditya Agarwal"
    role: "General Partner @ SPC"
    summary: "指出机器人领域正在重演 LLM 的范式迁移：从微调，到提示，再到直接用自然语言告诉模型想要什么。他举 Sergey Levine 的分享为例——Physical Intelligence 的 π0.7 能从纯语言教练式指导中学会新技能，机器人学习的人机接口正在变得像对话一样自然。"
    url: "https://x.com/adityaag/status/2113385971844518124"
    link_label: "X 原帖"
    time: "10-22 14:44"
  - title: "Madhu Guru"
    role: "Sr Director, AI @ Meta"
    summary: "给在 AI 变局中感到卡住的 PM 的建议：不要等清晰，先用行动创造清晰。许多人想转 AI 却不知从何开始、又心存恐惧，而惯性恰恰杀死清晰——做点东西、自动化一个流程、去连接能启发你的人，每次行动都会带来经验、反馈与新想法，清晰往往是行动的结果。"
    url: "https://x.com/realmadhuguru/status/2113437016818057641"
    link_label: "X 原帖"
    time: "10-22 18:07"
  - title: "David Silver and Lasse Espeholt of Ineffable Intelligence: A Superlearner for the Age of Experience"
    role: "Training Data · 播客"
    summary: "AlphaGo 核心人物 David Silver 与 Lasse Espeholt 谈新公司 Ineffable Intelligence 的信念：不走 LLM 的人类数据路线，而是让系统像人类集体发现语言、科学与数学那样，从经验中通过强化学习持续自我发现、永不停歇地学习——他们称之为「superlearner」，并认为这才是通向超级智能的本质。Silver 回顾了自 2009 年围棋博士研究以来始终未变的信念，并给出时间表判断：一年内会看到方法奏效的强证据，他原估 3–5 年、现因 coding agent 加速而收紧到约 3 年实现其定义的超级智能；公司刻意保持研究主导、抵御产品压力，认为突破的下游价值远大于增量产品。"
    url: "https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8"
    link_label: "节目页"
    time: "10-13 02:00"
---

**X 观点**

- [Boris Cherny（Claude Code @ Anthropic）](https://x.com/bcherny/status/2113333859907747871)：Agent Skills 最初只是 Claude Code 里的一个实验，如今已被业界广泛采用，Anthropic 因此决定把它捐给 Agentic AI Foundation，与 MCP 并列。这意味着 Skills 正从单一产品功能变成开放生态的公共基础设施，agent 能力的封装与分发开始标准化。
- [Claude（Anthropic 官方）](https://x.com/claudeai/status/2113360845409583307)：从下周起，Claude 网页、桌面与移动端在 Pro、Max 与 Team 套餐上将默认开启 auto mode——不再逐步请用户批准，而是由自动检查拦截有风险的操作，用户随时可切回手动。这把 agent 的默认交互从「每步确认」推向「放手执行、风险兜底」。
- [Claude（Anthropic 官方）](https://x.com/claudeai/status/2113380122468454765)：Claude Models on Google Cloud（Anthropic 托管）正式 GA，可在 Google Cloud 上用全套 Claude Platform 功能，并使用 Google Cloud 的 IAM 凭据、计费与承诺抵扣；同线程还称新功能与 beta 会在原生平台上线当天同步到达，包括 Opus 5.5 的 Fast mode、代码执行与 Skills API。企业上云的采购与合规路径因此更顺。
- [Thibault Sottiaux（Codex & ChatGPT @ OpenAI）](https://x.com/thsottiaux/status/2113492187770175603)：在他的「Day 18」清单里，Decisions API 已 GA、OpenResponses 加入 Linux Foundation、团队发布了性能改进，Uber 正全面采用 Codex 与 Work。清单之外他还预告当天有一次 reset，并另发帖称次日上午 10 点（PST）前会有新品落地——具体内容帖中未说明。
- [Swyx（Latent Space）](https://x.com/swyx/status/2113283272130412684)：称 Opus 5.5 是他用过的最好的工作量估算模型，并强调这种「校准」在人类越来越多地把工作委派给 AI 时愈发重要——不要按人类要花 2–3 个工作日的口径报时，一个不知疲倦且可大规模并行的系统应该能在 2–3 小时内完成。估算口径不改，委派的排期就会系统性失真。
- [Swyx（Latent Space）](https://x.com/swyx/status/2113359027682050352)：对 AI 找出代码 bug 的态度表态：不要怪 AI 发现了 bug，而是立刻锁定、尽快把 bug 全部清掉。在他看来，AI 扩大了可发现的问题面，团队的瓶颈随之从「发现问题」转向「处理问题的速度与决心」。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2113399539227136084)：主张终结「静态凭据」：攻击与泄露难以避免，但如果窃贼偷到的只是会自毁的短期密钥，损失就能被大幅限制。他呼吁业界像当年合力让每个网站都用上 TLS（绿色锁）一样，再合力把 OIDC 推进到同样普及的位置。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2113462657059639505)：用本周一桩安全事件作对比：普通人把密码「P4ssword!」写在厨房便利贴上，而守护互联网加密的 steward 们用的密钥口令竟只是「4」——这把密钥可被用来针对并解密近乎一切内容，残余风险仍在清理中。他以此提醒，关键基础设施的密钥管理薄弱程度可能远超外界想象。
- [Guillermo Rauch（CEO @ Vercel）](https://x.com/rauchg/status/2113451268316205515)：称一个 Generative UI 案例是他见过最酷的真实应用之一，并点出 Vercel AI Gateway 本身就是一个工具市场：在 AI SDK 里加一行代码接入一个 tool，就能得到「Google」——不只是搜索，还包括天气、体育、股票与选举等结构化能力。工具分发正被平台化、商品化。
- [Aaron Levie（CEO @ Box）](https://x.com/levie/status/2113499900399034689)：断言任何形式的「以隐蔽求安全」（security through obscurity）都已彻底终结——自治系统会翻遍每个角落、试尽每种攻击排列。后果是多年积压的企业遗留基础设施必须升级、安全实践现代化、数据管道清理、访问控制收紧；agent 在防御侧能加速这项工作并模拟风险向量，但他提醒准备期很长，这也是 AI 扩散时间线会比一些人预期的更久的原因之一。
- [Alex Albert（Research @ Anthropic）](https://x.com/alexalbert__/status/2113386454907007444)：提出一个他很想试的副线：用 AI 帮着经营一批本地小生意。他判断像 Claude Duet 这类产品对小生意的意义，最终可能比 Square 或 Google Maps 还大——AI 从「工具供应商」变成小微经营者的实际运营帮手，值得持续观察。
- [Matt Turck（Partner @ FirstMark Capital）](https://x.com/mattturck/status/2113311361639829673)：发布与 Mistral AI 研究负责人 Pierre Stock 的对话，主线是「Mistral 强势回归」：其开放模型 Le Chonk 被称为西方最大的开放模型，节目谈到 Mistral 在自有数据中心用 3,800 张 GPU 训练、Meta 把最强模型保持闭源而 Mistral 选择开放 Chonk，以及与 Beam、Muse Spark Open 和中国模型的对比。西方开放权重的竞争格局值得跟踪。
- [Matt Turck（Partner @ FirstMark Capital）](https://x.com/mattturck/status/2113263905950568730)：一句话概括 AI 产业的竞争形态：所有人都在与所有人竞争——芯片厂商与推理商竞争，推理商与 neo-cloud 和后训练竞争，模型与应用和芯片竞争，应用又与模型竞争；只有 NVIDIA 是卖给所有人的。理解任何一家 AI 公司的处境，都要放在这张全向竞争的图里看。
- [Nikunj Kothari（Partner @ FPV Ventures）](https://x.com/nikunj/status/2113405034826477910)：自述他见过的种子公司里约有 10% 在初次见面后几个月内就被收购，并判断 seed 到 Series A 的挤压已达历史最高、短期不会缓解——「从未如此容易做梦，也从未如此难以规模化」。他预告下周将就此发表长文，对早期创业的融资预期是一记提醒。
- [Aditya Agarwal（General Partner @ SPC）](https://x.com/adityaag/status/2113385971844518124)：指出机器人领域正在重演 LLM 的范式迁移：从微调，到提示，再到直接用自然语言告诉模型想要什么。他举 Sergey Levine 的分享为例——Physical Intelligence 的 π0.7 能从纯语言教练式指导中学会新技能，机器人学习的人机接口正在变得像对话一样自然。
- [Madhu Guru（Sr Director, AI @ Meta）](https://x.com/realmadhuguru/status/2113437016818057641)：给在 AI 变局中感到卡住的 PM 的建议：不要等清晰，先用行动创造清晰。许多人想转 AI 却不知从何开始、又心存恐惧，而惯性恰恰杀死清晰——做点东西、自动化一个流程、去连接能启发你的人，每次行动都会带来经验、反馈与新想法，清晰往往是行动的结果。

**播客**

- [Training Data：David Silver and Lasse Espeholt of Ineffable Intelligence: A Superlearner for the Age of Experience](https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8)：AlphaGo 核心人物 David Silver 与 Lasse Espeholt 谈新公司 Ineffable Intelligence 的信念：不走 LLM 的人类数据路线，而是让系统像人类集体发现语言、科学与数学那样，从经验中通过强化学习持续自我发现、永不停歇地学习——他们称之为「superlearner」，并认为这才是通向超级智能的本质。Silver 回顾了自 2009 年围棋博士研究以来始终未变的信念，并给出时间表判断：一年内会看到方法奏效的强证据，他原估 3–5 年、现因 coding agent 加速而收紧到约 3 年实现其定义的超级智能；公司刻意保持研究主导、抵御产品压力，认为突破的下游价值远大于增量产品。

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
