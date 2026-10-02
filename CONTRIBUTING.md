# 贡献指南（CONTRIBUTING）

感谢你考虑为 **obsidian-doubao-second-brain** 做贡献！本项目是个人知识管理工具，小而美优先。

## 项目结构

```
SKILL.md                  # Skill 定义（豆包工作读取的入口）
scripts/init_vault.py     # 知识库骨架初始化脚本
docs/                     # 架构 / SOP / 方案对比
examples/vault-template/  # 知识库模板
README.md                 # 用户入口文档
```

## 贡献方式

### 报告问题（Issues）
- 描述：环境（豆包工作桌面版/云电脑）、预期行为、实际行为、报错原文
- 视频转写问题请附：平台（B站/YouTube）、是否付费试看、飞书妙记返回信息

### 提交代码（PR）
1. Fork 本仓库，从 `main` 开分支：`git checkout -b fix/xxx`
2. 改动聚焦单一问题，保持与现有风格一致（中文注释、纯标准库优先）
3. 脚本类改动必须自带验证方式（如 `init_vault.py --demo` 的幂等测试）
4. 更新 `CHANGELOG.md`（Unreleased 段落）
5. 提交信息用 Conventional Commits：`feat:` / `fix:` / `docs:` / `refactor:`

## 代码约定

- `scripts/` 只用 Python 标准库，不引入第三方依赖
- 中文注释；文件编码 UTF-8
- 不把任何私有提示词、内部资料、个人信息提交进仓库
- 保持幂等：重复运行不破坏已有数据

## 行为准则

- 尊重用户知识主权：内容入库前由用户确认
- 不编造转写结果；受限内容如实标注
- 隐私内容（证照/密码/家庭住址/资产）拒绝入库、拒绝入库代码示例
