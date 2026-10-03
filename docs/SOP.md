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
8. 生成 Wiki/<主题>.md 总结页
9. 更新 index.md（总数+摘要）与 log.md（追加记录）
10. 提示用户 Obsidian Reload（外接卷）
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
4. 可选：生成 Wiki 总结页
5. 更新 index/log
```

## 流程 C：截图 / 豆包工作界面入库

```text
1. 读图提取文字与结构（OCR）
2. 按内容类型处理：列表→分类索引，文档→全文存档
3. 写 Raw Sources 或 Wiki（视内容）
4. 更新 index/log
```

## 流程 D：知识库初始化（新用户）

```bash
python3 scripts/init_vault.py --vault /路径/到/库
```

生成三支柱骨架：`Raw Sources/` `Wiki/` `Journal/` `CRM/` `AGENTS.md` `SCHEMA.md` `index.md` `log.md` `欢迎.md`

## 流程 E：每日复盘（Journal）

```text
1. 用户说「今天复盘」
2. 读 index.md + Wiki 最近更新（近 7 天）
3. 生成 Journal/<日期>-复盘.md：
   今日做了什么（用户提供，缺省标待补充）
   今日新知（从 Wiki 引用 1-3 页，双括号链接）
   明日计划（用户提供或 AI 建议）
   基于库内知识的建议（引用自 Wiki 内容）
4. 更新 index/log
```

## 流程 F：人脉录入（CRM）

```text
1. 用户说「记录一下 XX」
2. 查 CRM/ 是否已有 <姓名>.md：
   已有 → 追加「最近一次互动」（保留原内容）
   没有 → 新建（背景/最近互动/关注点/下次跟进）
3. 缺省字段标「待补充」，不虚构
4. 更新 index/log
```

## 流程 G：定时巡检（可选，推荐）

用豆包工作定时任务（doubao-cron-scheduler）配置：
- 每日 09:00：读 index.md 与库内文件核对一致性，差异写 log.md
- 每日 22:00：执行流程 E 生成当日复盘（若用户当天未手动复盘）

## 通用规则

- **先结果后依据**；数字/统计须可验证
- **不编造**：无来源内容标「待补充」
- **保留用户改动**：不覆盖用户重命名/编辑过的页面
- **隐私拦截**：证照/密码/家庭住址/资产内容拒绝入库
- 每次动作写 `log.md`，页面增减同步 `index.md`
- **备份**：建议库目录定期 commit 到私有 GitHub 仓库或 Obsidian Sync
