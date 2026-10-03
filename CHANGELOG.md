# 更新日志（CHANGELOG）

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 与 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added — v0.3.1 补齐最后 4 项（对标 15 项全对齐）
- **会议记录自动入库**（对标 Granola）：飞书妙记/录音转写 → Raw Sources → 摄入四步，会议提及的人自动关联 CRM
- **人脉检索**：「我和 XX 上次聊了什么」→ 读 CRM/<姓名> 回答（对标 Matt 演示 where did I meet Matthew Berman）
- **提问 grounded 协议**：提问必先读 index → 定位相关页 → 基于库内回答 + 标注引用来源 + 区分库内/通用知识（核心卖点固化）
- **元数据**：Raw Sources frontmatter 增加 `author`（作者/频道名）字段
- README 新增「人脉是什么」章节（你的关系网络，不是名人录）

### Changed
- SKILL.md 能力表 12 → 15 项；触发场景/输入路由/流程增加会议入库、人脉检索、提问协议

### Added — v0.3 全能力（对标 Matt Wolfe 12 项全对齐）
- **实体页层**：`Wiki/Entities/` 自动提取人物/公司/工具/想法/主题，实体页累积「提及记录」（点击实体可见所有提到它的来源）
- **自动互链**：摄入四步之三——查 index 与现有页互相补链接 + Wiki 页反向引用来源
- **raw/processed 归档**：处理完的原始文件自动移入 `Raw Sources/processed/`，收件箱保持干净
- **问答沉淀**：`Wiki/Queries/` 答案写回，每次提问都在复利
- **Journal 模式识别**：扫描近 30 天历史复盘，同一主题/挣扎 ≥3 次标注「📈 模式识别」
- **CRM 连接万物**：`linked_entities` 字段，联系人自动关联公司/工具/话题实体并互链
- **自动备份**：每日 git commit（可配置私有 GitHub 远程自动 push）
- init_vault.py 升级：骨架生成 16 文件（Entities/Queries/processed 模板 + 演示页），已验证幂等

### Changed
- SKILL.md / README.md / docs×3 / examples 全部升级到全能力版
- docs/COMPARISON.md 改为 12 项逐条对齐表

## [0.2.0] - 2026-10-02

### Added
- **三支柱架构**：Journal（每日复盘）+ CRM（人脉笔记），对标 Matt Wolfe
- init_vault.py：Journal/CRM 目录与模板（12 文件，幂等）
- 定时自动化章节、备份建议、六特性对齐表

## [0.1.0] - 2026-10-01

### Added
- 首个可用版本：豆包工作 + Obsidian 第二大脑全流程跑通（实际环境验证）
- LLM-Wiki 三层架构：Raw Sources / Wiki / index + log
- 人在环中入库规范与隐私拦截
- 视频转写链路：B站/YouTube → 飞书妙记 → 中英双语逐字稿
