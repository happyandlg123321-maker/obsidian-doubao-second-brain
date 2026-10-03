# Obsidian Doubao Second Brain（豆包第二大脑）

> **EN TL;DR**: A Doubao Work (豆包工作) Skill that turns **Obsidian** into a self-updating second brain — **three pillars**: Wiki (knowledge base), Journal (daily review grounded in your vault), CRM (contact memory). Feed in videos / articles / screenshots / links, transcribe with Feishu Minutes (飞书妙记), produce bilingual (EN/中文) notes. The Chinese, no-code counterpart of Matt Wolfe's *Obsidian + Codex* setup.

用 **豆包工作 + Obsidian** 搭建的「第二大脑」开源 Skill——对标 Matt Wolfe《Build A Second Brain That Remembers Everything》（Obsidian + Codex）方案的中文零代码版，**三支柱架构**。

- 🧠 **三支柱**：**Wiki**（知识库）+ **Journal**（每日复盘，AI 从你的库里取依据）+ **CRM**（人脉笔记）
- 🎙 **飞书妙记转写**：视频自动转逐字稿（B站试看受限时自动溯源 YouTube 原版）
- 🌐 **中英双语**：逐字稿段落级 EN 原文 + 中文意译
- 📚 **LLM-Wiki 架构**：`Raw Sources`（原始摄入）→ `Wiki`（AI 维护总结）→ `index.md` + `log.md`
- 🤝 **人在环中**：哪些入库、怎么翻译，由你决定——不是全自动的黑盒

---

## 三支柱（Three Pillars）

| 支柱 | 目录 | 干什么 | 怎么说一句话触发 |
|---|---|---|---|
| **Wiki** | `Wiki/` | 收藏内容 → AI 加工成可检索的总结页，双括号互链 | 「把这个链接整理进知识库」 |
| **Journal** | `Journal/` | 每日复盘，AI 从 Wiki 挑出与今天最相关的内容形成「今日新知」 | 「今天复盘一下」 |
| **CRM** | `CRM/` | 人脉笔记：背景 / 最近互动 / 关注点 / 下次跟进 | 「记录一下刚才见的 XX」 |

三根支柱由**一份规则文件**（`AGENTS.md`）同时驱动——对标 Matt Wolfe 的 agents.md 单一控制文件。

---

## 架构（Architecture）

```mermaid
flowchart LR
    A[视频链接] --> D[豆包工作<br>对话触发]
    B[文章/网页链接] --> D
    C[截图/本地文件/对话] --> D
    D --> E[飞书妙记转写]
    D --> F[内容提取/结构整理]
    E --> G[段落级中英双语逐字稿]
    F --> G
    G --> H[Raw Sources 原始存档]
    H --> I[Wiki AI 维护总结页]
    I --> J[index.md 目录]
    I --> K[log.md 操作日志]
    I --> J2[Journal 每日复盘]
    I --> C2[CRM 人脉笔记]
    J --> L[Obsidian 本地库<br>Markdown 全文可检索]
    K --> L
    J2 --> L
    C2 --> L
```

与 Matt Wolfe 方案逐特性对齐：

| # | Matt Wolfe 核心特性 | 本 Skill 实现 |
|---|---|---|
| 1 | 三支柱（Wiki + Journal + CRM） | ✅ 三支柱齐备 |
| 2 | LLM-Wiki 架构（raw → 总结 → 交叉链接） | ✅ Raw Sources → Wiki → index/log |
| 3 | 每小时自动化 | ✅ 豆包工作定时任务（每日巡检 + 复盘） |
| 4 | agents.md 单一控制文件 | ✅ AGENTS.md 一份规则驱动三支柱 |
| 5 | Web Clipper 收集 | ✅ 等价：链接/截图/文件直喂豆包 |
| 6 | 私有备份 + 复合增长 | ✅ 建议私有仓库备份；每摄入一条，库更聪明 |

---

## 快速开始（Quick Start）

### 前置条件
1. 安装 [Obsidian](https://obsidian.md/)，新建一个库（vault）
2. 豆包工作（本地客户端 / 云电脑 / 网页端均可用）

### 安装 Skill
1. 下载本仓库
2. 把仓库根目录作为豆包工作 Skill 安装（或将 `SKILL.md` 所在目录加入豆包工作技能根目录）
3. 用仓库内 `scripts/init_vault.py` 初始化知识库骨架：

```bash
python3 scripts/init_vault.py --vault "/你的/Obsidian/库路径"
```

会生成三支柱骨架：`Raw Sources/`、`Wiki/`、`Journal/`、`CRM/`、`AGENTS.md`、`SCHEMA.md`、`index.md`、`log.md`、`欢迎.md`。

### 依赖与说明（Dependencies）

| 能力 | 用途 | 获取方式 |
|---|---|---|
| 豆包工作 | 对话式 AI 入口（Skill 运行宿主） | [豆包工作官网](https://www.doubao.com/) 安装桌面端 |
| 飞书妙记 | 视频 → 逐字稿转写 | 豆包工作内授权飞书账号，首次视频转写会自动触发授权 |
| doubao-video-extract | 视频下载/转音频/妙记链路 | 豆包工作内置视频提取能力；若你的环境没有，可跳过视频类输入（文章/截图/文件仍可用） |

> **给首次使用者的提示**：本 Skill 的核心是"对话驱动"——你不需要配置 API Key。视频转写能力依赖飞书妙记授权；若只想先跑通文本/截图/链接入库，无需任何额外授权。

### 喂第一份内容
打开豆包工作，直接说：

> 把这个链接/截图/文件的内容整理进我的 Obsidian 知识库，做成中英双语

豆包会走完整链路：提取 →（视频则转写）→ 双语 → 写 Raw Sources → 更新 Wiki/index/log。

> Obsidian 外接卷新文件需 `Cmd+P → Reload app` 刷新。

### 用第二、第三支柱

> 「今天复盘一下」→ 生成 `Journal/<日期>-复盘.md`（AI 从 Wiki 引用今日新知）
>
> 「记录一下 XX，XX 公司的」→ 生成 `CRM/<姓名>.md`（背景/互动/关注点/下次跟进）

---

## 知识库规范（Vault Convention）

```
你的库/
├── Raw Sources/          # 原始摄入：逐字稿、原文存档（AI 提取物）
├── Wiki/                 # AI 维护的总结/概念页（知识支柱）
├── Journal/              # 每日复盘（复盘支柱）
├── CRM/                  # 人脉笔记（人脉支柱）
├── AGENTS.md             # 告诉豆包工作如何维护本库（规则层，驱动三支柱）
├── SCHEMA.md             # 页面结构 Schema
├── index.md              # 全库目录（AI 提问前先读这里）
├── log.md                # 操作日志（最新在上）
└── 欢迎.md               # 入库起点
```

- Wiki / Journal / CRM 页面互相用 Obsidian 双括号 `[[链接]]` 关联
- 每次摄入/更新都写 `log.md`，同步 `index.md` 页面总数

---

## 效果示例（Preview）

`scripts/init_vault.py` 初始化后的库结构（--demo 含示例页）：

```text
你的库/
├── Raw Sources/01-使用说明.md          # 原始摄入指引
├── Wiki/_template.md                  # 总结页模板
├── Journal/_template.md               # 每日复盘模板
├── CRM/_template.md                   # 人脉笔记模板
├── AGENTS.md                          # 规则层（驱动三支柱）
├── SCHEMA.md                          # 页面 Schema
├── index.md                           # 全库目录（页面总数随摄入增长）
├── log.md                             # 操作日志
└── 欢迎.md                            # 入库起点
```

一次真实视频摄入后的产物（真实案例）：

```text
Raw Sources/2026-10-01-obsidian专家系统-zettelkasten.md   # 21 段落中英双语逐字稿
Wiki/Obsidian-Zettelkasten成为专家系统.md                  # AI 维护的总结页
Journal/2026-10-01-复盘.md                                 # 当日复盘引用该页
index.md  → 页面总数 8，新增一行摘要
log.md    → 追加：来源/链路/创建文件
```

Obsidian 图视图中：Raw Sources → Wiki 总结页 → Journal/CRM 页，双括号 `[[链接]]` 形成知识网络。

---

## 文档（Docs）

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — 架构与对标分析（三支柱）
- [docs/SOP.md](docs/SOP.md) — 视频/文章/截图/复盘/CRM 的标准操作流程
- [docs/COMPARISON.md](docs/COMPARISON.md) — 与 Matt Wolfe 方案、Karpathy LLM-Wiki 的逐特性对比

## 示例模板（Examples）

- [examples/vault-template](examples/vault-template/) — 可直接复制进 Obsidian 的知识库骨架模板（AGENTS / SCHEMA / index / log / Wiki / Journal / CRM）

---

## 隐私（Privacy）

- 你的笔记永远留在本机 Obsidian 库，Markdown 明文
- 豆包工作只在处理时读取你喂的内容，不采集库内历史笔记
- 视频转写经飞书妙记（需豆包工作授权），转写结果回落本地库
- **备份建议**：库目录定期 commit 到私有 GitHub 仓库（或 Obsidian Sync），防数据丢失——私有仓库不公开你的笔记

## 许可（License）

[MIT](LICENSE)

---

## 致谢（Credits）

- Andrej Karpathy — [LLM Wiki](https://gist.github.com/karpathy/00103b0037c5a36c4870588b1a0c0d8d) 概念
- Matt Wolfe — Obsidian + Codex 第二大脑方案（本项目的英文对标：三支柱 + 自动化 + agents.md）
- 飞书妙记 — 视频转写能力
