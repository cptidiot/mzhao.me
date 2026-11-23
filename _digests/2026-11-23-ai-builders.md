---
section: ai-builders
section_name: AI Builders
date: 2026-11-23 09:51:00 -0800
title: "AI Builders Digest — 2026-11-23"
excerpt: "困惑度成了今日主角：OpenAI 与 Altman 提议以它作为行业自我监管的通用标尺；另有 agent 成为软件主要用户后的接口分叉、桌面 AI 的安全门槛与“隐形模型”的数据外泄警告，以及一份值得读的创始人收购复盘。"
items:
  - title: "Ryo Lu"
    role: "产品设计师，曾 @ Cursor、Notion、Stripe"
    summary: "他用 @airbuild 几乎一次生成了原生 iOS 应用 ryOS Karaoke：把 iPhone Duo 对折一半，就成了一台迷你卡拉 OK 机。这说明 AI 编程工具已能快速做出可用的原生应用，折叠屏形态也在催生新的产品玩法。"
    url: "https://x.com/ryolu_/status/2124473853858725907"
    link_label: "X 原帖"
    time: "11-22 04:03"
  - title: "Sam Altman"
    role: "CEO @ OpenAI"
    summary: "他提议前沿模型开发者共同制定共享规范：模型首次使用前就建立评估方法与红队安全案例、统一透明度标准，并以困惑度等可跨实验室追踪的指标设定第一道发展上限，只有在理解与监控能力达到具体里程碑（如 CoT 监控的继任者）后才能越过。这是对行业自我监管的一次具体呼吁。"
    url: "https://x.com/sama/status/2124551883130114403"
    link_label: "X 原帖"
    time: "11-22 09:13"
  - title: "Sam Altman"
    role: "CEO @ OpenAI"
    summary: "各实验室已按白宫协议（White House Accords）同意建立标准与最佳实践以提升系统安全，他认为围绕困惑度的讨论能进一步推动这一目标。把困惑度作为行业共同标尺的讨论，正在从 OpenAI 的提议走向多实验室共识。"
    url: "https://x.com/sama/status/2124558713646428663"
    link_label: "X 原帖"
    time: "11-22 09:40"
  - title: "Dan Shipper"
    role: "CEO @ Every"
    summary: "他不常危言耸听，但如果最近的事件真是 AI 辅助网络攻击所致，后果非常严重：只要能干扰飞机对自身重量、剩余燃油与位置的感知，9/11 以来针对人为劫机的整套安全措施就可能失效。他承认自己不是机载系统专家，也指出飞机多有手动 override，但在能见度差时依然极难应对，并请懂行的人补充。"
    url: "https://x.com/danshipper/status/2124567533449613819"
    link_label: "X 原帖"
    time: "11-22 10:15"
  - title: "Swyx"
    role: "AI 工程师，Latent Space 播客主持人"
    summary: "OpenAI 提议用困惑度（perplexity）作为行业自我监管与发展节奏的通用指标，而非 FLOPS 等算力指标。理由是新能力主要随压缩能力的进步而涌现，困惑度能给出与自动化程度无关的通用智能基准；按现有进展推算，进入约 0.68–0.7 对数困惑度区间后还会有变革性能力出现。"
    url: "https://x.com/swyx/status/2124583459356373052"
    link_label: "X 原帖"
    time: "11-22 11:19"
  - title: "Swyx"
    role: "AI 工程师，Latent Space 播客主持人"
    summary: "按困惑度这一指标，今年的 AI 进展已超过 2022–2025 年的总和。他半信半疑：体感上并不觉得如此，可能是算法或指标本身的问题，也可能该指标只在前沿数学层面才成立。对 builders 的提醒是：别只凭体感判断进展速度，基准的选择会直接影响结论。"
    url: "https://x.com/swyx/status/2124590240539259381"
    link_label: "X 原帖"
    time: "11-22 11:46"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "他提醒不要碰打着“免费推理”“ZDR（零数据留存）”旗号的“隐形模型”：这类服务很可能是工业规模的数据外泄通道，把提示词、客户数据与代码送往他国，Dragos 的研究似乎也印证了这一点。Vercel AI Gateway 靠真实 token 量做起来、没走这些捷径。"
    url: "https://x.com/rauchg/status/2124595496849445079"
    link_label: "X 原帖"
    time: "11-22 12:06"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "桌面 AI 应用普遍是安全与隐私噩梦。Replit 与 Windows 合作，为 Replit Desktop 打造了世界级安全模型，也正因此，全球顶级稀有艺术品托管机构佳士得（Christie's）选择了 Replit 做安全的 agent 工作。"
    url: "https://x.com/amasad/status/2124604574606795002"
    link_label: "X 原帖"
    time: "11-22 12:42"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "与其把 AI 指向艺术创作，不如指向“人类可理解性”与概念化：黎曼证明应当附带论文、讲解与新概念、新洞见。就像高级语言的中间表示在 LLM 能直接输出 CPU 指令的世界里依然有价值一样，AI 产出的人类可理解形式本身就是价值。"
    url: "https://x.com/rauchg/status/2124654108124848350"
    link_label: "X 原帖"
    time: "11-22 15:59"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "随着 agent 接手越来越多长期项目工作、成群 agent 并行推进同一目标，编排用的 agent 框架与架构必须进化。最大变化是 agent 群体如何共享知识、跟踪任务并与人类用户协调：既要让 agent 拿到所需资源，又不能给多或给少，还要防范 agent 成为新的安全风险向量。"
    url: "https://x.com/levie/status/2124658150771188157"
    link_label: "X 原帖"
    time: "11-22 16:15"
  - title: "Peter Yang"
    role: "AI 技能与教程博主"
    summary: "他引用微软 Copilot 副总裁 Charles Lamanna 的话：“Agent 是非常挑剔的客户。”当 agent 成为软件主要使用者，它们只认性能、价格与可靠性：人搜索要 10 条链接加摘要，agent 可直接返回一千条结果。API 与用户体验将随之演化，出现更适合 agent 的模式。"
    url: "https://x.com/petergyang/status/2124669298191090033"
    link_label: "X 原帖"
    time: "11-22 17:00"
  - title: "Matt Turck"
    role: "VC @ FirstMark Capital"
    summary: "他调侃：AI 没能解开最难的数学题，VC 又该如何收回那些以 10 亿美元以上投前估值投给尚无产品公司的巨额基金？一句玩笑点出当前 AI 投资的估值压力——天价入场估值需要与之匹配的回报，而技术突破的节奏并不保证。"
    url: "https://x.com/mattturck/status/2124671699245257037"
    link_label: "X 原帖"
    time: "11-22 17:09"
  - title: "Swyx"
    role: "AI 工程师，Latent Space 播客主持人"
    summary: "他推荐一篇从创立到被收购的完整创始人历程复盘，含遗憾与建议，并呼吁更多创始人把自己的经历写下来，能帮后来者少走很多弯路。亮点包括：见顶的 SaaS 市场、IP 归属的坑、别吹自己的 SEO、如何引起 Naval 的注意、招聘与裁员建议，以及如何“钓鱼”促成收购、扫清收购障碍。"
    url: "https://x.com/swyx/status/2124730733147390347"
    link_label: "X 原帖"
    time: "11-22 21:04"
---

# AI Builders Digest — 2026-11-23

## X 观点

**Ryo Lu（产品设计师，曾 @ Cursor、Notion、Stripe）**：他用 @airbuild 几乎一次生成了原生 iOS 应用 ryOS Karaoke：把 iPhone Duo 对折一半，就成了一台迷你卡拉 OK 机。这说明 AI 编程工具已能快速做出可用的原生应用，折叠屏形态也在催生新的产品玩法。[X 原帖](https://x.com/ryolu_/status/2124473853858725907)

**Sam Altman（CEO @ OpenAI）**：他提议前沿模型开发者共同制定共享规范：模型首次使用前就建立评估方法与红队安全案例、统一透明度标准，并以困惑度等可跨实验室追踪的指标设定第一道发展上限，只有在理解与监控能力达到具体里程碑（如 CoT 监控的继任者）后才能越过。这是对行业自我监管的一次具体呼吁。[X 原帖](https://x.com/sama/status/2124551883130114403)

**Sam Altman（CEO @ OpenAI）**：各实验室已按白宫协议（White House Accords）同意建立标准与最佳实践以提升系统安全，他认为围绕困惑度的讨论能进一步推动这一目标。把困惑度作为行业共同标尺的讨论，正在从 OpenAI 的提议走向多实验室共识。[X 原帖](https://x.com/sama/status/2124558713646428663)

**Dan Shipper（CEO @ Every）**：他不常危言耸听，但如果最近的事件真是 AI 辅助网络攻击所致，后果非常严重：只要能干扰飞机对自身重量、剩余燃油与位置的感知，9/11 以来针对人为劫机的整套安全措施就可能失效。他承认自己不是机载系统专家，也指出飞机多有手动 override，但在能见度差时依然极难应对，并请懂行的人补充。[X 原帖](https://x.com/danshipper/status/2124567533449613819)

**Swyx（AI 工程师，Latent Space 播客主持人）**：OpenAI 提议用困惑度（perplexity）作为行业自我监管与发展节奏的通用指标，而非 FLOPS 等算力指标。理由是新能力主要随压缩能力的进步而涌现，困惑度能给出与自动化程度无关的通用智能基准；按现有进展推算，进入约 0.68–0.7 对数困惑度区间后还会有变革性能力出现。他还认为这张图漂亮地讲清了过去四年的故事，后训练的争议只是大情节下的支线。[X 原帖](https://x.com/swyx/status/2124583459356373052)

**Swyx（AI 工程师，Latent Space 播客主持人）**：按困惑度这一指标，今年的 AI 进展已超过 2022–2025 年的总和。他半信半疑：体感上并不觉得如此，可能是算法或指标本身的问题，也可能该指标只在前沿数学层面才成立。对 builders 的提醒是：别只凭体感判断进展速度，基准的选择会直接影响结论。[X 原帖](https://x.com/swyx/status/2124590240539259381)

**Guillermo Rauch（CEO @ Vercel）**：他提醒不要碰那些打着“免费推理”“ZDR（零数据留存）”旗号的“隐形模型”：这类服务很可能是工业规模的数据外泄通道，把提示词、客户数据与代码送往他国，Dragos 的研究似乎也印证了这一点。Vercel AI Gateway 靠真实 token 量做起来、没走这些捷径，他还预告明天会讲如何进一步提高信任、隐私与安全标准。[X 原帖](https://x.com/rauchg/status/2124595496849445079)

**Amjad Masad（CEO @ Replit）**：桌面 AI 应用普遍是安全与隐私噩梦。Replit 与 Windows 合作，为 Replit Desktop 打造了世界级安全模型，也正因此，全球顶级稀有艺术品托管机构佳士得（Christie's）选择了 Replit 做安全的 agent 工作。对 builders 的启示：桌面 agent 的安全模型正在成为赢得高信任客户的关键。[X 原帖](https://x.com/amasad/status/2124604574606795002)

**Guillermo Rauch（CEO @ Vercel）**：与其把 AI 指向艺术创作，不如指向“人类可理解性”与概念化：黎曼证明应当附带论文、讲解与新概念、新洞见。就像高级语言的中间表示在 LLM 能直接输出 CPU 指令的世界里依然有价值一样，AI 产出的人类可理解形式本身就是价值。[X 原帖](https://x.com/rauchg/status/2124654108124848350)

**Aaron Levie（CEO @ Box）**：随着 agent 接手越来越多长期项目工作、成群 agent 并行推进同一目标，编排用的 agent 框架与架构必须进化。最大变化之一是 agent 群体如何共享知识、跟踪任务并与人类用户协调：理论上直接，实操复杂——既要让 agent 拿到所需资源，又不能给多或给少；还要借鉴人类协作方式，同时把吞吐量提到远超人类的水平，并防范 agent 成为新的安全风险向量。这是横向与垂直方向都大有机会的下一代 agent 基础设施。[X 原帖](https://x.com/levie/status/2124658150771188157)

**Peter Yang（AI 技能与教程博主）**：他引用微软 Copilot 执行副总裁 Charles Lamanna 的话：“Agent 是非常挑剔的客户。”当 agent 成为软件的主要使用者，它们只认性能、价格与可靠性，不在乎人喜欢的呈现方式：人搜索要 10 条链接加摘要，agent 不在乎，可以直接返回一千条结果。API 与用户体验将随之演化，出现更适合 agent 的模式。对 builders 来说：为 agent 设计接口与为人类设计界面正在分叉。[X 原帖](https://x.com/petergyang/status/2124669298191090033)

**Matt Turck（VC @ FirstMark Capital）**：他调侃：AI 没能解开最难的数学题，VC 又该如何收回那些以 10 亿美元以上投前估值投给尚无产品公司的巨额基金？一句玩笑点出当前 AI 投资的估值压力——天价入场估值需要与之匹配的回报，而技术突破的节奏并不保证。[X 原帖](https://x.com/mattturck/status/2124671699245257037)

**Swyx（AI 工程师，Latent Space 播客主持人）**：他推荐一篇从创立到被收购的完整创始人历程复盘，含遗憾与建议，并呼吁更多创始人把自己的经历写下来，能帮后来者少走很多弯路。亮点包括：All-In 播客眼中见顶的 SaaS 市场、IP 归属的坑、别吹自己的 SEO、如何引起 Naval 的注意、招聘与裁员建议、如何“钓鱼”促成收购、如何扫清收购障碍，以及“CTO 教练”这种存在。[X 原帖](https://x.com/swyx/status/2124730733147390347)

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
