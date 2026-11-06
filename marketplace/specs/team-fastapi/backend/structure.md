# 代码结构

```text
services/api/app/
├── main.py
├── core/          # 配置、安全、日志、统一错误
├── db/            # 数据库会话和基类
├── modules/
│   └── <模块名>/
│       ├── router.py    # 路由：只处理请求、响应和依赖注入
│       ├── schemas.py   # 请求和响应模型（Pydantic）
│       ├── service.py   # 业务逻辑
│       └── models.py    # 数据库模型（SQLAlchemy）
└── workers/       # 后台任务
```

## 分层规则

- `router` 不写业务逻辑，不直接操作数据库。
- `service` 写业务逻辑，接收和返回 schema 或领域对象。
- `models` 和 `schemas` 不混用，接口不直接返回数据库模型。
- 模块之间通过对方的 `service` 调用，不直接查询别的模块的数据表。
- 配置统一从 `core/config.py` 读取，不在业务代码中读取环境变量。

## 新增模块

1. 复制 `modules/example_items/` 的结构。
2. 在 `main.py` 中注册路由。
3. 新增数据表时写 Alembic 迁移。
4. 补充接口测试，包括权限和错误场景。

## 风格

- 所有函数都写类型注解，`pyright` 不报错。
- 外部调用（模型 API、微信接口、HTTP 请求）都设置超时。
- 不吞掉异常；需要转换时，转成 `core/errors.py` 中定义的业务错误。
