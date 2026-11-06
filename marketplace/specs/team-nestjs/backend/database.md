# 数据库规范

## 模型

- 表名使用复数的 `snake_case`，通过 `@@map` 映射；字段在 Prisma 中可以用 camelCase，用 `@map` 映射到 `snake_case` 列名。
- 每张表都有 `id`、`created_at`、`updated_at`；时间字段带时区。
- 多租户的业务表都有 `org_id`，查询通过统一的租户上下文过滤，不靠手动添加条件。

## Prisma 版本

- `prisma` 和 `@prisma/client` 锁定在同一个大版本（7.x），安装时明确写版本号。
- 生成的客户端不提交，CI 和全新克隆后先运行 `pnpm prisma generate`。

## 迁移

- 所有结构变化都通过 `prisma migrate dev` 生成迁移，不手动改数据库。
- 生成后人工检查 SQL。
- 已发布的迁移不修改。同步 `main` 后迁移冲突时，删除自己未合并的迁移目录，重新生成。
- 测试和生产环境使用 `prisma migrate deploy`，在部署时单独执行，不在应用启动时执行。
- 破坏性变更分步发布：先扩展，再迁移数据，再切换读取，最后单独发布收缩。
- 迁移要保证旧版本的代码也能在新的结构上运行。

## 查询

- 不使用 `$queryRawUnsafe` 拼接用户输入；需要原生 SQL 时使用参数化的 `$queryRaw`。
- 列表查询都分页。
- 用 `select` 或 `include` 只取需要的字段，注意 N+1 查询。
