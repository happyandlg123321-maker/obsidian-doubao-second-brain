# 方案对比（Comparison）

## 本 Skill vs Matt Wolfe（Codex 版）——12 项能力逐条对齐

| # | Matt Wolfe 核心能力 | Codex 版实现 | 本 Skill（豆包工作版）实现 | 对齐 |
|---|---|---|---|---|
| 1 | 三支柱（Wiki/Journal/CRM） | 同一 agents.md 扩展出三支柱 | 同：AGENTS.md 一份规则驱动三支柱 | ✅ |
| 2 | LLM-Wiki 架构 | raw → 每小时总结 → 交叉链接 → 归档 | Raw Sources → Wiki → index/log → processed | ✅ |
| 3 | 定时自动化 | 每小时 cron 后台跑 | 豆包工作定时任务（每日巡检+复盘+备份） | ✅ |
| 4 | agents.md 单一控制文件 | agents.md 定义全部行为 | AGENTS.md + SCHEMA.md | ✅ |
| 5 | Web Clipper 收集 | Obsidian Web Clipper（仅网页） | 链接/截图/文件/对话直喂豆包（全类型） | ✅ |
| 6 | 私有备份 + 复合增长 | vault commit 到私有 GitHub | 每日 git commit + 私有 GitHub 远程 | ✅ |
| 7 | 实体页层（人物/公司/工具/想法/主题） | 自动生成实体页，点击反查来源 | Wiki/Entities/ 自动提取累积「提及记录」 | ✅ |
| 8 | 自动互链（auto-link + back-link） | 处理时自动交叉引用 | 摄入四步之三：查库互链 + 反向引用 | ✅ |
| 9 | raw/processed 归档 | 处理完移走，收件箱干净 | Raw Sources/processed/ 自动归档 | ✅ |
| 10 | 问答写回 | 答案写回 wiki 可复用页 | Wiki/Queries/ 问答沉淀 | ✅ |
| 11 | Journal 模式识别 | 从历史日记识别反复模式 | 近 30 天扫描，≥3 次标注 | ✅ |
| 12 | CRM 连接万物 | 人与想法/公司/事件/对话互连 | linked_entities 自动互链 | ✅ |

## 定位差异（不是缺陷，是选择）

| 维度 | Codex 版 | 本 Skill |
|---|---|---|
| 门槛 | 命令行 + OpenAI 账号/API Key | 零代码，中文 |
| 知识把关 | 全自动无人复核 | 人在环中，用户确认入库 |
| 转写能力 | 无内置（需另配） | 飞书妙记内置链路（视频→双语） |
| 隐私 | 数据上云（OpenAI） | 笔记本地，仅处理时读取 |
| 生态 | 英文 | 中文（B站/飞书） |
| 自动化频率 | 每小时 | 每日（可按需配置） |

**结论**：Codex 版适合开发者/自动化重度用户；本 Skill 适合中文用户、非技术用户、在意知识质量的用户。**核心能力已 12 项全对齐**，差异仅在工程形态与自动化频率。

## 与 Karpathy LLM-Wiki 的关系

- 架构继承：Raw Sources → Wiki → index/log 三层
- 差异：Karpathy 用 Claude Code 维护；本 Skill 用豆包工作在对话中维护
- 本 Skill 在其上扩展：实体层 + Journal + CRM + Queries + 归档（对应 Matt Wolfe 的扩展集）

## 与 Obsidian 官方插件「Second Brain」的关系

Obsidian 社区已有同名插件（AI 编译概念/实体/来源）。本 Skill 与其差异：
- 不依赖插件生态，使用豆包工作对话即服务
- 转写能力（视频→文字）为插件不具备
- 中文双语输出为差异化
- 定时自动化 + 复盘/人脉/问答沉淀/实体层为插件不具备
