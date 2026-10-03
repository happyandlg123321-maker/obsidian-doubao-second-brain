---
name: obsidian-doubao-second-brain
description: 用豆包工作 + Obsidian 搭建「第二大脑」知识库，三支柱架构（Wiki 知识库 + Journal 每日复盘 + CRM 人脉笔记）。对标 Matt Wolfe 的 Obsidian+Codex 方案，中文零代码版：视频链接（B站/YouTube）、文章链接、截图、本地文件、对话内容 → 提取/转写 → 中英双语 → 写入 Obsidian 库。当用户说「把这个链接/截图/视频整理进我的 Obsidian」「同步到知识库」「做中英双语入库」「今天复盘」「记录一下 XX（人脉）」等时使用。使用前要求 Obsidian 库已初始化（含 AGENTS.md/SCHEMA.md/index.md/log.md，可用 scripts/init_vault.py 生成）。
---

# 豆包第二大脑（Obsidian Second Brain）

将外部内容持续沉淀进用户的 Obsidian 本地库，形成可检索、可复利、三支柱驱动的知识系统。

## 三支柱

| 支柱 | 目录 | 用途 | 触发话术 |
|---|---|---|---|
| Wiki | `Wiki/` | 知识总结页（摄入内容加工后） | 「整理进知识库」 |
| Journal | `Journal/` | 每日复盘（AI 从 Wiki 取知识） | 「今天复盘」 |
| CRM | `CRM/` | 人脉笔记（背景/互动/跟进） | 「记录一下 XX」 |

## 触发场景

- 用户给出链接（视频/文章/网页）并要求入库
- 用户上传截图/本地文件并要求提取入库
- 用户说「同步到 Obsidian」「整理进知识库」「做成中英双语」
- 用户说「今天复盘/写日记」→ 生成 Journal
- 用户说「记录一下 XX」「刚才见了 XX」→ 写入 CRM

## 前置条件检查

1. 确认用户 Obsidian 库路径（含 `Raw Sources/`、`Wiki/`、`Journal/`、`CRM/`、`index.md`、`log.md`）
2. 库未初始化时：运行 `scripts/init_vault.py --vault <路径>` 生成骨架（含三支柱模板）
3. 视频转写需要豆包工作授权飞书妙记（首次使用会触发授权）

## 工作流程

### 1. 输入路由

| 输入类型 | 处理链路 |
|---|---|
| B站/YouTube 视频链接 | 下载 → 转音频 → 飞书妙记转写 → 双语逐字稿 |
| 文章/网页链接 | 抓取正文 → 结构化整理 |
| 截图/豆包工作界面 | 读图提取文字与结构 |
| 本地文件（md/docx/pdf） | 读取 → 转写或摘要 |
| 对话内容 | 直接整理成笔记 |
| 「今天复盘」 | 读 Wiki 最近更新 → 生成 Journal/<日期>-复盘.md |
| 「记录 XX」 | 查 CRM 是否已有 → 新建/追加 <姓名>.md |

### 2. 视频转写链路（doubao-video-extract Skill 能力）

- B站视频：优先用分享短链（保留 buvid 参数防 412）
- 遇到「充电/会员专属」试看限制：从简介/搜索溯源 YouTube 原版，取完整版
- 转写产物：段落级逐字稿（含时间戳），再生成中英双语版本

### 3. 入库规范（LLM-Wiki 三层 + 两支柱）

- `Raw Sources/<日期>-<主题>.md`：原始摄入存档（双语逐字稿/提取内容），frontmatter 含 source_url/ingested/content_type/lang
- `Wiki/<主题>.md`：AI 维护的 summary 页（摘要/关键要点/与本库关系/来源），用双括号 `[[链接]]` 关联
- `Journal/<日期>-复盘.md`：每日复盘（今日做了什么/今日新知从 Wiki 引用/明日计划/库内建议）
- `CRM/<姓名>.md`：人脉笔记（背景/最近互动/关注点/下次跟进）
- `index.md`：更新页面总数与摘要行
- `log.md`：顶部追加摄入记录（动作/来源/链路/创建文件）

### 4. 自动化（可选，推荐）

用豆包工作定时任务（doubao-cron-scheduler）配置每日巡检：
- 每日 09:00：读 index.md 与库内文件核对一致性，更新 log.md
- 每日 22:00：生成当日 Journal 复盘（引用 Wiki 最近更新）

### 5. 交付

- 报告产物路径与内容概要
- 提醒 Obsidian 外接卷需 `Cmd+P → Reload app` 刷新
- 涉及隐私（银行卡/密码/证件/家庭住址/资产）内容拒绝入库
- 备份建议：库目录定期 commit 到私有 GitHub 仓库或 Obsidian Sync

## 反模式

- 不编造转写内容；截断/受限时如实标注「待补充」
- 不覆盖用户已有改动（如用户改名的页面）
- 不把用户私有提示词/内部资料写入公开材料
- 不从搜索/浏览器替代转写证据（视频内容必须来自转写产物）
- Journal/CRM 缺省字段标「待补充」，不替用户虚构事实（如"昨天见了谁"）
