---
section: ai-builders
section_name: AI Builders
date: 2026-11-13 09:55:00 -0800
title: "AI Builders Digest — 2026-11-13"
excerpt: "Gemini 4 Hydrogen 发布、Box 实测数据亮眼，Claude Meetings 上线 Google Meet，Vercel 推出 agent 时代的 UI SDK；另有 No Priors 对话 Isomorphic Labs 总裁谈 AI 新药研发。"
items:
  - title: "Josh Woodward"
    role: "Google VP，Google Labs / Gemini"
    summary: "Google 推出 Gemini 4 Hydrogen，现已上线 Gemini App。Woodward 称它“快、聪明、是一次大跨步”。这是 Gemini 面向所有人的新旗舰级模型。发布本身信息不多，但同日 Box 的实测（见下条）给了具体数字——准确率与速度双双大幅提升，意味着 Google 在“快模型”这条线上直接对标竞品，值得关注它在 Gemini App 里的实际表现。"
    url: "https://x.com/joshwoodward/status/2120942262054232392"
    link_label: "X 原帖"
    time: "11-12 10:10"
  - title: "Aaron Levie"
    role: "CEO @ Box"
    summary: "Box 用自家的 Box AI Complex Work Eval 对 Gemini 4 Hydrogen 做了早期测试：与 Gemini 3.8 Flash 相比，复杂企业文档任务的准确率高 5 个百分点，同时用时不到一半、token 消耗少约 12%。评测任务覆盖金融、咨询、生命科学等真实企业文档场景。Levie 认为它会成为很多“高效但复杂”任务的好选择，Box 将很快在 Box AI Studio 上线该模型供客户搭建自定义 agent。这是 Hydrogen 发布后第一份来自企业的独立实测数据。"
    url: "https://x.com/levie/status/2120947988143198302"
    link_label: "X 原帖"
    time: "11-12 10:33"
  - title: "Matt Turck"
    role: "VC @ FirstMark Capital"
    summary: "黄仁勋风波之下，Turck 盘点 AI 生态将失去什么：NVIDIA 是生态的“中央银行”（出手托底）、最活跃的投资方，以及一位敢于大胆收购的买家——他还特意提到 Hugging Face 的收购时机可能是大型并购史上最佳。这些激进动作只有创始人才能做。他的意思是，无论传闻结局如何，风波本身已动摇生态中一个结构性支点，值得 builders 关注后续连锁反应。"
    url: "https://x.com/mattturck/status/2120951444526264388"
    link_label: "X 原帖"
    time: "11-12 10:46"
  - title: "Guillermo Rauch"
    role: "CEO @ Vercel"
    summary: "Rauch 抛出 agent 时代的问题：框架、组件库会怎样？他的答案是 Vercel 的 UI SDK——把 UI 行为打包成可复用的“包”，像 agent 用来即兴搭建新 UI 组件的“x86 指令集”。Agent 是新的设计工程师，能按需求无限生成 UI；高层级、僵化的单框架抽象反而是瓶颈。UI SDK 想两全其美：保留无障碍、性能与一致性，同时省 token、少出错，且对能生成的 UI 毫无限制。这是 Vercel 对 agent 生成式 UI 的正式下注。"
    url: "https://x.com/rauchg/status/2120966768483262648"
    link_label: "X 原帖"
    time: "11-12 11:47"
  - title: "Claude"
    role: "Anthropic 官方账号"
    summary: "Claude 正式推出 Claude Meetings：先上 Google Meet，其他视频会议平台随后跟进。Claude 以可见参与者身份加入会议，可被口头或文字提问、现场起草文档；会后笔记、待办事项、逐字稿和会上构建的内容都汇总在会议页面。Anthropic 研究员 Alex Albert 补充了背后的逻辑：用好 Claude 的关键是找到它缺失的上下文并补上，Meetings 正是补齐“会议里那部分上下文”的办法，内部已证明很有用。这是 Claude 从聊天助手向会议工作流延伸的重要一步。"
    url: "https://x.com/claudeai/status/2120974000746582357"
    link_label: "X 原帖"
    time: "11-12 12:16"
  - title: "Josh Woodward"
    role: "Google VP，Google Labs / Gemini"
    summary: "“Gemini，现在从你的视角出发。”Google 的 Gemini 眼镜开启预订，可在 Warby Parker、Gentle Monster 和 Google 部分门店试戴，12 月 10 日发货。这是 Google 把 Gemini 装进可穿戴设备的落地一步：眼镜形态的 AI 助手从演示走向市售，渠道上直接借了两家眼镜品牌。预订已开，值得关注首批佩戴场景的实际反馈。"
    url: "https://x.com/joshwoodward/status/2120990821902397885"
    link_label: "X 原帖"
    time: "11-12 13:23"
  - title: "Peter Steinberger"
    role: "OpenClaw / OpenAI"
    summary: "Steinberger 提醒：本周晚些时候会有一个新 agent 发布，而营销方正出高价请人在 X 上说好话。“留意真实测评。”在 agent 产品扎堆发布的当下，这是一条针对“付费好评”的预警——读到本周新 agent 的夸赞时，先看是不是收了钱的软文。对 builders 来说，判断新工具是否值得试，独立实测比时间线上的赞美更可信。"
    url: "https://x.com/steipete/status/2121009372470067544"
    link_label: "X 原帖"
    time: "11-12 14:36"
  - title: "Amjad Masad"
    role: "CEO @ Replit"
    summary: "Replit Agent 现在能替企业买东西了，包括购买广告来获取新客户。Agent 从“写代码、搭应用”向“替业务花钱办事”延伸了一步：采购与获客这类有真实资金流动的操作，开始交给 agent 执行。对 Replit 来说，这是 Agent 从开发工具变成业务执行层的关键扩展；对用户来说，要留意权限与预算控制怎么做。"
    url: "https://x.com/amasad/status/2121018020520931712"
    link_label: "X 原帖"
    time: "11-12 15:11"
  - title: "Thibault Sottiaux"
    role: "Codex & ChatGPT @ OpenAI"
    summary: "OpenAI 宣布正在开发新的网络安全工具，覆盖自动打补丁和自动红队测试两端。Thibault 附上了发布录像。这是 OpenAI 把 agent 能力伸向安全运维的信号：补丁与红队都是人力密集、重复度高的工作，若自动化可靠，会直接改变安全团队的工作方式。具体发布时间与细节尚未公布，可看录像了解全貌。"
    url: "https://x.com/thsottiaux/status/2121036562058400200"
    link_label: "X 原帖"
    time: "11-12 16:24"
  - title: "Peter Steinberger"
    role: "OpenClaw / OpenAI"
    summary: "Steinberger 转发了团队的文章，讲 OpenAI 内部如何运行持久化 agent。持久化 agent 是 agent 从“一次对话”走向“长期在岗”的关键形态：它要持续保有状态、记忆与目标，并在后台推进工作。这篇文章来自一线实践，对正在搭建长期运行 agent 的 builders 有直接参考价值。"
    url: "https://x.com/steipete/status/2121058770767982997"
    link_label: "X 原帖"
    time: "11-12 17:53"
  - title: "No Priors × Max Jaderberg"
    summary: "No Priors 对话 Isomorphic Labs 总裁 Max Jaderberg，主题是 AI 如何重做新药研发。核心论点：制药至今仍是高度经验主义的试错——新药获批数多年持平，单药成本却从几亿美元涨到约 15 亿美元、周期从 8–9 年拉到约 15 年；失败大多发生在临床阶段，毒性与脱靶效应直到进人体才暴露。Isomorphic 的路线是把药物设计整个搬上计算机：以 AlphaFold 为范例，用达到实验精度的预测模型替代真实实验，让现实世界只做验证、不做迭代。现有药企数据库是多年被动收集的副产品、偏差大，他们选择自己生成数据，并观察到明显的数据规模效应；大鼠毒性模型对人类临床毒性的预测力只有约 30%，他们想用体外指标加 AI、类器官与器官芯片直接建模人类毒性。商业模式上不卖模型，只内部用药：自有管线聚焦肿瘤与免疫炎症等根节点问题，同时与药企合作攻克多年未解的难题。首个临床试验没有具体日期，Jaderberg 预期五年内对疾病生物学的预测理解会大幅跃升。"
    url: "https://www.youtube.com/@NoPriorsPodcast"
    link_label: "节目页"
    time: "11-12 03:00"
---

## X 观点

**Josh Woodward（Google VP，Google Labs / Gemini）**：Google 推出 Gemini 4 Hydrogen，现已上线 Gemini App。Woodward 称它“快、聪明、是一次大跨步”。这是 Gemini 面向所有人的新旗舰级模型。发布本身信息不多，但同日 Box 的实测（见下条）给了具体数字——准确率与速度双双大幅提升，意味着 Google 在“快模型”这条线上直接对标竞品，值得关注它在 Gemini App 里的实际表现。[X 原帖](https://x.com/joshwoodward/status/2120942262054232392)

**Aaron Levie（CEO @ Box）**：Box 用自家的 Box AI Complex Work Eval 对 Gemini 4 Hydrogen 做了早期测试：与 Gemini 3.8 Flash 相比，复杂企业文档任务的准确率高 5 个百分点，同时用时不到一半、token 消耗少约 12%。评测任务覆盖金融、咨询、生命科学等真实企业文档场景。Levie 认为它会成为很多“高效但复杂”任务的好选择，Box 将很快在 Box AI Studio 上线该模型供客户搭建自定义 agent。这是 Hydrogen 发布后第一份来自企业的独立实测数据。[X 原帖](https://x.com/levie/status/2120947988143198302)

**Matt Turck（VC @ FirstMark Capital）**：黄仁勋风波之下，Turck 盘点 AI 生态将失去什么：NVIDIA 是生态的“中央银行”（出手托底）、最活跃的投资方，以及一位敢于大胆收购的买家——他还特意提到 Hugging Face 的收购时机可能是大型并购史上最佳。这些激进动作只有创始人才能做。他的意思是，无论传闻结局如何，风波本身已动摇生态中一个结构性支点，值得 builders 关注后续连锁反应。[X 原帖](https://x.com/mattturck/status/2120951444526264388)

**Guillermo Rauch（CEO @ Vercel）**：Rauch 抛出 agent 时代的问题：框架、组件库会怎样？他的答案是 Vercel 的 UI SDK——把 UI 行为打包成可复用的“包”，像 agent 用来即兴搭建新 UI 组件的“x86 指令集”。Agent 是新的设计工程师，能按需求无限生成 UI；高层级、僵化的单框架抽象反而是瓶颈。UI SDK 想两全其美：保留无障碍、性能与一致性，同时省 token、少出错，且对能生成的 UI 毫无限制。这是 Vercel 对 agent 生成式 UI 的正式下注。[X 原帖](https://x.com/rauchg/status/2120966768483262648)

**Claude（Anthropic 官方账号）**：Claude 正式推出 Claude Meetings：先上 Google Meet，其他视频会议平台随后跟进。Claude 以可见参与者身份加入会议，可被口头或文字提问、现场起草文档；会后笔记、待办事项、逐字稿和会上构建的内容都汇总在会议页面。Anthropic 研究员 Alex Albert 补充了背后的逻辑：用好 Claude 的关键是找到它缺失的上下文并补上，Meetings 正是补齐“会议里那部分上下文”的办法，内部已证明很有用。这是 Claude 从聊天助手向会议工作流延伸的重要一步。[X 原帖](https://x.com/claudeai/status/2120974000746582357)

**Josh Woodward（Google VP，Google Labs / Gemini）**：“Gemini，现在从你的视角出发。”Google 的 Gemini 眼镜开启预订，可在 Warby Parker、Gentle Monster 和 Google 部分门店试戴，12 月 10 日发货。这是 Google 把 Gemini 装进可穿戴设备的落地一步：眼镜形态的 AI 助手从演示走向市售，渠道上直接借了两家眼镜品牌。预订已开，值得关注首批佩戴场景的实际反馈。[X 原帖](https://x.com/joshwoodward/status/2120990821902397885)

**Peter Steinberger（OpenClaw / OpenAI）**：Steinberger 提醒：本周晚些时候会有一个新 agent 发布，而营销方正出高价请人在 X 上说好话。“留意真实测评。”在 agent 产品扎堆发布的当下，这是一条针对“付费好评”的预警——读到本周新 agent 的夸赞时，先看是不是收了钱的软文。对 builders 来说，判断新工具是否值得试，独立实测比时间线上的赞美更可信。[X 原帖](https://x.com/steipete/status/2121009372470067544)

**Amjad Masad（CEO @ Replit）**：Replit Agent 现在能替企业买东西了，包括购买广告来获取新客户。Agent 从“写代码、搭应用”向“替业务花钱办事”延伸了一步：采购与获客这类有真实资金流动的操作，开始交给 agent 执行。对 Replit 来说，这是 Agent 从开发工具变成业务执行层的关键扩展；对用户来说，要留意权限与预算控制怎么做。[X 原帖](https://x.com/amasad/status/2121018020520931712)

**Thibault Sottiaux（Codex & ChatGPT @ OpenAI）**：OpenAI 宣布正在开发新的网络安全工具，覆盖自动打补丁和自动红队测试两端。Thibault 附上了发布录像。这是 OpenAI 把 agent 能力伸向安全运维的信号：补丁与红队都是人力密集、重复度高的工作，若自动化可靠，会直接改变安全团队的工作方式。具体发布时间与细节尚未公布，可看录像了解全貌。[X 原帖](https://x.com/thsottiaux/status/2121036562058400200)

**Peter Steinberger（OpenClaw / OpenAI）**：Steinberger 转发了团队的文章，讲 OpenAI 内部如何运行持久化 agent。持久化 agent 是 agent 从“一次对话”走向“长期在岗”的关键形态：它要持续保有状态、记忆与目标，并在后台推进工作。这篇文章来自一线实践，对正在搭建长期运行 agent 的 builders 有直接参考价值。[X 原帖](https://x.com/steipete/status/2121058770767982997)

## 播客

**No Priors × Max Jaderberg**：No Priors 对话 Isomorphic Labs 总裁 Max Jaderberg，主题是 AI 如何重做新药研发。核心论点：制药至今仍是高度经验主义的试错——新药获批数多年持平，单药成本却从几亿美元涨到约 15 亿美元、周期从 8–9 年拉到约 15 年；失败大多发生在临床阶段，毒性与脱靶效应直到进人体才暴露。Isomorphic 的路线是把药物设计整个搬上计算机：以 AlphaFold 为范例，用达到实验精度的预测模型替代真实实验，让现实世界只做验证、不做迭代。现有药企数据库是多年被动收集的副产品、偏差大，他们选择自己生成数据，并观察到明显的数据规模效应；大鼠毒性模型对人类临床毒性的预测力只有约 30%，他们想用体外指标加 AI、类器官与器官芯片直接建模人类毒性。商业模式上不卖模型，只内部用药：自有管线聚焦肿瘤与免疫炎症等根节点问题，同时与药企合作攻克多年未解的难题。首个临床试验没有具体日期，Jaderberg 预期五年内对疾病生物学的预测理解会大幅跃升。[节目页](https://www.youtube.com/@NoPriorsPodcast)

内容来源：Follow Builders — [Follow Builders](https://github.com/zarazhangrui/follow-builders)
