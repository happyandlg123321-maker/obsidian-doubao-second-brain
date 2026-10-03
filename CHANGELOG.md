# 更新日志（CHANGELOG）

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 与 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added
- **三支柱架构**：新增 Journal（每日复盘）与 CRM（人脉笔记）两支柱，对标 Matt Wolfe 方案
- `init_vault.py` 升级：骨架生成 Journal/CRM 目录与模板（--demo 含三支柱示例页）
- SKILL.md 升级：三支柱触发话术（「今天复盘」「记录一下 XX」）、定时自动化章节、备份建议
- README 升级：三支柱介绍、与 Matt Wolfe 六特性逐条对齐表、备份建议
- docs 升级：ARCHITECTURE（三支柱）、SOP（新增流程 E 复盘 / F CRM / G 定时巡检）、COMPARISON（六特性对齐）
- examples/vault-template 升级：新增 Journal/_template.md、CRM/_template.md
- 发布清单 RELEASE.md

## [0.1.0] - 2026-10-01

### Added
- 首个可用版本：豆包工作 + Obsidian 第二大脑全流程跑通（实际环境验证）
- LLM-Wiki 三层架构：Raw Sources / Wiki / index + log
- 人在环中入库规范与隐私拦截
- 视频转写链路：B站/YouTube → 飞书妙记 → 中英双语逐字稿
