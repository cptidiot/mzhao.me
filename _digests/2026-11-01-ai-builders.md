---
section: ai-builders
section_name: AI Builders
date: 2026-11-01 09:50:00 -0800
title: "AI Builders Digest — 2026-11-01"
excerpt: "Swyx 谈 effort 档位的品味之争与低 effort + critique loop 的实操路线，Aaron Levie 给出检验 AI 用没用够的试金石；播客里 Arca 详解用 agent 跑长周期金融工作的 harness、记忆与合规设计。"
items:
  - title: "Swyx"
    role: "smol_ai / Cognition / Temporal"
    summary: "Karpathy 在新项目 Hackertube 上用 Opus 5.5 的 medium 档 effort；Swyx 认为对 effort 档位有强烈执念就像当年的 tabs vs spaces 之争，调到顺手就好——当然他的选择肯定比你的好。Effort 档位正在成为 agent 使用中的新品味之争，务实调参胜过教条。"
    url: "https://x.com/swyx/status/2116773135668404286"
    link_label: "X 原帖"
    time: "10-31 23:03"
  - title: "Swyx"
    role: "smol_ai / Cognition / Temporal"
    summary: "旗帜鲜明站“轻量派”：低 effort + critique loop 胜过 superultramaxhighwhatever，对 throughput 受限的场景尤其如此，并指向他的 babysit-runs skill。省 token 又保质量的实操路线——低档跑量、critique 兜底，值得直接抄作业。"
    url: "https://x.com/swyx/status/2116642586387730593"
    link_label: "X 原帖"
    time: "10-31 14:24"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "检验你有没有把 AI 用够的试金石：半年前 AI 只能把你本来就会做的事做快一点；现在 AI 的产出应该在质上超越你原本能做到的——原型功能更完整、架构性能更好、研究穷尽所有事实、流程能从失败中学习。如果你的产出是“没有 AI 也能做出来的东西”，说明你还没 push 够。"
    url: "https://x.com/levie/status/2116652002830963114"
    link_label: "X 原帖"
    time: "10-31 15:02"
  - title: "Using Agents for Long-Horizon Financial Work — Aman Singh, Arca"
    role: "Latent Space"
    summary: "Arca AI 平台负责人 Aman Singh 详解用 agent 跑长周期金融工作：Arca 不是 SaaS，而是 AI 原生的财富管理公司本身，agent 24/7 主动服务，AI 取代的是顾问周围的全部工作而非顾问本人。自研模型无关 harness 按任务复杂度分档选模型，内部基准而非外部榜单决定模型选择；分析全自动，但动钱、清算、直接联系客户必须 human in the loop；安全靠确定性限制、写库校验与边缘 prompt injection 检测，合规靠默认审计日志；员工每次修改附原因并成为 eval，每晚 meta agent 从真实 trace 提改进建议。这是高 stakes、长周期、强监管场景下 agent 落地的完整范本。"
    url: "https://www.youtube.com/@LatentSpacePod"
    link_label: "节目页"
    time: "10-31 09:00"
---

**X 观点**

- [Swyx（smol_ai / Cognition / Temporal）](https://x.com/swyx/status/2116773135668404286)：Karpathy 在新项目 Hackertube 上用 Opus 5.5 的 medium 档 effort；Swyx 认为对 effort 档位有强烈执念就像当年的 tabs vs spaces 之争，调到顺手就好——当然他的选择肯定比你的好。Effort 档位正在成为 agent 使用中的新品味之争，务实调参胜过教条。
- [Swyx（smol_ai / Cognition / Temporal）](https://x.com/swyx/status/2116642586387730593)：旗帜鲜明站“轻量派”：低 effort + critique loop 胜过 superultramaxhighwhatever，对 throughput 受限的场景尤其如此，并指向他的 babysit-runs skill。省 token 又保质量的实操路线——低档跑量、critique 兜底，值得直接抄作业。
- [Aaron Levie（CEO @ Box）](https://x.com/levie/status/2116652002830963114)：检验你有没有把 AI 用够的试金石：半年前 AI 只能把你本来就会做的事做快一点；现在 AI 的产出应该在质上超越你原本能做到的——原型功能更完整、架构性能更好、研究穷尽所有事实、流程能从失败中学习。如果你的产出是“没有 AI 也能做出来的东西”，说明你还没 push 够。

**播客**

- [Using Agents for Long-Horizon Financial Work — Aman Singh, Arca（Latent Space）](https://www.youtube.com/@LatentSpacePod)：Arca AI 平台负责人 Aman Singh 详解用 agent 跑长周期金融工作：Arca 不是 SaaS，而是 AI 原生的财富管理公司本身，agent 24/7 主动服务，AI 取代的是顾问周围的全部工作而非顾问本人。自研模型无关 harness 按任务复杂度分档选模型，内部基准而非外部榜单决定模型选择；分析全自动，但动钱、清算、直接联系客户必须 human in the loop；安全靠确定性限制、写库校验与边缘 prompt injection 检测，合规靠默认审计日志；员工每次修改附原因并成为 eval，每晚 meta agent 从真实 trace 提改进建议。这是高 stakes、长周期、强监管场景下 agent 落地的完整范本。

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
