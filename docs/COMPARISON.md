# 方案对比（Comparison）

## 本 Skill vs Matt Wolfe（Codex 版）

| 维度 | Matt Wolfe（Obsidian + Codex） | 本 Skill（Obsidian + 豆包工作） |
|---|---|---|
| 触发 | Codex CLI / 每小时自动化 | 豆包工作对话，一句话触发 |
| 内容收集 | Obsidian Web Clipper（仅网页） | 链接/截图/文件/对话全类型 |
| 视频转写 | 无内置（需另配） | 飞书妙记内置链路 |
| 自动化程度 | 全自动后台跑 | 人在环中，半自动 |
| 门槛 | 命令行 + OpenAI 账号/API Key | 零代码，中文 |
| 知识把关 | 无人复核 | 用户确认后入库 |
| 隐私 | 数据上云（OpenAI） | 笔记本地，仅处理时读取 |
| 语言 | 英文生态 | 中文生态（B站/飞书） |

**结论**：目标人群不同——Codex 版适合开发者/自动化重度用户；本 Skill 适合中文用户、非技术用户、在意知识质量的用户。两者可并存：本 Skill 管"摄入与入库"，Codex 版管"定时后台自动化"。

## 与 Karpathy LLM-Wiki 的关系

- 架构继承：Raw Sources → Wiki → index/log 三层
- 差异：Karpathy 用 Claude Code 维护；本 Skill 用豆包工作在对话中维护
- 本库实际落地（示例）：
  - `Raw Sources/` = 视频逐字稿、文章存档
  - `Wiki/` = 总结页（如《Obsidian-Zettelkasten成为专家系统》）
  - `index.md` = 提问前必读目录

## 与 Obsidian 官方插件「Second Brain」的关系

Obsidian 社区已有同名插件（AI 编译概念/实体/来源）。本 Skill 与其差异：
- 不依赖插件生态，使用豆包工作对话即服务
- 转写能力（视频→文字）为插件不具备
- 中文双语输出为差异化
