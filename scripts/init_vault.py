#!/usr/bin/env python3
"""init_vault.py — 初始化 Obsidian 第二大脑知识库骨架。

用法:
  python3 init_vault.py --vault /路径/到/Obsidian库      # 生成知识库骨架
  python3 init_vault.py --vault /路径/到/库 --demo        # 带示例内容的演示库

生成结构:
  Raw Sources/        # 原始摄入（逐字稿/文章存档）
  Wiki/               # AI 维护的总结/概念页
  Journal/            # 每日复盘日记（AI 从 Wiki 取知识做复盘）
  CRM/                # 人脉笔记（见过谁/聊过什么/下次跟进）
  AGENTS.md           # 规则层（告诉豆包工作如何维护本库）
  SCHEMA.md           # 页面结构 Schema
  index.md            # 全库目录
  log.md              # 操作日志
  欢迎.md              # 入库起点

特性: 幂等——已存在的文件不会被覆盖；目录缺失自动创建。
纯 Python 标准库，无第三方依赖。
"""

import argparse
import datetime
import pathlib
import sys

FILES: dict[str, str] = {}

FILES["AGENTS.md"] = """# 知识库规则（AGENTS.md）

> 豆包工作维护本库时必须遵守的规则。**一份规则文件同时驱动三支柱：Wiki / Journal / CRM。**

## 目录结构
- `Raw Sources/`：原始摄入存档（逐字稿/提取内容），文件命名 `<日期>-<主题>.md`
- `Wiki/`：AI 维护的总结/概念页，用双括号 `[[链接]]` 互连
- `Journal/`：每日复盘日记，AI 自动从 Wiki 取知识做复盘（文件命名 `<日期>-复盘.md`）
- `CRM/`：人脉笔记（联系人背景/互动记录/下次跟进），文件命名 `<姓名>.md`
- `index.md`：全库目录（AI 提问前先读这里）
- `log.md`：操作日志（追加式，最新在上）

## 规则
- 先结果后依据；数字/统计须可验证
- 不编造内容；截断/受限时标「待补充」
- 保留用户已有改动，不覆盖无关工作
- 敏感信息（证照/密码/家庭住址/资产）拒绝入库
- 每次摄入/更新写 `log.md`，页面增减同步 `index.md`
- 每日复盘：从 Wiki 中挑选与当日工作最相关的 1-3 页引用，形成「今日新知」
- CRM 录入：记录背景、最近互动、关注点、下次跟进四项，缺省标「待补充」
"""

FILES["SCHEMA.md"] = """# 页面结构 Schema（SCHEMA.md）

## Raw Sources 页面
- frontmatter: `source_url`（来源链接）/ `ingested`（日期）/ `content_type`（video/article/image）/ `lang`（zh-en 等）
- 正文：原始内容/双语逐字稿/提取结果，保留来源信息

## Wiki 页面
- frontmatter: `title` / `created` / `updated` / `type`（summary|concept）/ `tags` / `sources`（指向 Raw Sources）
- 正文：摘要 → 关键要点 → 与本库的关系 → 与其他知识的关联 → 待解答的问题 → 来源

## Journal 页面（每日复盘）
- frontmatter: `title`（<日期> 每日复盘）/ `created` / `type: journal` / `tags` / `sources`（引用 Wiki 页）
- 正文：今日做了什么 → 今日新知（AI 从 Wiki 引用） → 明日计划 → 基于库内知识的建议

## CRM 页面（人脉笔记）
- frontmatter: `title`（联系人姓名）/ `created` / `updated` / `type: crm` / `tags`
- 正文：背景（公司/职位/行业）→ 最近一次互动（日期/场合/聊了什么）→ 关注点 → 下次跟进
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
- [[示例概念页]]：概念定义
-->

## 对比 / 综合分析（comparison）

## 问答沉淀（query）

## Journal（每日复盘）

## CRM（人脉笔记）
"""

FILES["log.md"] = """# 操作日志（log.md）

> 追加式记录，每次动作写一条。最新在上。
> 格式：`## [YYYY-MM-DD] 动作 | 主题`（动作：摄入 / 更新 / 查询 / 巡检 / 创建）

## [{date}] 创建 | 知识库初始化
- 建立三支柱架构：Raw Sources / Wiki / Journal / CRM + AGENTS.md + SCHEMA.md
"""

FILES["欢迎.md"] = """# 欢迎来到你的第二大脑

这个库由 **豆包工作 + Obsidian** 维护，三支柱架构对标 Matt Wolfe（Obsidian+Codex）方案：
**Wiki**（知识库）+ **Journal**（每日复盘）+ **CRM**（人脉笔记）。

## 怎么用
1. 打开豆包工作，说「把这个链接/截图/文件整理进我的知识库」
2. 内容会进入 `Raw Sources/`（原始存档）和 `Wiki/`（总结页）
3. 每晚说「今天复盘一下」，AI 从 Wiki 取知识生成 `Journal/<日期>-复盘.md`
4. 见了重要的人，说「记录一下 XX」，AI 写入 `CRM/<姓名>.md`
5. 在 Obsidian 里用图视图 / 搜索 / 双括号链接探索你的知识网络

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
confidence: medium
---

# 页面标题

## 摘要
一句话总结。

## 关键要点
- 要点一
- 要点二

## 与本库的关系
- 与 [[index]] 中其他页面的关联

## 与其他知识的关联
- [[相关页面]]：关联说明

## 待解答的问题
- 尚未确认的问题

## 来源
- [来源链接](https://example.com)
"""

FILES["Raw Sources/01-使用说明.md"] = """---
source_url: (本库内部说明)
ingested: {date}
content_type: guide
lang: zh
---

# Raw Sources 使用说明

本文件夹存放**原始摄入内容**：

- 视频逐字稿（中英双语）
- 文章/网页提取结果
- 截图提取内容
- 对话沉淀

命名规则：`<YYYY-MM-DD>-<主题>.md`。每个文件 frontmatter 记录来源。
由 Wiki 页通过 `sources` 字段引用。
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

    # 演示库：多生成示例页，展示三支柱与链接约定
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
confidence: high
---

# 示例：如何用本库

## 摘要
本库三支柱 = Wiki（知识）+ Journal（每日复盘）+ CRM（人脉）。

## 关键要点
- 喂内容给豆包工作 → 自动生成双语逐字稿/提取 → 写入 Raw Sources
- Wiki 页与 Raw Sources 用双括号 `[[链接]]` 关联
- 每晚说「今天复盘」→ 生成 Journal；见了人说「记录一下 XX」→ 写入 CRM
- 每次动作更新 index 和 log

## 来源
- [[Raw Sources/01-使用说明]]
""".replace("{date}", date),
                encoding="utf-8",
            )
            created.append("Wiki/示例-如何用本库.md")
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
- [[示例-如何用本库]]：三支柱 = Wiki + Journal + CRM

## 明日计划
- 喂第一份内容，验证完整链路

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
