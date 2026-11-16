# Events 数据规范（schema_version 1）

适用对象：每周刷新 mzhao.me/events 的 agent。

## 1. 改了什么

以前每周刷新会整页重写 `events/index.html`，样式、脚本和数据都在同一个文件里。从现在起：

- **只写一个文件：`events/data.json`。** 每次刷新整体覆盖它。
- **不要修改 `events/index.html`**，也不要改 `assets/site.css`、`assets/site.js`。页面模板是固定的，会自己读取 `data.json`。
- 提交前运行 `node _tools/validate_events.mjs`，必须是 `0 error(s)` 才能提交。warning 允许，但要尽量消除。
- 提交信息沿用 `Events: weekly refresh YYYY-MM-DD`，这次提交里只应该有 `events/data.json` 一个文件。

## 2. 文件结构

```json
{
  "schema_version": 1,
  "updated": "2026-11-16",
  "headline": "先逛手作市集，再走进狄更斯的伦敦",
  "days": [ { "date": "2026-11-21", "title": "狄更斯市集开幕，伯克利 Big Game", "picks": ["dickens", "biggame"] } ],
  "events": [ { "…": "见第 4 节" } ],
  "notes": [ { "title": "本期来源配比", "body": "…" } ]
}
```

### 顶层字段

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `schema_version` | 整数 | 是 | 固定为 `1` |
| `updated` | 字符串 | 是 | 本次刷新的日期，`YYYY-MM-DD`，America/Los_Angeles |
| `headline` | 字符串 | 是 | 本期标题，一句话，28 个字以内 |
| `days` | 数组 | 是 | 本期覆盖的每一天，1 到 6 项，见第 3 节 |
| `events` | 数组 | 是 | 全部活动，见第 4 节 |
| `notes` | 数组 | 否 | 来源配比、逐源产出、未收录说明等。页面默认折叠显示 |

`notes` 每一项是 `{ "title": "小标题", "body": "纯文本" }`。`title` 可省略，`body` 必填，不要写 HTML。

## 3. `days`

每一项代表页面上的一个日期标签。

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `date` | 字符串 | 是 | `YYYY-MM-DD`，不能重复 |
| `title` | 字符串 | 否 | 当天的一句话看点，20 个字以内。**不要**写“本周六”“下周日”，页面会自己加“今天 / 明天 / 已结束” |
| `picks` | 字符串数组 | 否 | 当天的编辑首选，最多 3 个活动 `id`。被选中的活动当天必须有场次 |

## 4. `events`

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `id` | 字符串 | 是 | 小写字母、数字、连字符，如 `dickens-fair`。全文件唯一。同一个活动跨周出现时尽量沿用同一个 `id` |
| `title` | 字符串 | 是 | 中文标题，40 个字以内。不要把“（免费）”写进标题，用 `free` 字段 |
| `title_en` | 字符串 | 否 | 英文原名，只用于搜索 |
| `region` | 字符串 | 是 | 只能是 `sf`、`east-bay`、`south-bay`、`peninsula`、`north-bay` 之一 |
| `city` | 字符串 | 是 | 城市英文名，如 `San Francisco` |
| `venue` | 字符串 | 是 | 场馆名称，如 `Fort Mason Center Festival Pavilion`。不要写“见活动页” |
| `address` | 字符串 | 否 | 街道地址，如 `2 Marina Blvd, San Francisco`。有就填，地图按钮会更准 |
| `sessions` | 数组 | 是 | 活动在本期每一天的场次，见第 5 节 |
| `time_note` | 字符串 | 视情况 | 时间的一行补充说明，见第 5 节 |
| `price` | 字符串 | 是 | 票价的一行文字，如 `$26 起`、`免费入场（建议捐赠 $5）`。查不到写 `票价待确认`，不要写“查看活动页” |
| `free` | 布尔 | 是 | 不花钱就能参加为 `true`（需要免费登记也算） |
| `family` | 布尔 | 是 | 见第 6 节的判定标准 |
| `outdoor` | 布尔 | 是 | 主要活动区域在户外为 `true` |
| `tags` | 字符串数组 | 是 | 0 到 4 个短标签。不要放“亲子友好”“免费”“户外”，这三项已有专门字段 |
| `desc` | 字符串 | 是 | 简介，160 个字以内，纯文本 |
| `url` | 字符串 | 是 | `https://` 开头的链接 |
| `link_type` | 字符串 | 是 | `event` 或 `listing`，见第 7 节 |
| `source` | 字符串 | 是 | 来源名称，如 `Eventbrite`、`Filoli 官网`、`DoTheBay 当日列表` |

## 5. 时间：`sessions` 与 `time_note`

`sessions` 里每一项是活动在某一天的一场：

```json
{ "date": "2026-11-21", "start": "19:30", "end": "22:00" }
```

- `date`：`YYYY-MM-DD`，必须是 `days` 里出现过的日期。活动在哪几天举办，就写几项。**同一天只写一项**。
- `start`：24 小时制 `HH:MM`，如 `09:00`、`19:30`。同一天有多场时，填当天最早一场的开始时间。查不到时填 `null`。
- `end`：可选，`HH:MM`。不确定就省略。
- 两天时间不同，就在各自的 session 里写各自的时间，例如周六 `19:30`、周日 `19:00`。

`time_note` 是整个活动共用的一行时间说明，写了以后页面会用它**替代**自动生成的“开始–结束”：

- 多场次、分时入场、开门时间等需要说明的情况才写，例如 `14:00 与 19:00 两场`、`16:30–21:00，分时入场至 18:30`、`14:30 开门，17:30–18:30 放灯`。
- 普通的 `11:00–17:00` 不需要写 `time_note`，填好 `start` 和 `end` 即可。
- 只要有一项 `start` 是 `null`，就**必须**写 `time_note`，例如 `开球时间赛前公布`。
- 页面按 `start` 排序并分组：12:00 前为上午，12:00–16:59 为下午，17:00 起为晚上，`null` 归入“时间待定”。所以 `start` 填错会直接排错位置。

## 6. 判定标准

- `free`：入场不收费。建议捐赠、需免费登记都算 `true`。只是“儿童免费”不算。
- `family`：**明确面向儿童或全家**的活动才为 `true`，例如儿童剧、动物园、亲子手作、灯会。一般的市集、演唱会、体育比赛即使允许带孩子，也填 `false`。上一期 47 条里有 39 条是 `true`，这个筛选等于没用，目标是控制在一半以下。
- `outdoor`：主要活动区域在户外。室内场馆加户外餐车不算。

## 7. 链接：`link_type`

| 值 | 含义 | 页面按钮 |
| --- | --- | --- |
| `event` | 点开就是这个活动自己的页面：主办方活动页、场馆的该场次页、购票详情页 | 活动页 ↗ |
| `listing` | 点开后还要自己找：当日列表、月度专题、类目页、日历页、艺人页 | 在来源页查找 ↗ |

要求：

- 优先找 `event` 链接。只有确实找不到详情页时才用 `listing`。
- 目标：`listing` 不超过全部活动的 25%。上一期是 47 条里 24 条。
- 不要让多个活动共用同一个 `listing` 链接。上一期有 3 场活动都指向 `dothebay.com/events/2026/11/15`。
- 去掉链接里的跟踪参数（`utm_*`、`aff`、`hxref` 等）。

## 8. 文案规则

- **不要使用相对日期。** `title`、`desc`、`time_note`、`price`、`days[].title` 里不能出现：本周、下周、上周、今天、明天、昨天、今晚、明晚、本期、下期、上期。要写就写实际日期，如 `11/21–22`。校验脚本会把这些词判为 error。
- `desc` 先写这个活动是什么，再写一条实用信息（是否需要提前买票、停车、封路等）。
- 信息查不到时明确写“待确认”，不要写“见活动页”“查看活动页”。目标：`start` 为 `null` 的活动不超过 10%。
- 同一个演出在两个周末都有，写成一个活动、多个 `sessions`，不要拆成两条。
- 所有字符串都是纯文本，不要写 HTML 或 Markdown。

## 9. 完整示例

```json
{
  "schema_version": 1,
  "updated": "2026-11-16",
  "headline": "狄更斯的伦敦开门，Big Game 在伯克利打响",
  "days": [
    { "date": "2026-11-21", "title": "狄更斯市集开幕，伯克利 Big Game", "picks": ["dickens-fair", "covenant"] },
    { "date": "2026-11-22", "title": "市集续摊，话剧收官", "picks": ["dickens-fair"] }
  ],
  "events": [
    {
      "id": "dickens-fair",
      "title": "狄更斯圣诞市集开幕周末",
      "title_en": "The Great Dickens Christmas Fair 2026",
      "region": "peninsula",
      "city": "Daly City",
      "venue": "Cow Palace",
      "address": "2600 Geneva Ave, Daly City",
      "sessions": [
        { "date": "2026-11-21", "start": "10:00", "end": "18:00" },
        { "date": "2026-11-22", "start": "10:00", "end": "18:00" }
      ],
      "price": "需提前在线购票，无现场售票",
      "free": false,
      "family": true,
      "outdoor": false,
      "tags": ["圣诞市集", "维多利亚", "沉浸式"],
      "desc": "第 42 届：展厅变身维多利亚时代伦敦的圣诞夜，煤气灯街道、剧场、酒馆与手作店，数百位演员着时代服装穿行其间。门票只能提前在线购买。",
      "url": "https://dickensfair.com/",
      "link_type": "event",
      "source": "主办方官网"
    },
    {
      "id": "covenant",
      "title": "Berkeley Rep 话剧《Covenant》",
      "title_en": "Covenant · Berkeley Repertory Theatre",
      "region": "east-bay",
      "city": "Berkeley",
      "venue": "Peet's Theatre",
      "address": "2025 Addison St, Berkeley",
      "sessions": [
        { "date": "2026-11-21", "start": "19:30" },
        { "date": "2026-11-22", "start": "19:00" }
      ],
      "price": "$25–137",
      "free": false,
      "family": false,
      "outdoor": false,
      "tags": ["话剧"],
      "desc": "南方哥特惊悚剧，演至 12/13：1930 年代乔治亚小镇、十字路口与魔鬼交易的传闻。选座时在官网复核场次时间。",
      "url": "https://www.berkeleyrep.org/shows/covenant-c7h1",
      "link_type": "event",
      "source": "Berkeley Rep 官网"
    }
  ],
  "notes": [
    { "title": "本期来源配比", "body": "场馆与主办方官网 11 条、Eventbrite 5 条、Ticketmaster 5 条。" },
    { "title": "未收录", "body": "11/22 49 人队的指定主场在墨西哥城举行，不在湾区。" }
  ]
}
```

示例中的 `https://dickensfair.com/` 只用来演示格式，实际链接以核对到的为准。

## 10. 提交前自查

1. `node _tools/validate_events.mjs` 输出 `0 error(s)`。
2. `git status` 里只有 `events/data.json` 被修改。
3. `days` 是接下来的两个周末（共 4 天），日期没有写成已经过去的周末。
4. 每个 `picks` 里的 `id` 当天确实有场次。
5. 随机点开 5 个 `link_type` 为 `event` 的链接，确认打开的就是那个活动。
