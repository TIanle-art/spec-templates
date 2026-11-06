# 后端规范（FastAPI）

技术栈：Python、FastAPI、Pydantic、SQLAlchemy 2（异步）、Alembic、PostgreSQL、uv。

| 文件 | 什么时候读 |
|---|---|
| [structure.md](structure.md) | 新增模块、决定代码放在哪里时 |
| [api.md](api.md) | 新增或修改接口时 |
| [database.md](database.md) | 修改数据模型、写查询、写迁移时 |
| [ai-gateway.md](ai-gateway.md) | 调用模型、处理流式输出、写评估时 |
| [testing.md](testing.md) | 写后端测试时 |

## 常用命令

```bash
uv sync
uv run fastapi dev app/main.py
uv run alembic revision --autogenerate -m "<说明>"
uv run alembic upgrade head
uv run ruff check . && uv run ruff format --check .
uv run pyright
uv run pytest
```

正确示例：`services/api/app/modules/example_items/`。
