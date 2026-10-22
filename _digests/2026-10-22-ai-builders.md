---
section: ai-builders
section_name: AI Builders
date: 2026-10-22 09:56:00 -0700
title: "AI Builders Digest — 2026-10-22"
excerpt: "Anthropic 发布主动型 agent Claude Duet、Vercel 与业界联手应对 Node.js RCE 与 php2shell 安全事件、Levie 谈 AI 网络安全新 regime、Every 复盘 frontier team 的组织打法。"
items:
  - title: "Cat Wu"
    role: "Claude Code + Cowork @ Anthropic"
    summary: "Anthropic 回应「希望 Claude 更主动分担」的反馈，推出 Claude Duet：它会注意到需要做的事，并在你开口前先做掉。官方称这是朝主动型 agent 迈出的一大步，现已开放 waitlist。对日常使用者，这意味着 Claude 的形态正从「问答工具」转向「常驻协作者」。"
    url: "https://x.com/_catwu/status/2112988751576330487"
    link_label: "X 原帖"
    time: "10-21 12:25"
  - title: "Claude"
    role: "Anthropic 官方"
    summary: "补充 Duet 的设计：围绕 Claude Opus 5.5 构建，由它判断什么事需要你、什么可以等、什么要先征询你；并继承你 Claude 账户的记忆、skills 与已连接应用，几乎无需重新配置。同线程还说明安全设计——Duet 不直接接触密码、另有分类器防敏感信息外泄，重要决定仍由用户拍板；目前是早期研究预览，美国 Pro 与 Max 用户可经 waitlist 加入，官方也坦承它仍可能误判优先级。"
    url: "https://x.com/claudeai/status/2112984666437546104"
    link_label: "X 原帖"
    time: "10-21 12:09"
  - title: "Dan Shipper"
    role: "CEO @ Every"
    summary: "称 Duet 是 Anthropic 刚发布的 always-on 个人 agent，也是他第一个愿意称为「专业工具」的个人 agent。团队已实测两周，他自己的使用从几乎全用 ChatGPT 变成与 Claude 大约五五开，是近一年来他用 Anthropic 最多的一段时间；Duet 有独立 App（iOS、Android、Web）、按工作与生活领域划分的 channels，以及不会丢失进度的 todo list。"
    url: "https://x.com/danshipper/status/2112997559463506059"
    link_label: "X 原帖"
    time: "10-21 13:00"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "安全快讯：Vercel 已在官方补丁发布前，抢先为当天的 Node.js 远程代码执行（RCE）漏洞推出 Firewall 层缓解措施，所有部署的全部流量自动受保护，团队正持续监控并推送托管 runtime 升级。用 Vercel 部署的项目无需手动操作即已覆盖。"
    url: "https://x.com/rauchg/status/2113050053724221732"
    link_label: "X 原帖"
    time: "10-21 16:29"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "复盘另一场跨公司协作：业界提前数周在幕后联手应对 php2shell 漏洞、保护基础设施，Vercel 已部署的 WAF 缓解措施成功拦截了针对 PHP 源站的尝试。他提醒要假设更多漏洞还在路上，平时就得练好「打补丁→重新部署」这块肌肉。"
    url: "https://x.com/rauchg/status/2112989629536440400"
    link_label: "X 原帖"
    time: "10-21 12:29"
  - title: "Peter Steinberger"
    role: "OpenClaw"
    summary: "一句话点出攻防格局的变化：本周可能引发大麻烦的那个 PHP 漏洞，是用 GPT-5.6 Sol 发现的。AI 找漏洞已从演示变成真实攻防事件，与 Rauch 的 php2shell 复盘正好互相印证。"
    url: "https://x.com/steipete/status/2112913060709228764"
    link_label: "X 原帖"
    time: "10-21 07:25"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "谈 AI 将创造的岗位：想知道答案就看网络安全——它会成为企业未来最大的投入领域之一。即便工作越来越 agentic、自治化，企业仍需要更多人才去指挥 agent 做最关键的工作、审查发现、修补系统、响应事件；保护数据与企业的系统和从业者，眼下机会都很大，而且局势只会更激烈。"
    url: "https://x.com/levie/status/2113137032633757773"
    link_label: "X 原帖"
    time: "10-21 22:15"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "进一步断言网络安全将是 AI 最深远的影响之一：如今有了一支不知疲倦的劳动力，能猎查、发现、修补或攻击任何已建系统与软件。防御方会用 agent 找出存量系统与基础设施里积压已久的风险，攻击方也会用 agent 加速发现环境缺口，双方还将用 agent 抵御攻击、识别异常模式——我们正在进入一个新的网络安全 regime。"
    url: "https://x.com/levie/status/2112964214818283917"
    link_label: "X 原帖"
    time: "10-21 10:48"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "DeepSeek v4.1 Flash（1017）已纳入 Vercel 的 Token Pass：速度快、便宜得惊人，且以零数据保留（ZDR）方式提供。他特别点出用法——很适合跑执行大模型规划的 subagents，便宜到把 TypeScript 移植到 Rust 跑 10 遍也不会用完 credits。"
    url: "https://x.com/rauchg/status/2113010010766913815"
    link_label: "X 原帖"
    time: "10-21 13:50"
  - title: "Dan Shipper"
    role: "CEO @ Every"
    summary: "提出组织命题：跟上 AI 本身就是一份全职工作，所以每家公司都需要一个 frontier team——它的职责是随模型变化持续跟进前沿，其他人则负责用好它学到的东西。Every 已组建这样一支团队，并称这彻底改变了他们的工作方式；本期播客正是这一主题的展开。"
    url: "https://x.com/danshipper/status/2113010761786175970"
    link_label: "X 原帖"
    time: "10-21 13:53"
  - title: "Matt Turck"
    role: "Partner @ FirstMark Capital"
    summary: "在 tokens、APIs 与 agents 的时代，世界正走向持续财务规划（continuous financial planning），而 Pigment 就是为此而建的平台。他恭喜 Pigment 团队完成新一轮融资——同日另一条推文提到 Pigment 宣布 2.5 亿美元 E 轮、Legora 宣布 5.5 亿美元 E 轮，FirstMark 是 Pigment 的种子轮投资方。"
    url: "https://x.com/mattturck/status/2112927524321726921"
    link_label: "X 原帖"
    time: "10-21 08:22"
  - title: "Aditya Agarwal"
    role: "General Partner @ SPC"
    summary: "分享一个观察：用 AI 做东西，可能和「用」AI 一样好玩。他儿子看《星球大战 IV》约 3 小时，却花了约 20 小时围绕剧情做游戏，真正玩的时间反而很少——乐趣在建造本身。他感慨编程的快乐过去只有程序员能体会，如今也许人人都能体验到。"
    url: "https://x.com/adityaag/status/2112923959176106056"
    link_label: "X 原帖"
    time: "10-21 08:08"
  - title: "Zara Zhang"
    role: "Builder"
    summary: "一句话判断：你的个人网站就是新的简历。在 builder 靠作品与分发建立信誉的时代，个人站从「名片」变成了可被直接检验的履历本体。"
    url: "https://x.com/zarazhangrui/status/2113148949842534482"
    link_label: "X 原帖"
    time: "10-21 23:02"
  - title: "How a Frontier Team Can Help Your Company Keep Up With AI"
    role: "AI & I by Every · 播客"
    summary: "Dan Shipper 与负责企业 AI adoption 的 Natalia 复盘 Every 运行数月的 frontier team：每位员工都陷在「干活还是追前沿」的两难里，frontier team 用关注点分离破局——专人疯狂实验，低端产出是内容，高端产出才推入产品，其他人无需追每个新模型。团队构成有诀窍：既要快速试错的「海盗」，也要把混乱实验压缩成可用形态的「架构师」；Head of Evals Mike Taylor 把定性 vibe check 量化为个人 benchmark，还演示 Opus 仅凭 Slack 消息与会议记录剪出讲解视频；另有 Wrangler 角色负责整理实验、盯 token 用量与回报。收尾忠告很实在：frontier team 的成败在整合——别把 100 个实验一股脑倒进频道淹没全公司，要让成果真正被采用。"
    url: "https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL"
    link_label: "节目页"
    time: "10-21 11:31"
---

**X 观点**

- [Cat Wu（Claude Code + Cowork @ Anthropic）](https://x.com/_catwu/status/2112988751576330487)：Anthropic 回应「希望 Claude 更主动分担」的反馈，推出 Claude Duet：它会注意到需要做的事，并在你开口前先做掉。官方称这是朝主动型 agent 迈出的一大步，现已开放 waitlist。对日常使用者，这意味着 Claude 的形态正从「问答工具」转向「常驻协作者」。
- [Claude（Anthropic 官方）](https://x.com/claudeai/status/2112984666437546104)：补充 Duet 的设计：围绕 Claude Opus 5.5 构建，由它判断什么事需要你、什么可以等、什么要先征询你；并继承你 Claude 账户的记忆、skills 与已连接应用，几乎无需重新配置。同线程还说明安全设计——Duet 不直接接触密码、另有分类器防敏感信息外泄，重要决定仍由用户拍板；目前是早期研究预览，美国 Pro 与 Max 用户可经 waitlist 加入，官方也坦承它仍可能误判优先级。
- [Dan Shipper（Every CEO）](https://x.com/danshipper/status/2112997559463506059)：称 Duet 是 Anthropic 刚发布的 always-on 个人 agent，也是他第一个愿意称为「专业工具」的个人 agent。团队已实测两周，他自己的使用从几乎全用 ChatGPT 变成与 Claude 大约五五开，是近一年来他用 Anthropic 最多的一段时间；Duet 有独立 App（iOS、Android、Web）、按工作与生活领域划分的 channels，以及不会丢失进度的 todo list。
- [Guillermo Rauch（Vercel CEO）](https://x.com/rauchg/status/2113050053724221732)：安全快讯：Vercel 已在官方补丁发布前，抢先为当天的 Node.js 远程代码执行（RCE）漏洞推出 Firewall 层缓解措施，所有部署的全部流量自动受保护，团队正持续监控并推送托管 runtime 升级。用 Vercel 部署的项目无需手动操作即已覆盖。
- [Guillermo Rauch（Vercel CEO）](https://x.com/rauchg/status/2112989629536440400)：复盘另一场跨公司协作：业界提前数周在幕后联手应对 php2shell 漏洞、保护基础设施，Vercel 已部署的 WAF 缓解措施成功拦截了针对 PHP 源站的尝试。他提醒要假设更多漏洞还在路上，平时就得练好「打补丁→重新部署」这块肌肉。
- [Peter Steinberger（OpenClaw）](https://x.com/steipete/status/2112913060709228764)：一句话点出攻防格局的变化：本周可能引发大麻烦的那个 PHP 漏洞，是用 GPT-5.6 Sol 发现的。AI 找漏洞已从演示变成真实攻防事件，与 Rauch 的 php2shell 复盘正好互相印证。
- [Aaron Levie（Box CEO）](https://x.com/levie/status/2113137032633757773)：谈 AI 将创造的岗位：想知道答案就看网络安全——它会成为企业未来最大的投入领域之一。即便工作越来越 agentic、自治化，企业仍需要更多人才去指挥 agent 做最关键的工作、审查发现、修补系统、响应事件；保护数据与企业的系统和从业者，眼下机会都很大，而且局势只会更激烈。
- [Aaron Levie（Box CEO）](https://x.com/levie/status/2112964214818283917)：进一步断言网络安全将是 AI 最深远的影响之一：如今有了一支不知疲倦的劳动力，能猎查、发现、修补或攻击任何已建系统与软件。防御方会用 agent 找出存量系统与基础设施里积压已久的风险，攻击方也会用 agent 加速发现环境缺口，双方还将用 agent 抵御攻击、识别异常模式——我们正在进入一个新的网络安全 regime。
- [Guillermo Rauch（Vercel CEO）](https://x.com/rauchg/status/2113010010766913815)：DeepSeek v4.1 Flash（1017）已纳入 Vercel 的 Token Pass：速度快、便宜得惊人，且以零数据保留（ZDR）方式提供。他特别点出用法——很适合跑执行大模型规划的 subagents，便宜到把 TypeScript 移植到 Rust 跑 10 遍也不会用完 credits。
- [Dan Shipper（Every CEO）](https://x.com/danshipper/status/2113010761786175970)：提出组织命题：跟上 AI 本身就是一份全职工作，所以每家公司都需要一个 frontier team——它的职责是随模型变化持续跟进前沿，其他人则负责用好它学到的东西。Every 已组建这样一支团队，并称这彻底改变了他们的工作方式；本期播客正是这一主题的展开。
- [Matt Turck（FirstMark Capital 合伙人）](https://x.com/mattturck/status/2112927524321726921)：在 tokens、APIs 与 agents 的时代，世界正走向持续财务规划（continuous financial planning），而 Pigment 就是为此而建的平台。他恭喜 Pigment 团队完成新一轮融资——同日另一条推文提到 Pigment 宣布 2.5 亿美元 E 轮、Legora 宣布 5.5 亿美元 E 轮，FirstMark 是 Pigment 的种子轮投资方。
- [Aditya Agarwal（SPC 合伙人、前 Dropbox CTO）](https://x.com/adityaag/status/2112923959176106056)：分享一个观察：用 AI 做东西，可能和「用」AI 一样好玩。他儿子看《星球大战 IV》约 3 小时，却花了约 20 小时围绕剧情做游戏，真正玩的时间反而很少——乐趣在建造本身。他感慨编程的快乐过去只有程序员能体会，如今也许人人都能体验到。
- [Zara Zhang（Builder）](https://x.com/zarazhangrui/status/2113148949842534482)：一句话判断：你的个人网站就是新的简历。在 builder 靠作品与分发建立信誉的时代，个人站从「名片」变成了可被直接检验的履历本体。

**播客**

- [AI & I by Every：How a Frontier Team Can Help Your Company Keep Up With AI](https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL)：Dan Shipper 与负责企业 AI adoption 的 Natalia 复盘 Every 运行数月的 frontier team：每位员工都陷在「干活还是追前沿」的两难里，frontier team 用关注点分离破局——专人疯狂实验，低端产出是内容，高端产出才推入产品，其他人无需追每个新模型。团队构成有诀窍：既要快速试错的「海盗」，也要把混乱实验压缩成可用形态的「架构师」；Head of Evals Mike Taylor 把定性 vibe check 量化为个人 benchmark，还演示 Opus 仅凭 Slack 消息与会议记录剪出讲解视频；另有 Wrangler 角色负责整理实验、盯 token 用量与回报。收尾忠告很实在：frontier team 的成败在整合——别把 100 个实验一股脑倒进频道淹没全公司，要让成果真正被采用。

---
内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
