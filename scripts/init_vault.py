#!/usr/bin/env python3
"""init_vault.py — 初始化 Obsidian 第二大脑知识库骨架（v0.3）。

用法:
  python3 init_vault.py --vault /路径/到/Obsidian库      # 生成知识库骨架
  python3 init_vault.py --vault /路径/到/库 --demo        # 带示例内容的演示库

生成结构（三支柱 + 实体层 + 问答沉淀 + 归档区）:
  Raw Sources/           # 原始摄入收件箱（逐字稿/文章存档）
  Raw Sources/processed/ # 已处理归档区（处理完的文件移入，收件箱保持干净）
  Wiki/                  # AI 维护的总结/概念页
  Wiki/Entities/         # 实体页（人物/公司/工具/想法/主题，自动提取累积）
  Wiki/Queries/          # 问答沉淀页（提问答案写回，复利）
  Journal/               # 每日复盘日记（含模式识别）
  CRM/                   # 人脉笔记（关联 Wiki/实体/事件）
  AGENTS.md              # 规则层（告诉豆包工作如何维护本库）
  SCHEMA.md              # 页面结构 Schema
  index.md               # 全库目录
  log.md                 # 操作日志
  欢迎.md                 # 入库起点

特性: 幂等——已存在的文件不会被覆盖；目录缺失自动创建。
纯 Python 标准库，无第三方依赖。
"""

import argparse
import datetime
import pathlib
import sys

FILES: dict[str, str] = {}

FILES["AGENTS.md"] = """# 知识库规则（AGENTS.md）

> 豆包工作维护本库时必须遵守的规则。**一份规则文件同时驱动全部能力：Wiki / Journal / CRM / 实体层 / 问答沉淀 / 归档 / 备份。**

## 目录结构
- `Raw Sources/`：原始摄入收件箱（逐字稿/提取内容），文件命名 `<日期>-<主题>.md`
- `Raw Sources/processed/`：**已处理归档区**——完成 Wiki/实体页生成后，原始文件移入此处，收件箱保持干净
- `Wiki/`：AI 维护的总结/概念页，用双括号 `[[链接]]` 互连
- `Wiki/Entities/`：**实体页**（人物/公司/工具/想法/主题），摄入时自动提取并累积「提及记录」
- `Wiki/Queries/`：**问答沉淀页**——向库提问的答案写回此处，成为可复用知识
- `Journal/`：每日复盘日记，AI 自动从 Wiki 取知识做复盘，并扫描历史复盘识别模式
- `CRM/`：人脉笔记（联系人背景/互动记录/下次跟进 + 关联实体/想法/事件）
- `index.md`：全库目录（AI 提问前先读这里）
- `log.md`：操作日志（追加式，最新在上）

## 核心规则
- 先结果后依据；数字/统计须可验证
- 不编造内容；截断/受限时标「待补充」；Journal/CRM 缺省字段不虚构
- 保留用户已有改动，不覆盖无关工作
- 敏感信息（证照/密码/家庭住址/资产）拒绝入库
- 每次摄入/更新写 `log.md`，页面增减同步 `index.md`

## 摄入规则（每次处理原始内容必做）
1. **总结**：生成 Wiki/<主题>.md 总结页
2. **提取实体**：扫描内容中的人物/公司/工具/想法/主题，为每个实体创建或更新 `Wiki/Entities/` 实体页，追加「提及记录」（日期+来源+观点）
3. **自动互链**：查 index 与现有 Wiki 页，找出相关页（同实体/同主题），互相补双括号链接；Wiki 页反向引用其来源笔记
4. **归档**：完成上述步骤后，将原始文件移入 `Raw Sources/processed/`

## 复盘规则（Journal）
- 从 Wiki 中挑选与当日工作最相关的 1-3 页引用，形成「今日新知」
- **模式识别**：扫描近 30 天历史复盘，识别反复出现的主题/挣扎（≥3 次），在当日复盘标注「📈 模式识别」

## 问答沉淀（Queries）
- 用户向知识库提问且答案基于库内内容时，答案写回 `Wiki/Queries/<日期>-<问题>.md`（问题/答案/引用来源），复利积累

## CRM 规则
- 记录背景、最近互动、关注点、下次跟进四项，缺省标「待补充」
- **连接万物**：录入/更新时自动检索库中相关实体页（所在公司/提到的工具/聊过的主题），写入 `linked_entities` 并互链

## 备份规则
- 每日巡检后执行 git add -A + commit（本机可用时）；配置私有 GitHub remote 后自动 push
"""

FILES["SCHEMA.md"] = """# 页面结构 Schema（SCHEMA.md）

## Raw Sources 页面
- frontmatter: `source_url`（来源链接）/ `ingested`（日期）/ `content_type`（video/article/image）/ `lang`（zh-en 等）
- 正文：原始内容/双语逐字稿/提取结果，保留来源信息
- 处理完成后文件移入 `Raw Sources/processed/`

## Wiki 页面（summary/concept）
- frontmatter: `title` / `created` / `updated` / `type`（summary|concept）/ `tags` / `sources`（指向 Raw Sources）/ `entities`（相关实体页）
- 正文：摘要 → 关键要点 → 相关实体（自动提取）→ 与本库的关系（自动互链）→ 与其他知识的关联 → 待解答的问题 → 来源

## Entity 页面（Wiki/Entities/，type: entity）
- frontmatter: `title`（实体名）/ `entity_type`（people|company|tool|idea|theme）/ `created` / `updated` / `sources`（提及来源列表）
- 正文：是什么（一句话）→ 提及记录（每条：日期+来源+观点，自动累积）→ 相关实体（自动互链）

## Query 页面（Wiki/Queries/，type: query）
- frontmatter: `title`（问题）/ `asked`（日期）/ `type: query` / `sources`（答案依据）
- 正文：问题 → 答案（基于库内内容）→ 引用来源 → 备注

## Journal 页面（每日复盘）
- frontmatter: `title`（<日期> 每日复盘）/ `created` / `type: journal` / `tags` / `sources`（引用 Wiki 页）
- 正文：今日做了什么 → 今日新知（AI 从 Wiki 引用） → 📈 模式识别（近 30 天反复主题，≥3 次） → 明日计划 → 基于库内知识的建议

## CRM 页面（人脉笔记）
- frontmatter: `title`（联系人姓名）/ `created` / `updated` / `type: crm` / `tags` / `linked_entities`（关联实体页）
- 正文：背景（公司/职位/行业）→ 最近一次互动（日期/场合/聊了什么）→ 关注点 → 相关想法/事件/对话（连接万物）→ 下次跟进
"""

FILES["index.md"] = """# 知识库目录（index.md）

> 全库目录。**AI 提问前先读这里。** 每个 Wiki 页面一行：链接 + 一句话摘要。
> 最后更新：{date} ｜ 页面总数：0

## 主题总结（summary）

<!-- 示例：
- [[示例总结页]]：一句话摘要
-->

## 实体 / 概念（entity / concept）

<!-- 示例：
- [[实体-工具-OpenClaw]]：工具实体页，提及记录自动累积
-->

## 对比 / 综合分析（comparison）

## 问答沉淀（query）

<!-- 示例：
- [[Queries/2026-10-01-如何开始]]：问题 → 答案 + 来源
-->

## Journal（每日复盘）

## CRM（人脉笔记）
"""

FILES["log.md"] = """# 操作日志（log.md）

> 追加式记录，每次动作写一条。最新在上。
> 格式：`## [YYYY-MM-DD] 动作 | 主题`（动作：摄入 / 更新 / 查询 / 巡检 / 创建）

## [{date}] 创建 | 知识库初始化
- 建立全能力架构：Raw Sources（含 processed 归档）/ Wiki（含 Entities + Queries）/ Journal / CRM + AGENTS.md + SCHEMA.md
"""

FILES["欢迎.md"] = """# 欢迎来到你的第二大脑

这个库由 **豆包工作 + Obsidian** 维护，架构对标 Matt Wolfe（Obsidian+Codex）方案：
**Wiki**（知识）+ **Journal**（每日复盘）+ **CRM**（人脉）三支柱，外加**实体层**（自动提取人物/公司/工具/想法/主题）与**问答沉淀**（答案写回复利）。

## 怎么用
1. 打开豆包工作，说「把这个链接/截图/文件整理进我的知识库」
2. 内容进入 `Raw Sources/` → 生成 `Wiki/` 总结页 + `Wiki/Entities/` 实体页 → 归档到 `Raw Sources/processed/`
3. 每晚说「今天复盘一下」→ 生成 `Journal/<日期>-复盘.md`（含模式识别）
4. 问了知识库一个问题 → 答案自动沉淀到 `Wiki/Queries/`
5. 见了重要的人，说「记录一下 XX」→ 写入 `CRM/<姓名>.md`（自动关联实体）
6. 在 Obsidian 里用图视图 / 搜索 / 双括号链接探索你的知识网络

## 目录
- [[index]] 全库目录
- [[log]] 操作日志
"""

FILES["Journal/_template.md"] = """---
title: {date} 每日复盘
created: {date}
updated: {date}
type: journal
tags: [journal]
sources: [Wiki/<相关页面>.md]
confidence: medium
---

# {date} 每日复盘

## 今日做了什么
- 事项一

## 今日新知（AI 从知识库引用）
- [[相关Wiki页]]：要点一
- [[相关Wiki页]]：要点二

## 📈 模式识别（近 30 天）
- 近期反复出现的主题：待观察（扫描历史复盘后填写；≥3 次才标注）

## 明日计划
- 待办一

## 基于库内知识的建议
- 建议一（引用自知识库内容）
"""

FILES["CRM/_template.md"] = """---
title: 联系人-姓名
created: {date}
updated: {date}
type: crm
tags: [crm]
linked_entities: [Wiki/Entities/实体-公司-xxx.md, Wiki/Entities/实体-工具-xxx.md]
confidence: medium
---

# 联系人：姓名

## 背景
- 公司/职位/行业：待补充

## 最近一次互动
- 日期/场合：待补充
- 聊了什么：待补充

## 关注点
- 待补充

## 相关想法 / 事件 / 对话（连接万物）
- [[相关Wiki页]]：聊到的话题一
- [[Wiki/Entities/实体-公司-xxx]]：ta 所在公司

## 下次跟进
- 时间/方式/话题：待补充
"""

FILES["Wiki/_template.md"] = """---
title: 页面标题
created: {date}
updated: {date}
type: summary
tags: [待定]
sources: [Raw Sources/<来源文件>.md]
entities: [Wiki/Entities/<实体页>.md]
confidence: medium
---

# 页面标题

## 摘要
一句话总结。

## 关键要点
- 要点一
- 要点二

## 相关实体（自动提取）
- [[实体-人物-xxx]]：本页提及的人物
- [[实体-工具-xxx]]：本页提及的工具

## 与本库的关系（自动互链）
- 与 [[index]] 中其他页面的关联

## 与其他知识的关联
- [[相关页面]]：关联说明

## 待解答的问题
- 尚未确认的问题

## 来源
- [来源链接](https://example.com)
"""

FILES["Wiki/Entities/_template.md"] = """---
title: 实体-类型-名称
created: {date}
updated: {date}
type: entity
entity_type: tool
tags: [entity, tool]
sources: [Raw Sources/<来源文件>.md]
confidence: medium
---

# 实体：名称

## 是什么（一句话）
- 待补充

## 提及记录（自动累积）
- {date} | [[Raw Sources/<来源文件>]] | 提及内容/观点

## 相关实体（自动互链）
- [[实体-人物-xxx]]：关联说明
- [[实体-公司-xxx]]：关联说明
"""

FILES["Wiki/Queries/_template.md"] = """---
title: {date} 问题一句话
asked: {date}
updated: {date}
type: query
tags: [query]
sources: [Wiki/<答案依据页>.md]
confidence: medium
---

# 问题：一句话描述问题

## 答案（基于库内内容）
- 答案要点一（引用 [[Wiki/相关页]]）
- 答案要点二

## 引用来源
- [[Wiki/相关页]]：支撑句一
- [[Raw Sources/相关来源]]

## 备注
- 本问答由用户提问触发，答案沉淀为可复用知识
"""

FILES["Raw Sources/01-使用说明.md"] = """---
source_url: (本库内部说明)
ingested: {date}
content_type: guide
lang: zh
---

# Raw Sources 使用说明

本文件夹是**原始摄入收件箱**：

- 视频逐字稿（中英双语）
- 文章/网页提取结果
- 截图提取内容
- 对话沉淀

命名规则：`<YYYY-MM-DD>-<主题>.md`。每个文件 frontmatter 记录来源。

**处理流程**：文件进入本文件夹 → 豆包工作生成 Wiki 总结页 + 实体页 → 完成后文件移入 `processed/` 归档，收件箱保持干净。
"""

FILES["Raw Sources/processed/README.md"] = """# 已处理归档区（processed/）

**规则**：本文件夹存放**已完成处理**的原始文件——即已经生成 Wiki 总结页、提取实体并更新 index/log 后的原始逐字稿/存档。

- 收件箱（`Raw Sources/` 根目录）只保留等待处理或处理中的文件
- 归档保留原始证据，历史可追溯（图/链接仍指向 `processed/` 内的文件）
- 归档由豆包工作按 `AGENTS.md` 摄入规则自动执行，无需手动操作
"""


def _now() -> str:
    return datetime.date.today().isoformat()


def init_vault(vault: pathlib.Path, demo: bool = False) -> None:
    """生成知识库骨架。已存在的文件不覆盖。"""
    if vault.exists() and not vault.is_dir():
        sys.exit(f"错误：{vault} 存在但不是文件夹")
    vault.mkdir(parents=True, exist_ok=True)

    date = _now()
    created: list[str] = []
    for rel, content in FILES.items():
        target = vault / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        body = content.replace("{date}", date)
        if target.exists():
            print(f"跳过（已存在）: {rel}")
            continue
        target.write_text(body, encoding="utf-8")
        created.append(rel)

    # 演示库：多生成示例页，展示全能力与链接约定
    if demo:
        example = vault / "Wiki/示例-如何用本库.md"
        if not example.exists():
            example.write_text(
                """---
title: 示例-如何用本库
created: {date}
updated: {date}
type: summary
tags: [示例]
sources: [Raw Sources/01-使用说明.md]
entities: [Wiki/Entities/实体-想法-第二大脑.md]
confidence: high
---

# 示例：如何用本库

## 摘要
本库 = 三支柱（Wiki/Journal/CRM）+ 实体层 + 问答沉淀，对标 Matt Wolfe 方案。

## 关键要点
- 喂内容给豆包工作 → 双语逐字稿/提取 → 写入 Raw Sources
- 处理完生成 Wiki 总结页 + Entities 实体页 → 原始文件归档 processed/
- 每晚「今天复盘」→ Journal（含模式识别）；提问答案写回 Queries
- 每次动作更新 index 和 log

## 相关实体（自动提取）
- [[实体-想法-第二大脑]]：本页的核心概念

## 来源
- [[Raw Sources/01-使用说明]]
""".replace("{date}", date),
                encoding="utf-8",
            )
            created.append("Wiki/示例-如何用本库.md")
        edemo = vault / "Wiki/Entities/实体-想法-第二大脑.md"
        if not edemo.exists():
            edemo.write_text(
                """---
title: 实体-想法-第二大脑
created: {date}
updated: {date}
type: entity
entity_type: idea
tags: [entity, idea]
sources: [Wiki/示例-如何用本库.md]
confidence: high
---

# 实体：第二大脑（Second Brain）

## 是什么（一句话）
- 个人知识管理系统：收集、组织、检索笔记/文章/想法，让 AI 基于你自己的知识回答。

## 提及记录（自动累积）
- {date} | [[Wiki/示例-如何用本库]] | 本库的核心概念

## 相关实体（自动互链）
- [[实体-想法-LLM-Wiki]]：底层架构（待摄入补充）
""".replace("{date}", date),
                encoding="utf-8",
            )
            created.append("Wiki/Entities/实体-想法-第二大脑.md")
        jdemo = vault / "Journal/示例-复盘.md"
        if not jdemo.exists():
            jdemo.write_text(
                """---
title: {date} 每日复盘
created: {date}
type: journal
tags: [示例]
sources: [Wiki/示例-如何用本库.md]
confidence: high
---

# {date} 每日复盘

## 今日做了什么
- 初始化知识库，安装了豆包第二大脑 Skill

## 今日新知（AI 从知识库引用）
- [[示例-如何用本库]]：三支柱 + 实体层 + 问答沉淀

## 📈 模式识别（近 30 天）
- 首次复盘，暂无历史模式（30 天后自动扫描）

## 明日计划
- 喂第一份内容，验证完整链路（含实体提取与归档）

## 基于库内知识的建议
- 每次摄入后更新 index 与 log，保持目录真实
""".replace("{date}", date),
                encoding="utf-8",
            )
            created.append("Journal/示例-复盘.md")
        cdemo = vault / "CRM/示例-联系人.md"
        if not cdemo.exists():
            cdemo.write_text(
                """---
title: 联系人-示例
created: {date}
type: crm
tags: [示例]
linked_entities: [Wiki/Entities/实体-想法-第二大脑.md]
confidence: high
---

# 联系人：示例

## 背景
- 公司/职位/行业：示例公司 / 示例职位 / 示例行业

## 最近一次互动
- 日期/场合：{date} / 初次认识
- 聊了什么：聊了豆包第二大脑方案

## 关注点
- 对知识管理自动化感兴趣

## 相关想法 / 事件 / 对话（连接万物）
- [[实体-想法-第二大脑]]：本次聊天的核心话题

## 下次跟进
- 一周后 / 微信 / 分享 Skill 发布进展
""".replace("{date}", date),
                encoding="utf-8",
            )
            created.append("CRM/示例-联系人.md")

    print(f"知识库骨架已生成：{vault}")
    for rel in created:
        print(f"  + {rel}")
    print(f"共创建 {len(created)} 个文件。")


def main() -> None:
    parser = argparse.ArgumentParser(description="初始化 Obsidian 第二大脑知识库骨架")
    parser.add_argument("--vault", required=True, help="Obsidian 库路径")
    parser.add_argument("--demo", action="store_true", help="额外生成示例页面（演示用）")
    args = parser.parse_args()
    init_vault(pathlib.Path(args.vault).expanduser(), demo=args.demo)


if __name__ == "__main__":
    main()
