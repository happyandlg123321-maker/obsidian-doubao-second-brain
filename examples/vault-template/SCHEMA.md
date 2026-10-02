# 页面结构 Schema（SCHEMA.md）

## Raw Sources 页面
- frontmatter: `source_url`（来源链接）/ `ingested`（日期）/ `content_type`（video/article/image）/ `lang`（zh-en 等）
- 正文：原始内容/双语逐字稿/提取结果，保留来源信息

## Wiki 页面
- frontmatter: `title` / `created` / `updated` / `type`（summary|concept）/ `tags` / `sources`（指向 Raw Sources）
- 正文：摘要 → 关键要点 → 与本库的关系 → 与其他知识的关联 → 待解答的问题 → 来源
