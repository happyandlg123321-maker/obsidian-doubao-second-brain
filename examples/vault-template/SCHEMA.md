# 页面结构 Schema（SCHEMA.md）

## Raw Sources 页面
- frontmatter: `source_url`（来源链接）/ `ingested`（日期）/ `content_type`（video/article/image）/ `lang`（zh-en 等）
- 正文：原始内容/双语逐字稿/提取结果，保留来源信息

## Wiki 页面
- frontmatter: `title` / `created` / `updated` / `type`（summary|concept）/ `tags` / `sources`（指向 Raw Sources）
- 正文：摘要 → 关键要点 → 与本库的关系 → 与其他知识的关联 → 待解答的问题 → 来源

## Journal 页面（每日复盘）
- frontmatter: `title`（<日期> 每日复盘）/ `created` / `type: journal` / `tags` / `sources`（引用 Wiki 页）
- 正文：今日做了什么 → 今日新知（AI 从 Wiki 引用） → 明日计划 → 基于库内知识的建议

## CRM 页面（人脉笔记）
- frontmatter: `title`（联系人姓名）/ `created` / `updated` / `type: crm` / `tags`
- 正文：背景（公司/职位/行业）→ 最近一次互动（日期/场合/聊了什么）→ 关注点 → 下次跟进
