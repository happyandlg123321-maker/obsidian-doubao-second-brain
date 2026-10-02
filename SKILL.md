---
name: obsidian-doubao-second-brain
description: 用豆包工作 + Obsidian 搭建「第二大脑」知识库。对标 Matt Wolfe 的 Obsidian+Codex 方案，中文零代码版：视频链接（B站/YouTube）、文章链接、截图、本地文件、对话内容 → 提取/转写 → 中英双语 → 写入 Obsidian 库（Raw Sources 原始存档 + Wiki 总结页 + index/log 维护）。当用户说「把这个链接/截图/视频整理进我的 Obsidian」「同步到知识库」「做中英双语入库」等时使用。使用前要求 Obsidian 库已初始化（含 AGENTS.md/SCHEMA.md/index.md/log.md）。
---

# 豆包第二大脑（Obsidian Second Brain）

将外部内容持续沉淀进用户的 Obsidian 本地库，形成可检索、可复利的知识库。

## 触发场景

- 用户给出链接（视频/文章/网页）并要求入库
- 用户上传截图/本地文件并要求提取入库
- 用户说「同步到 Obsidian」「整理进知识库」「做成中英双语」

## 前置条件检查

1. 确认用户 Obsidian 库路径（含 `Raw Sources/`、`Wiki/`、`index.md`、`log.md`）
2. 库未初始化时：运行 `scripts/init_vault.py --vault <路径>` 生成骨架
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

### 2. 视频转写链路（doubao-video-extract Skill 能力）

- B站视频：优先用分享短链（保留 buvid 参数防 412）
- 遇到「充电/会员专属」试看限制：从简介/搜索溯源 YouTube 原版，取完整版
- 转写产物：段落级逐字稿（含时间戳），再生成中英双语版本

### 3. 入库规范（LLM-Wiki 三层）

- `Raw Sources/<日期>-<主题>.md`：原始摄入存档（双语逐字稿/提取内容），frontmatter 含 source_url/ingested/content_type/lang
- `Wiki/<主题>.md`：AI 维护的 summary 页（摘要/关键要点/与本库关系/来源），用双括号 `[[链接]]` 关联
- `index.md`：更新页面总数与摘要行
- `log.md`：顶部追加摄入记录（动作/来源/链路/创建文件）

### 4. 交付

- 报告产物路径与内容概要
- 提醒 Obsidian 外接卷需 `Cmd+P → Reload app` 刷新
- 涉及隐私（银行卡/密码/证件/家庭住址/资产）内容拒绝入库

## 反模式

- 不编造转写内容；截断/受限时如实标注「待补充」
- 不覆盖用户已有改动（如用户改名的页面）
- 不把用户私有提示词/内部资料写入公开材料
- 不从搜索/浏览器替代转写证据（视频内容必须来自转写产物）
