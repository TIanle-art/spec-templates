# 代码结构

```text
services/api/app/
├── main.py
├── cli.py         # 命令行：create-admin
├── core/          # 配置、日志（structlog）、request_id、统一错误、分页、安全、限流、共用依赖
├── db/            # 数据库会话和基类
├── modules/
│   └── <模块名>/
│       ├── router.py    # 路由：只处理请求、响应和依赖注入
│       ├── schemas.py   # 请求和响应模型（Pydantic）
│       ├── service.py   # 业务逻辑
│       └── models.py    # 数据库模型（SQLAlchemy）
└── workers/       # 后台任务（有耗时任务时再加）
```

## 分层规则

- `router` 不写业务逻辑，不直接操作数据库。
- `service` 写业务逻辑，接收和返回 schema 或领域对象。
- `models` 和 `schemas` 不混用，接口不直接返回数据库模型。
- 模块之间通过对方的 `service` 调用，不直接查询别的模块的数据表。
- 配置统一从 `core/config.py` 读取，不在业务代码中读取环境变量。
- **配置拆成两层：** `DatabaseSettings` 只有 `DATABASE_URL`，`Settings` 继承它并增加其余配置。Alembic 的 `env.py` 只实例化 `DatabaseSettings`：CI 的迁移检查只提供 `DATABASE_URL`，不能因为缺少 `SECRET_KEY` 等应用配置而失败。新增必填配置放进 `Settings`，不要放进 `DatabaseSettings`。
- 必填配置没有默认值，缺少时启动直接报错退出。生产环境（`APP_ENV=production`）额外校验：`SECRET_KEY` 至少 32 个字符且不是占位符，数据库口令不能是默认口令，`CORS_ORIGINS` 不能是 `*`。这些校验不能为了让测试通过而放宽，测试里设置测试用的值即可。
- 日志用 structlog：`structlog.get_logger(__name__)`，字段用关键字参数，例如 `logger.info("ai_call", feature="chat")`；不要把密码、令牌和用户输入写进日志。每条日志自动带 `request_id`。
- 数据库驱动是 asyncpg：`.env` 和 CI 里写 `postgresql://`，配置代码转成 `postgresql+asyncpg://`。
## 新增模块

1. 复制 `modules/example_items/` 的结构。
2. 在 `main.py` 的 `API_ROUTERS` 中注册路由；路由的 `tags` 用模块名，不含连字符（见 [api.md](api.md) 的 operationId）。
3. 在 `alembic/env.py` 中导入它的 `models`，新增数据表时写 Alembic 迁移。
4. 补充接口测试，包括未登录、无权限、访问别人的数据和错误场景。
5. 接口有变化时运行 `make openapi`，提交 `openapi.json`。

## 风格

- 所有函数都写类型注解，`pyright` 不报错。
- 外部调用（模型 API、微信接口、HTTP 请求）都设置超时。
- 不吞掉异常；需要转换时，转成 `core/errors.py` 中定义的业务错误。
