# 后端规范（FastAPI）

技术栈：Python、FastAPI、Pydantic、SQLAlchemy 2（异步，asyncpg）、Alembic、PostgreSQL、structlog、pwdlib（Argon2id）、PyJWT、uv。

| 文件 | 什么时候读 |
|---|---|
| [structure.md](structure.md) | 新增模块、决定代码放在哪里时 |
| [api.md](api.md) | 新增或修改接口时（含 `operationId` 约定和 `openapi.json`） |
| [auth.md](auth.md) | 登录、令牌、角色权限、限流 |
| [database.md](database.md) | 修改数据模型、写查询、写迁移时 |
| [ai-gateway.md](ai-gateway.md) | 调用模型、处理流式输出、写评估时 |
| [testing.md](testing.md) | 写后端测试时 |

## 常用命令

```bash
make setup                                # 安装依赖，启用 Git hook，生成 .env
make dev                                  # 数据库 + 迁移 + API
make check                                # lint、类型检查、openapi-check、测试、Skill 一致性
make openapi                              # 改了接口之后，导出并提交 openapi.json
make create-admin EMAIL=<邮箱>            # 创建管理员
uv sync
uv run fastapi dev app/main.py
uv run alembic revision --autogenerate -m "<说明>"
uv run alembic upgrade head
uv run ruff check . && uv run ruff format --check .
uv run pyright
uv run pytest
```

正确示例：`services/api/app/modules/example_items/`（含权限）、`auth/`、`users/`。
