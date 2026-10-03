# 标准操作流程（SOP）

## 流程 A：视频链接入库（B站 / YouTube）

```text
1. 用户给链接
   ├─ b23.tv 短链 → 先解析 302 完整 URL（保留 buvid 等参数，防 412）
   └─ YouTube watch 链接 → 直接进入下载
2. 下载（yt-dlp）
3. 转音频（PyAV → mp3）
4. 上传飞书妙记 → 等待转写完成（minute not ready 时轮询）
5. 读取 transcript.txt
6. 生成段落级中英双语逐字稿（EN 原文 + 中文意译）
7. 写入 Raw Sources/<日期>-<主题>.md
8. 执行摄入四步（见流程 H）
9. 提示用户 Obsidian Reload（外接卷）
```

**坑位提醒**：
- 视频显示「充电/会员专属」仅试看：从简介/搜索溯源 YouTube 原版取完整版
- 转写临时 RPC 超时：等待 60–90s 重试
- 截断内容如实标「待补充」，不编造

## 流程 B：文章/网页链接入库

```text
1. 抓取正文（web fetch，分页读完）
2. 结构化整理：标题/来源/关键要点/引文
3. 写 Raw Sources/<日期>-<主题>.md（frontmatter 记 source_url）
4. 执行摄入四步（见流程 H）
5. 更新 index/log
```

## 流程 C：截图 / 豆包工作界面入库

```text
1. 读图提取文字与结构（OCR）
2. 按内容类型处理：列表→分类索引，文档→全文存档
3. 写 Raw Sources 或 Wiki（视内容）
4. 执行摄入四步（见流程 H）
```

## 流程 D：知识库初始化（新用户）

```bash
python3 scripts/init_vault.py --vault /路径/到/库
```

生成全能力骨架：`Raw Sources/`（含 `processed/` 归档区）、`Wiki/`（含 `Entities/` + `Queries/`）、`Journal/`、`CRM/`、`AGENTS.md`、`SCHEMA.md`、`index.md`、`log.md`、`欢迎.md`

## 流程 E：每日复盘（Journal）

```text
1. 用户说「今天复盘」
2. 读 index.md + Wiki 最近更新（近 7 天）
3. 扫描近 30 天历史复盘，识别反复主题（≥3 次 → 📈 模式识别）
4. 生成 Journal/<日期>-复盘.md：
   今日做了什么（用户提供，缺省标待补充）
   今日新知（从 Wiki 引用 1-3 页，双括号链接）
   📈 模式识别（近 30 天反复主题）
   明日计划（用户提供或 AI 建议）
   基于库内知识的建议（引用自 Wiki 内容）
5. 更新 index/log
```

## 流程 F：人脉录入（CRM，连接万物）

```text
1. 用户说「记录一下 XX」
2. 查 CRM/ 是否已有 <姓名>.md：
   已有 → 追加「最近一次互动」（保留原内容）
   没有 → 新建（背景/最近互动/关注点/下次跟进）
3. 自动检索库中相关实体页（所在公司/提到的工具/聊过的主题），写入 linked_entities 并互链
4. 缺省字段标「待补充」，不虚构
5. 更新 index/log
```

**人脉检索**（对标 Matt 演示「where did I meet Matthew Berman」）：
```text
1. 用户问「我和 XX 上次聊了什么」「XX 是哪家公司的」
2. 读 CRM/<姓名>.md 的「最近一次互动」/「背景」
3. 库内无记录 → 如实说明，提示用户补充，不虚构
```

## 流程 G：提问 grounded 协议 + 问答沉淀（Queries 写回）

```text
1. 用户向知识库提问（如「我对 XX 有什么认知？」）
2. 读 index.md 定位相关页
3. 读取相关 Wiki/Entities/CRM/Queries 页
4. 基于库内内容回答，标注引用来源（[[Wiki/相关页]]）
5. 库内没有的部分明确区分「库内知识」与「通用 AI 知识」
6. 答案有复用价值时 → 写回 Wiki/Queries/<日期>-<问题>.md
7. 更新 index/log
```

## 流程 H：摄入四步（每次处理原始内容必做）

```text
1. 总结     → 生成 Wiki/<主题>.md（摘要/要点/相关实体/关联）
2. 提取实体 → 扫描人物/公司/工具/想法/主题
             创建或更新 Wiki/Entities/<实体>.md
             追加「提及记录」（日期+来源+观点）
3. 自动互链 → 查 index + 现有 Wiki/Entities 页
             同主题/同实体互相补双括号链接
             Wiki 页反向引用来源笔记
4. 归档     → 原始文件移入 Raw Sources/processed/
```

## 流程 I：定时巡检与备份（可选，推荐）

用豆包工作定时任务（doubao-cron-scheduler）配置：
- 每日 09:00：读 index.md 与库内文件核对一致性，差异写 log.md
- 每日 22:00：执行流程 E 生成当日复盘（若用户当天未手动复盘）
- 每日 23:00：git add -A + commit（本机可用时）；配置私有 GitHub remote 后自动 push

## 流程 J：会议录音入库（对标 Granola 会议注入）

```text
1. 用户提供会议录音（或引用豆包工作已录制的音频）
2. 录音转写（豆包录音转写 / analyze_audio）
3. 逐字稿写入 Raw Sources/<日期>-<会议主题>.md
   frontmatter: content_type=meeting, author=参会人/组织
4. 执行摄入四步（流程 H：总结/实体/互链/归档）
5. 会议提及的人 → 自动关联 CRM（已存在追加互动；不存在提示用户创建）
6. 更新 index/log
```

## 通用规则

- **先结果后依据**；数字/统计须可验证
- **不编造**：无来源内容标「待补充」；实体提及记录只记真实出现的信息
- **保留用户改动**：不覆盖用户重命名/编辑过的页面
- **隐私拦截**：证照/密码/家庭住址/资产内容拒绝入库
- 每次动作写 `log.md`，页面增减同步 `index.md`
- **备份**：每日 git commit；私有 GitHub 仓库不公开你的笔记
