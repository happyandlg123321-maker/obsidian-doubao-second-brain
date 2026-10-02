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

生成：`Raw Sources/` `Wiki/` `AGENTS.md` `SCHEMA.md` `index.md` `log.md` `欢迎.md`

## 通用规则

- **先结果后依据**；数字/统计须可验证
- **不编造**：无来源内容标「待补充」
- **保留用户改动**：不覆盖用户重命名/编辑过的页面
- **隐私拦截**：证照/密码/家庭住址/资产内容拒绝入库
- 每次动作写 `log.md`，页面增减同步 `index.md`
