---
section: ai-builders
section_name: AI Builders
date: 2026-11-14 09:55:00 -0800
title: "AI Builders Digest — 2026-11-14"
excerpt: "Vercel 发布 Workflow SDK 5，Garry Tan 实测 Opus 5.5 性价比胜过 Fable 5.2，Replit 与 Visa 推进 agent 商务；另有 Training Data 对话 Trajectory 谈持续学习。"
items:
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "Vercel 发布 Workflow SDK 5 与 Vercel Workflows，Rauch 称之为 agent 的“巨大进步”：首步耗时与步骤间隔大幅缩短，加密与安全性加强，可靠性已在超大规模场景验证并演练了灾难恢复；底层持久化日志被抽成可复用的 durable-harness，供任何 agent 框架使用。对 builders 来说，工作流编排正在从“能跑”走向“生产级可靠”，而把耐久日志做成通用层，意味着自研 agent 框架也能直接复用这套基础设施。"
    url: "https://x.com/rauchg/status/2121277727940776114"
    link_label: "X 原帖"
    time: "11-13 08:23"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "Llama 4 之后本以为大家不再拿刷榜当卖点，但“榜单 cartel”又回来了。Kothari 的判断：真正了解模型适不适合自己的工作流，唯一办法是亲自上手用；真正有意义的基准其实很少，内行都清楚；其余大多是营销造势、靠刷某一项榜单撑门面，短期对少数公司有效、长期站不住。对正在选模型的 builders，这是个提醒：榜单分数不等于工作流里的实际表现。"
    url: "https://x.com/nikunj/status/2121320899161010360"
    link_label: "X 原帖"
    time: "11-13 11:14"
  - title: "Nikunj Kothari"
    role: "Partner @ FPV Ventures"
    summary: "FAA 全国机场地面停摆是现代史上第三次：第一次是 9/11，第二次是 2023 年 NOTAM 系统故障，这次是第三次、原因尚不明确。Kothari 拿这条时间线点出事态的罕见程度——不是寻常延误，而是几十年一遇的级别。虽不是 AI 话题，但同一批 builder 都在天上飞、都在关注，对行程与供应链的连锁影响值得留意。"
    url: "https://x.com/nikunj/status/2121366466905981435"
    link_label: "X 原帖"
    time: "11-13 14:15"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "Masad 呼吁大家读《Stand with Jensen》公开信并考虑联署。黄仁勋风波进入公开声援阶段，Replit CEO 公开站队“程序正义”一侧。结合前几天 Turck 对 NVIDIA 生态支点作用的盘点，这封联署信的走向值得 builders 跟进——它不只关乎一个人，也关乎生态里最活跃的投资方与买家能否继续正常运转。"
    url: "https://x.com/amasad/status/2121377395244749097"
    link_label: "X 原帖"
    time: "11-13 14:59"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "Replit 与 Visa 在 agent 商务上的合作进展顺利，更多功能与用例在路上。Agent 正在从“写代码、搭应用”伸向“替用户完成真实购买”，支付网络随之成为 agent 经济的基础设施。Replit 上周刚让 Agent 能替企业买东西，这次是把支付环节与 Visa 一起做深——agent 花钱这件事，正在从演示变成产品。"
    url: "https://x.com/amasad/status/2121428406764204199"
    link_label: "X 原帖"
    time: "11-13 18:22"
  - title: "Peter Yang"
    role: "AI 技能与教程博主"
    summary: "Yang 发布免费的 /fuck-cancer skill：如果身边有人患癌症或其他长期疾病，把患者全部病历上传到云盘文件夹，让 ChatGPT 或 Claude 安装这个 skill，就能生成一页病情简报、检索临床试验等；也可以 fork 改造成其他长期疾病版本。把 AI 能力直接用在重病家庭的实际决策支持上，是个很有温度的实用案例，也展示了 skill 这种形态能承载的真实价值。"
    url: "https://x.com/petergyang/status/2121430386685395022"
    link_label: "X 原帖"
    time: "11-13 18:29"
  - title: "Peter Yang"
    role: "AI 技能与教程博主"
    summary: "WSJ 关于 NVIDIA 员工 Alice Huang 的报道存疑——Yang 援引新加坡政府的材料指出，目前仍不清楚她就是间谍，WSJ 下结论过早，并提醒读者自行研究。黄仁勋风波的余波仍在发酵，相关报道的真实性本身成了 builders 需要留意的功课：先核对信源，再下判断。"
    url: "https://x.com/petergyang/status/2121430819667579031"
    link_label: "X 原帖"
    time: "11-13 18:31"
  - title: "Garry Tan"
    role: "President & CEO @ Y Combinator"
    summary: "Tan 建议把 Opus 5.5 留作 Claude Code 的默认编码模型：他在 52 个编码任务上用开源评测框架实测，Fable 5.2 解决率 82.7%、Opus 5.5 为 84.6%，基本打平，但 Fable 每解决一个任务的成本是 Opus 的 2.80 倍。结论是 Opus 已能解决大多数任务，要分出高下需要更难的任务。对 builders 来说，选模型时性价比比榜单名次更实在，这份实测数据可以直接参考。"
    url: "https://x.com/garrytan/status/2121464508225053153"
    link_label: "X 原帖"
    time: "11-13 20:45"
  - title: "Training Data × Ronak"
    summary: "Training Data 对话 Trajectory 的 Ronak，主题是持续学习（continual learning）。核心论点：今天的 AI 仍是“伪持续学习”——模型像纸质地图时代，改路线要整批重训；真正的持续学习应像 Google Maps，每次行驶都在更新。Trajectory 的产品是“一键训练”界面：拿生产中的 agent 轨迹、定义好“什么是好结果”，训练、评估、部署放在一处，像当年 iPhone 把上网与打电话合进一部手机。团队来自 Windsurf（从生产编辑与重试中学习）、Gemini Robotics（机器人每日更新）与 Vision Pro。基础设施三件套是：记录轨迹、让轨迹可回放、把奖励信号传回去；他还谈到“好奇心”——LLM 擅长从一个状态跳到下一个状态，却不懂状态之间的转移函数，agent 需要主动探索来建立世界模型。终局愿景是：今天只有约 1% 的企业真正用上了 AI，持续学习要把这个数字推向 99%。"
    url: "https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8"
    link_label: "节目页"
    time: "11-05 02:00"
---

## X 观点

**Guillermo Rauch（CEO @ Vercel）**：Vercel 发布 Workflow SDK 5 与 Vercel Workflows，Rauch 称之为 agent 的“巨大进步”：首步耗时与步骤间隔大幅缩短，加密与安全性加强，可靠性已在超大规模场景验证并演练了灾难恢复；底层持久化日志被抽成可复用的 durable-harness，供任何 agent 框架使用。对 builders 来说，工作流编排正在从“能跑”走向“生产级可靠”，而把耐久日志做成通用层，意味着自研 agent 框架也能直接复用这套基础设施。[X 原帖](https://x.com/rauchg/status/2121277727940776114)

**Nikunj Kothari（Partner @ FPV Ventures）**：Llama 4 之后本以为大家不再拿刷榜当卖点，但“榜单 cartel”又回来了。Kothari 的判断：真正了解模型适不适合自己的工作流，唯一办法是亲自上手用；真正有意义的基准其实很少，内行都清楚；其余大多是营销造势、靠刷某一项榜单撑门面，短期对少数公司有效、长期站不住。对正在选模型的 builders，这是个提醒：榜单分数不等于工作流里的实际表现。[X 原帖](https://x.com/nikunj/status/2121320899161010360)

**Nikunj Kothari（Partner @ FPV Ventures）**：FAA 全国机场地面停摆是现代史上第三次：第一次是 9/11，第二次是 2023 年 NOTAM 系统故障，这次是第三次、原因尚不明确。Kothari 拿这条时间线点出事态的罕见程度——不是寻常延误，而是几十年一遇的级别。虽不是 AI 话题，但同一批 builder 都在天上飞、都在关注，对行程与供应链的连锁影响值得留意。[X 原帖](https://x.com/nikunj/status/2121366466905981435)

**Amjad Masad（CEO @ Replit）**：Masad 呼吁大家读《Stand with Jensen》公开信并考虑联署。黄仁勋风波进入公开声援阶段，Replit CEO 公开站队“程序正义”一侧。结合前几天 Turck 对 NVIDIA 生态支点作用的盘点，这封联署信的走向值得 builders 跟进——它不只关乎一个人，也关乎生态里最活跃的投资方与买家能否继续正常运转。[X 原帖](https://x.com/amasad/status/2121377395244749097)

**Amjad Masad（CEO @ Replit）**：Replit 与 Visa 在 agent 商务上的合作进展顺利，更多功能与用例在路上。Agent 正在从“写代码、搭应用”伸向“替用户完成真实购买”，支付网络随之成为 agent 经济的基础设施。Replit 上周刚让 Agent 能替企业买东西，这次是把支付环节与 Visa 一起做深——agent 花钱这件事，正在从演示变成产品。[X 原帖](https://x.com/amasad/status/2121428406764204199)

**Peter Yang（AI 技能与教程博主）**：Yang 发布免费的 /fuck-cancer skill：如果身边有人患癌症或其他长期疾病，把患者全部病历上传到云盘文件夹，让 ChatGPT 或 Claude 安装这个 skill，就能生成一页病情简报、检索临床试验等；也可以 fork 改造成其他长期疾病版本。把 AI 能力直接用在重病家庭的实际决策支持上，是个很有温度的实用案例，也展示了 skill 这种形态能承载的真实价值。[X 原帖](https://x.com/petergyang/status/2121430386685395022)

**Peter Yang（AI 技能与教程博主）**：WSJ 关于 NVIDIA 员工 Alice Huang 的报道存疑——Yang 援引新加坡政府的材料指出，目前仍不清楚她就是间谍，WSJ 下结论过早，并提醒读者自行研究。黄仁勋风波的余波仍在发酵，相关报道的真实性本身成了 builders 需要留意的功课：先核对信源，再下判断。[X 原帖](https://x.com/petergyang/status/2121430819667579031)

**Garry Tan（President & CEO @ Y Combinator）**：Tan 建议把 Opus 5.5 留作 Claude Code 的默认编码模型：他在 52 个编码任务上用开源评测框架实测，Fable 5.2 解决率 82.7%、Opus 5.5 为 84.6%，基本打平，但 Fable 每解决一个任务的成本是 Opus 的 2.80 倍。结论是 Opus 已能解决大多数任务，要分出高下需要更难的任务。对 builders 来说，选模型时性价比比榜单名次更实在，这份实测数据可以直接参考。[X 原帖](https://x.com/garrytan/status/2121464508225053153)

## 播客

**Training Data × Ronak**：Training Data 对话 Trajectory 的 Ronak，主题是持续学习（continual learning）。核心论点：今天的 AI 仍是“伪持续学习”——模型像纸质地图时代，改路线要整批重训；真正的持续学习应像 Google Maps，每次行驶都在更新。Trajectory 的产品是“一键训练”界面：拿生产中的 agent 轨迹、定义好“什么是好结果”，训练、评估、部署放在一处，像当年 iPhone 把上网与打电话合进一部手机。团队来自 Windsurf（从生产编辑与重试中学习）、Gemini Robotics（机器人每日更新）与 Vision Pro。基础设施三件套是：记录轨迹、让轨迹可回放、把奖励信号传回去；他还谈到“好奇心”——LLM 擅长从一个状态跳到下一个状态，却不懂状态之间的转移函数，agent 需要主动探索来建立世界模型。终局愿景是：今天只有约 1% 的企业真正用上了 AI，持续学习要把这个数字推向 99%。[节目页](https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8)

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
