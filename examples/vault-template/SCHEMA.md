# 页面结构 Schema（SCHEMA.md）

## Raw Sources 页面
- frontmatter: `source_url`（来源链接）/ `ingested`（日期）/ `content_type`（video/article/image）/ `lang`（zh-en 等）
- 正文：原始内容/双语逐字稿/提取结果，保留来源信息
- 处理完成后文件移入 `Raw Sources/processed/`

## Wiki 页面（summary/concept）
- frontmatter: `title` / `created` / `updated` / `type`（summary|concept）/ `tags` / `sources`（指向 Raw Sources）/ `entities`（相关实体页）
- 正文：摘要 → 关键要点 → 相关实体（自动提取）→ 与本库的关系（自动互链）→ 与其他知识的关联 → 待解答的问题 → 来源

## Entity 页面（Wiki/Entities/，type: entity）
- frontmatter: `title`（实体名）/ `entity_type`（people|company|tool|idea|theme）/ `created` / `updated` / `sources`（提及来源列表）
- 正文：是什么（一句话）→ 提及记录（每条：日期+来源+观点，自动累积）→ 相关实体（自动互链）

## Query 页面（Wiki/Queries/，type: query）
- frontmatter: `title`（问题）/ `asked`（日期）/ `type: query` / `sources`（答案依据）
- 正文：问题 → 答案（基于库内内容）→ 引用来源 → 备注

## Journal 页面（每日复盘）
- frontmatter: `title`（<日期> 每日复盘）/ `created` / `type: journal` / `tags` / `sources`（引用 Wiki 页）
- 正文：今日做了什么 → 今日新知（AI 从 Wiki 引用） → 📈 模式识别（近 30 天反复主题，≥3 次） → 明日计划 → 基于库内知识的建议

## CRM 页面（人脉笔记）
- frontmatter: `title`（联系人姓名）/ `created` / `updated` / `type: crm` / `tags` / `linked_entities`（关联实体页）
- 正文：背景（公司/职位/行业）→ 最近一次互动（日期/场合/聊了什么）→ 关注点 → 相关想法/事件/对话（连接万物）→ 下次跟进
