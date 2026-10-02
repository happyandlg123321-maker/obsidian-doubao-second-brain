# 发布到 GitHub 操作清单（RELEASE.md）

> 本 Skill 已在本地完成：文件齐全、脚本验证通过、git 仓库已初始化并首次提交。
> 发布是**外部公开动作**，请确认以下事项后自行选择一种方式执行。

## 发布前检查

- [ ] GitHub 账号已注册（https://github.com）
- [ ] 仓库内容确认公开（README/SKILL/docs/scripts/examples，不含任何私有提示词或内部资料）
- [ ] 仓库名：`obsidian-doubao-second-brain`（可自定）

## 方式 A：自己执行（推荐，token 不经过 AI）

在**你的终端**逐条执行：

```bash
# 1. 进入项目目录
cd /path/to/obsidian-doubao-second-brain

# 2. 登录 GitHub（浏览器授权，不泄露 token）
gh auth login

# 3. 创建公开仓库
gh repo create obsidian-doubao-second-brain --public --source=. --push
```

或不用 gh CLI，用 HTTPS + 令牌：

```bash
cd /path/to/obsidian-doubao-second-brain
git remote add origin https://github.com/<你的用户名>/obsidian-doubao-second-brain.git
git push -u origin main
# 首次 push 会提示输入 GitHub 用户名和 Personal Access Token（勾选 repo 权限）
```

## 方式 B：授权 AI 代推

1. 在你的终端运行 `gh auth login` 完成浏览器授权
2. 回到豆包对话告诉我「已登录 gh，可以推送」
3. 我会执行：`gh repo create obsidian-doubao-second-brain --public --source=. --push`

## 发布后建议

- 到仓库 Settings 添加描述和 Topics（`obsidian`、`second-brain`、`豆包`、`llm-wiki`）
- 如后续更新：`git add -A && git commit -m "..." && git push`
- 仓库文件被他人下载后：参照 README「快速开始」安装 Skill 并初始化知识库
