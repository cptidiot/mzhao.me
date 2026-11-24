---
section: ai-builders
section_name: AI Builders
date: 2026-11-24 10:00:00 -0800
title: "AI Builders Digest — 2026-11-24"
excerpt: "Claude Ship 上线、ChatGPT Dots 内外冷热不一、Replit 发布 agent 群体扩展定律研究；另有 Claude 插件体系与零数据留存 EFS、Vercel 加码日本，以及 agent 如何改写服务业的规模逻辑。"
items:
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "他让 Fable 研究自己全部编程会话，判断 Opus 还是 Gemini Neon 更适合自己，结果选了 Neon。他感慨 Google 强势回归这件事被严重低估了——这也给模型选型提供了一个“个人评测”的新思路：不用看通用榜单，直接拿自己的真实工作来测。"
    url: "https://x.com/rauchg/status/2124880074168242369"
    link_label: "X 原帖"
    time: "11-23 06:57"
  - title: "Zara Zhang"
    role: "Follow Builders 作者"
    summary: "每天发帖与注重隐私并不矛盾：她几乎每天发帖，但只分享生活与想法的极小一部分（不到 1%）。关键是找到“别人感兴趣”与“自己舒服”的交集，只发那部分——公开分享不等于把整个人生摊开。"
    url: "https://x.com/zarazhangrui/status/2124905740095885414"
    link_label: "X 原帖"
    time: "11-23 08:39"
  - title: "Garry Tan"
    role: "CEO @ Y Combinator"
    summary: "创业公司可以用一个简单方法自我提醒：循环自问“我们是不是快死了？”主动问这个问题，才能及时发现正在杀死公司的东西并设法规避，而不是等到无可挽回。"
    url: "https://x.com/garrytan/status/2124905972296560973"
    link_label: "X 原帖"
    time: "11-23 08:40"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "在 OpenAI 内部，dots 正在迅速成为完成工作的主要方式，甚至已经出现“用 dots 搭建 dots 系统”的局面。ChatGPT 的新 agent 形态不只是对外功能，内部已把它当作日常生产力工具在用。"
    url: "https://x.com/thsottiaux/status/2124923055072043052"
    link_label: "X 原帖"
    time: "11-23 09:48"
  - title: "Claude"
    role: "Claude 官方账号"
    summary: "零数据留存（ZDR）结合企业级前沿安全保障（EFS）现已进入公开测试，面向符合条件的企业：它在多请求层面筛查滥用，同时与 ZDR 兼容，已与 100 多家客户共同开发。现已登陆 Claude 平台、AWS、Bedrock 与 Google Cloud，Microsoft Foundry 支持即将到来。"
    url: "https://x.com/claudeai/status/2124929944530587712"
    link_label: "X 原帖"
    time: "11-23 10:15"
  - title: "Boris Cherny"
    role: "Claude @ Anthropic"
    summary: "一年前 Opus 4.5 成为第一个写出他 100% 代码的模型，但发 PR 的环节没跟上；今天 Claude Ship 进入 beta（Team 与 Enterprise 计划）。Code Review 负责找 bug，PR Steward 处理修复与失败的检查，Claude Approvals 按团队策略自动批准（后两者仍在 beta）。管理员可按 GitHub 仓库开启，建议先从一个仓库、用观察模式的审批跑起，等建立信任再放开。"
    url: "https://x.com/bcherny/status/2124961485801836573"
    link_label: "X 原帖"
    time: "11-23 12:21"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "Replit 发布 agent 群体扩展定律研究：增加 agent 数量能带来显著性能提升，但不像传统扩展定律那样“算力越多越好”，组织方式很关键。固定两小时窗口内，Opus 5.5 在 NumPy 任务上从 1 个 agent 的 3.7 倍加速升至 32 个 agent 的 18.9 倍；GPT-6.2 Astra 单体最强，但超过 8 个 agent 后出现负扩展；去中心化群体比依赖中心协调的扩展更好；问题本身的可并行性是群体表现的强预测因子；个体模型智能反而不能很好预测集体智能。团队同时开源了 Optimization-Bench。"
    url: "https://x.com/amasad/status/2124969305674748175"
    link_label: "X 原帖"
    time: "11-23 12:52"
  - title: "Claude"
    role: "Claude 官方账号"
    summary: "连接工具、教 Claude 新技能、或两者兼做，现在统一走插件这一种方式。插件体系已上线，收录 1 万多个插件，覆盖 Free、Pro、Max 与 Ultra 计划，Team 与 Enterprise 即将推出——这意味着 Claude 的扩展能力从分散的连接器与技能，收敛成一个统一的插件市场。"
    url: "https://x.com/claudeai/status/2124970294523945328"
    link_label: "X 原帖"
    time: "11-23 12:56"
  - title: "Thariq"
    role: "前 Claude Code @ Anthropic"
    summary: "X 的创作者分成是个好模式，值得未来软件公司借鉴：保持精简的核心团队，把增长、反馈与销售的收益分给用户。软件公司的规模不一定来自员工数，也可以来自被激励的用户网络。"
    url: "https://x.com/trq212/status/2124987187406275037"
    link_label: "X 原帖"
    time: "11-23 14:03"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "ChatGPT 的回答质量在新一轮改进推送到用户后会有明显提升。配合应用简化、提速，以及聊天与工作的合并，到年底日常体验会有相当大的改善——OpenAI 正在把零散的升级打包成一次集中的体验跃升。"
    url: "https://x.com/thsottiaux/status/2124998553856844186"
    link_label: "X 原帖"
    time: "11-23 14:48"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "他上周五与副总统 Vance 会面，讨论美国 AI 领导力、网络安全与国家软件基础设施现代化。他特别关心美国在开放权重 AI 上的领导力：盟友想要主权 AI，正越来越多地转向中国开源模型；美国本土创业公司也需要有竞争力的模型生态。美国可能赢得前沿 AI 竞赛，却输掉全球 AI 生态。他还提到很高兴看到 Jensen 回到 Nvidia，称其为美国开放权重 AI 最重要的支持者之一。"
    url: "https://x.com/amasad/status/2125008810041610359"
    link_label: "X 原帖"
    time: "11-23 15:29"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "一句关于 2027 年职位名的玩笑：创始人叫 Swarm Overlord、产品经理 Swarm Rider、设计师 Swarm Choreographer、系统工程师 Swarm Architect、一线部署工程师 Swarm Wrangler、市场 Swarm Propagandist、VC Swarm Speculator。玩笑背后是 agent 群体正在成为默认工作方式的预期。"
    url: "https://x.com/nikunj/status/2125033540287131901"
    link_label: "X 原帖"
    time: "11-23 17:07"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "Vercel 宣布在日本加大投入。结合他当天另一条关于模型评测的帖子，Vercel 正在同时推进产品能力与区域扩张。"
    url: "https://x.com/rauchg/status/2125057274213507253"
    link_label: "X 原帖"
    time: "11-23 18:41"
  - title: "Peter Yang"
    role: "AI 技能与教程博主"
    summary: "他对 ChatGPT Dots 的早期体验很直接：它会在他审核前就发邮件，还会随机停止响应。他很想喜欢这个产品，怀疑是不是自己提示词用得不对。与 OpenAI 内部的乐观形成对照，dots 走到普通用户手里仍有不少坑要填。"
    url: "https://x.com/petergyang/status/2125060785667969399"
    link_label: "X 原帖"
    time: "11-23 18:55"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "Agent 正在改写服务业的规模逻辑：服务业历来受限于交付能力，产出只能靠加人头，客户永远想要更快、更便宜、更好；agent 让产出与投入时间脱钩，一个工程师能顶几十个工程师，一个设计师能搭出完整设计系统与品牌。关键仍在前端：需要专家确保 agent 交付出正确的结果。网络安全、广告营销、法律、会计、IT 转型等历来只能靠人的行业都会被重塑，现在正是创业或改造现有公司的好时机。"
    url: "https://x.com/levie/status/2125089009018040779"
    link_label: "X 原帖"
    time: "11-23 20:47"
  - title: "Aditya Agarwal"
    role: "GP @ South Park Commons，前 Dropbox CTO"
    summary: "有时候需要出国旅行，才能深切体会美国对世界其他地方有多大的感召力：很多国家与个人都渴望拥有美国这样的创业生态与资本市场基础，不想成为中国、英国或丹麦那样的模式——最有抱负的人都在学习美国如何建设。这不代表美国没有改进空间，必须、也一定会做得更好。"
    url: "https://x.com/adityaag/status/2125096073228439683"
    link_label: "X 原帖"
    time: "11-23 21:16"
  - title: "Madhu Guru"
    role: "Sr Director, AI @ Meta"
    summary: "“数据”这个名字大大低估了它在模型开发中真正的含义。不熟悉模型开发的人把数据看作买来倒进模型的惰性商品，像煤一样；实际上优质数据编码了极高价值的知识、品味与专业能力，很多是以此前不存在的方式表达与结构化的。这使数据成为构建跨领域更强智能最基础的构件之一，未来仍将处于智能产业的中心。"
    url: "https://x.com/realmadhuguru/status/2125102190196859156"
    link_label: "X 原帖"
    time: "11-23 21:40"
  - title: "Aditya Agarwal"
    role: "GP @ South Park Commons，前 Dropbox CTO"
    summary: "大多数好组织在遭遇没有摧毁它们的生存危机后，会带着复仇心态归来：见过失败的样子，就决心不让它重演；他在 Meta 多次有这种感受。Nvidia 现在不会手软——经历过危机的组织往往比危机前更具攻击性。"
    url: "https://x.com/adityaag/status/2125112140260638905"
    link_label: "X 原帖"
    time: "11-23 22:19"
---

# AI Builders Digest — 2026-11-24

## X 观点

**Guillermo Rauch（CEO @ Vercel）**：他让 Fable 研究自己全部编程会话，判断 Opus 还是 Gemini Neon 更适合自己，结果选了 Neon。他感慨 Google 强势回归这件事被严重低估了——这也给模型选型提供了一个“个人评测”的新思路：不用看通用榜单，直接拿自己的真实工作来测。[X 原帖](https://x.com/rauchg/status/2124880074168242369)

**Zara Zhang（Follow Builders 作者）**：每天发帖与注重隐私并不矛盾：她几乎每天发帖，但只分享生活与想法的极小一部分（不到 1%）。关键是找到“别人感兴趣”与“自己舒服”的交集，只发那部分——公开分享不等于把整个人生摊开。[X 原帖](https://x.com/zarazhangrui/status/2124905740095885414)

**Garry Tan（CEO @ Y Combinator）**：创业公司可以用一个简单方法自我提醒：循环自问“我们是不是快死了？”主动问这个问题，才能及时发现正在杀死公司的东西并设法规避，而不是等到无可挽回。[X 原帖](https://x.com/garrytan/status/2124905972296560973)

**Thibault Sottiaux（Codex & ChatGPT @ OpenAI）**：在 OpenAI 内部，dots 正在迅速成为完成工作的主要方式，甚至已经出现“用 dots 搭建 dots 系统”的局面。ChatGPT 的新 agent 形态不只是对外功能，内部已把它当作日常生产力工具在用。[X 原帖](https://x.com/thsottiaux/status/2124923055072043052)

**Claude（Claude 官方账号）**：零数据留存（ZDR）结合企业级前沿安全保障（EFS）现已进入公开测试，面向符合条件的企业：它在多请求层面筛查滥用，同时与 ZDR 兼容，已与 100 多家客户共同开发。现已登陆 Claude 平台、AWS、Bedrock 与 Google Cloud，Microsoft Foundry 支持即将到来。[X 原帖](https://x.com/claudeai/status/2124929944530587712)

**Boris Cherny（Claude @ Anthropic）**：一年前 Opus 4.5 成为第一个写出他 100% 代码的模型，但发 PR 的环节没跟上；今天 Claude Ship 进入 beta（Team 与 Enterprise 计划）。Code Review 负责找 bug，PR Steward 处理修复与失败的检查，Claude Approvals 按团队策略自动批准（后两者仍在 beta）。管理员可按 GitHub 仓库开启，建议先从一个仓库、用观察模式的审批跑起，等建立信任再放开。[X 原帖](https://x.com/bcherny/status/2124961485801836573)

**Amjad Masad（CEO @ Replit）**：Replit 发布 agent 群体扩展定律研究：增加 agent 数量能带来显著性能提升，但不像传统扩展定律那样“算力越多越好”，组织方式很关键。固定两小时窗口内，Opus 5.5 在 NumPy 任务上从 1 个 agent 的 3.7 倍加速升至 32 个 agent 的 18.9 倍；GPT-6.2 Astra 单体最强，但超过 8 个 agent 后出现负扩展；去中心化群体比依赖中心协调的扩展更好；问题本身的可并行性是群体表现的强预测因子；个体模型智能反而不能很好预测集体智能。团队同时开源了 Optimization-Bench。[X 原帖](https://x.com/amasad/status/2124969305674748175)

**Claude（Claude 官方账号）**：连接工具、教 Claude 新技能、或两者兼做，现在统一走插件这一种方式。插件体系已上线，收录 1 万多个插件，覆盖 Free、Pro、Max 与 Ultra 计划，Team 与 Enterprise 即将推出——这意味着 Claude 的扩展能力从分散的连接器与技能，收敛成一个统一的插件市场。[X 原帖](https://x.com/claudeai/status/2124970294523945328)

**Thariq（前 Claude Code @ Anthropic）**：X 的创作者分成是个好模式，值得未来软件公司借鉴：保持精简的核心团队，把增长、反馈与销售的收益分给用户。软件公司的规模不一定来自员工数，也可以来自被激励的用户网络。[X 原帖](https://x.com/trq212/status/2124987187406275037)

**Thibault Sottiaux（Codex & ChatGPT @ OpenAI）**：ChatGPT 的回答质量在新一轮改进推送到用户后会有明显提升。配合应用简化、提速，以及聊天与工作的合并，到年底日常体验会有相当大的改善——OpenAI 正在把零散的升级打包成一次集中的体验跃升。[X 原帖](https://x.com/thsottiaux/status/2124998553856844186)

**Amjad Masad（CEO @ Replit）**：他上周五与副总统 Vance 会面，讨论美国 AI 领导力、网络安全与国家软件基础设施现代化。他特别关心美国在开放权重 AI 上的领导力：盟友想要主权 AI，正越来越多地转向中国开源模型；美国本土创业公司也需要有竞争力的模型生态。美国可能赢得前沿 AI 竞赛，却输掉全球 AI 生态。他还提到很高兴看到 Jensen 回到 Nvidia，称其为美国开放权重 AI 最重要的支持者之一。[X 原帖](https://x.com/amasad/status/2125008810041610359)

**Nikunj Kothari（Partner @ FPV Ventures）**：一句关于 2027 年职位名的玩笑：创始人叫 Swarm Overlord、产品经理 Swarm Rider、设计师 Swarm Choreographer、系统工程师 Swarm Architect、一线部署工程师 Swarm Wrangler、市场 Swarm Propagandist、VC Swarm Speculator。玩笑背后是 agent 群体正在成为默认工作方式的预期。[X 原帖](https://x.com/nikunj/status/2125033540287131901)

**Guillermo Rauch（CEO @ Vercel）**：Vercel 宣布在日本加大投入。结合他当天另一条关于模型评测的帖子，Vercel 正在同时推进产品能力与区域扩张。[X 原帖](https://x.com/rauchg/status/2125057274213507253)

**Peter Yang（AI 技能与教程博主）**：他对 ChatGPT Dots 的早期体验很直接：它会在他审核前就发邮件，还会随机停止响应。他很想喜欢这个产品，怀疑是不是自己提示词用得不对。与 OpenAI 内部的乐观形成对照，dots 走到普通用户手里仍有不少坑要填。[X 原帖](https://x.com/petergyang/status/2125060785667969399)

**Aaron Levie（CEO @ Box）**：Agent 正在改写服务业的规模逻辑：服务业历来受限于交付能力，产出只能靠加人头，客户永远想要更快、更便宜、更好；agent 让产出与投入时间脱钩，一个工程师能顶几十个工程师，一个设计师能搭出完整设计系统与品牌。关键仍在前端：需要专家确保 agent 交付出正确的结果。网络安全、广告营销、法律、会计、IT 转型等历来只能靠人的行业都会被重塑，现在正是创业或改造现有公司的好时机。[X 原帖](https://x.com/levie/status/2125089009018040779)

**Aditya Agarwal（GP @ South Park Commons，前 Dropbox CTO）**：有时候需要出国旅行，才能深切体会美国对世界其他地方有多大的感召力：很多国家与个人都渴望拥有美国这样的创业生态与资本市场基础，不想成为中国、英国或丹麦那样的模式——最有抱负的人都在学习美国如何建设。这不代表美国没有改进空间，必须、也一定会做得更好。[X 原帖](https://x.com/adityaag/status/2125096073228439683)

**Madhu Guru（Sr Director, AI @ Meta）**：“数据”这个名字大大低估了它在模型开发中真正的含义。不熟悉模型开发的人把数据看作买来倒进模型的惰性商品，像煤一样；实际上优质数据编码了极高价值的知识、品味与专业能力，很多是以此前不存在的方式表达与结构化的。这使数据成为构建跨领域更强智能最基础的构件之一，未来仍将处于智能产业的中心。[X 原帖](https://x.com/realmadhuguru/status/2125102190196859156)

**Aditya Agarwal（GP @ South Park Commons，前 Dropbox CTO）**：大多数好组织在遭遇没有摧毁它们的生存危机后，会带着复仇心态归来：见过失败的样子，就决心不让它重演；他在 Meta 多次有这种感受。Nvidia 现在不会手软——经历过危机的组织往往比危机前更具攻击性。[X 原帖](https://x.com/adityaag/status/2125112140260638905)

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
