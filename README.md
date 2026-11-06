# spec-templates

公司的 Trellis 团队规范模板。新项目用 `trellis init` 从这里安装规范到 `.trellis/spec/`，AI 在写代码前读取这些规范。

规范的总体说明见 handbook 仓库的《公司项目脚手架规范》6.4 节。

## 模板列表

- `team-base`：所有项目必装。Git、测试、安全、AI 使用、开始写代码前的检查、完成标准、卡住时怎么办
- `team-fastapi`：FastAPI 后端（Python、SQLAlchemy 2、Alembic、PostgreSQL）
- `team-nestjs`：NestJS 后端（TypeScript、Prisma、PostgreSQL）
- `team-web`：网页前端（React、TypeScript、Vite、Tailwind CSS、shadcn/ui、TanStack Query）
- `team-miniapp`：微信小程序（Taro 4）
- `team-desktop`：桌面软件（Electron、SQLite、Drizzle，Windows、macOS、Linux）

模板清单在 `marketplace/index.json`，内容在 `marketplace/specs/<模板 id>/`。

## 使用方法

本仓库是私有仓库。安装前，本机的 git 要能访问它（已登录 GitHub 即可）；也可以设置环境变量 `GIGET_AUTH` 为有读取权限的 GitHub token。

先安装公共规范，再按项目追加技术栈规范：

```bash
# 1. 公共规范（所有项目）
trellis init --claude --cursor --codex \
  --registry gh:TIanle-art/spec-templates/marketplace --template team-base

# 2. 按项目追加，例如 FastAPI + 网页
trellis init --registry gh:TIanle-art/spec-templates/marketplace --template team-fastapi --append
trellis init --registry gh:TIanle-art/spec-templates/marketplace --template team-web --append
```

`--claude --cursor --codex` 按团队成员实际使用的工具选择，可用的还有 `--copilot`、`--opencode`、`--kimi`，以 `trellis init --help` 为准。

安装后：

1. 检查 `.trellis/spec/` 中的文件，把项目特有的内容补进去。
2. 检查 Trellis 生成的 `AGENTS.md`，把 handbook 中 `project-kit/AGENTS.md` 的公司规则合并进去。
3. 提交 `.trellis/` 和相关文件，提 PR。

## 固定版本

默认安装 `main` 分支的最新内容。需要固定版本时，在仓库路径后加标签，例如：

```bash
trellis init --registry gh:TIanle-art/spec-templates/marketplace#v1 --template team-base
```

模板有较大变动时打新的标签（`v1`、`v2`……），并在团队频道说明变化。已有项目不会自动更新，需要时由技术负责人对比后手动合并。

## 新增或修改模板

1. 从 `main` 建分支。
2. 新增模板时，在 `marketplace/specs/` 下建目录，并在 `marketplace/index.json` 中加一条记录：`id` 与目录名相同，`type` 为 `spec`，`path` 从仓库根目录写起。
3. 模板目录中直接放规范文件，例如 `backend/index.md`，不要再套一层 `spec/`。
4. 运行检查：

   ```bash
   python3 scripts/validate.py
   ```

   它会检查 `index.json` 的格式、模板目录是否存在，以及文档中的相对链接是否有效。PR 中 CI 也会运行同样的检查。

5. 在一个临时仓库中实际运行一次 `trellis init` 确认能安装，再提 PR。
6. 规范内容的改动由模板负责人审查。

## 写规范的原则

- 写具体的规则和例子，不写空泛的原则。
- 每条规则 AI 都能照着执行，也能在审查时检查。
- 与 handbook 中两份规范保持一致；有冲突时以 handbook 为准，并同时修正这里。
- 不写客户信息、内网地址、密钥。
