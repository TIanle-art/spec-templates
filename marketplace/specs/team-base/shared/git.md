# Git 规范

## 分支

- 从最新的 `main` 创建，命名为 `<类型>/<Issue 编号>-<简短英文描述>`。
- 类型：`feat`、`fix`、`chore`、`docs`、`spike`、`hotfix`、`revert`。
- 示例：`feat/123-doc-upload`、`fix/456-token-refresh`。
- 分支存在超过 2 到 3 天，就同步一次 `main`。

## 提交

- 格式：`<类型>(<范围>): <说明>`，例如 `feat(auth): 支持短信验证码登录`。
- 一次提交只做一件事，说明写清楚为什么改。
- 按路径添加文件，不习惯性地 `git add .`，先用 `git status` 确认。

## PR

- 一个 PR 只解决一个问题，有效改动尽量不超过 400 行。
- 正文写明：改了什么、为什么改、如何验证、风险级别、请审查人注意的地方。
- 关联 Issue：功能和修复用 `Closes #编号`，需求文档用 `Refs #编号`。
- 统一使用 Squash Merge，PR 标题按提交格式书写。

## 禁止

- 推送或强推 `main`、`release/*`。
- 在共享分支上 rebase 或强推。
- 用 `git reset --hard` 加强推来“回滚”共享分支，回滚用 `git revert` 并走 PR。
- 用 `--no-verify` 跳过 Git hook，除非技术负责人同意并记录原因。

## 冲突

- 锁文件（`uv.lock`、`pnpm-lock.yaml`）和生成的文件不手工合并，同步后重新生成。
- rebase 时 `--ours` 是 `main` 的版本，`--theirs` 是你自己的提交，注意不要选反。
- 解决冲突后运行 `make check`，并由人检查结果。
