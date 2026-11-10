# 数据库规范

## 模型

- 表名使用复数的 `snake_case`，例如 `documents`。
- 每张表都有 `id`、`created_at`、`updated_at`；时间字段带时区。
- 主键：新业务表用 UUID（不可猜测）；`example_items` 保留自增整数，展示两种写法。选哪种由项目决定，不要在同一个模块里混用。路径里的整数 id 要有上界（超出数据库 `bigint` 范围会让驱动抛错），见 [api.md](api.md)。
- 多租户的业务表都有 `org_id`，查询通过统一的租户上下文过滤，不靠手动添加条件。

## 迁移

- 所有结构变化都通过 Alembic 迁移，不手动改数据库。
- 生成迁移后，人工检查内容，自动生成可能遗漏或多出操作。
- 合并前同步 `main`，用 `uv run alembic heads` 确认只有一个 head。出现多个 head 时，把自己未合并的迁移的 `down_revision` 改为 `main` 上最新的版本。
- 已发布的迁移不修改。
- 给已有数据的表加 `NOT NULL` 的外键或列，要分步：先加可空列，回填数据，再改为 `NOT NULL`。模板里的 `example_items.owner_id` 迁移直接清空了演示数据，那是因为它是示例表，真实项目不能这样做。
- Alembic 的 `env.py` 只依赖 `DatabaseSettings`（只有 `DATABASE_URL`），见 [structure.md](structure.md)。
- 破坏性变更分步发布：先扩展（新增字段），再迁移数据，再切换读取，最后单独发布收缩（删除旧字段）。
- 迁移要保证旧版本的代码也能在新的结构上运行，这样部署失败时可以回退代码。

## 查询

- 使用 SQLAlchemy 的参数化查询，不拼接 SQL 字符串。
- 列表查询都分页，避免一次加载全部数据。
- 注意 N+1 查询，需要时使用 `selectinload` 等预加载。
- 大表的变更先评估锁表时间。
