# 后端规范（NestJS）

技术栈：TypeScript、NestJS、Prisma（锁定 7.x）、PostgreSQL、pnpm；检查和格式用 Biome，测试用 Vitest + Supertest，接口契约用 `openapi.json` + `@hey-api/openapi-ts`（全公司 TS 项目统一）。

> NestJS 模板还没有建。下面标明“在模板中验证”的地方，以模板的验证结果为准：Vitest 对装饰器元数据的支持、Biome 对装饰器的解析、`operationIdFactory` 的写法。

| 文件 | 什么时候读 |
|---|---|
| [structure.md](structure.md) | 新增模块、决定代码放在哪里时 |
| [api.md](api.md) | 新增或修改接口时 |
| [database.md](database.md) | 修改数据模型、写查询、写迁移时 |
| [ai-gateway.md](ai-gateway.md) | 调用模型、处理流式输出、写评估时 |
| [testing.md](testing.md) | 写后端测试时 |

## 常用命令

```bash
pnpm install
pnpm prisma generate
pnpm start:dev
pnpm prisma migrate dev --name <说明>
pnpm lint             # Biome（检查和格式）
pnpm typecheck        # package.json 中定义为 tsc --noEmit；CI 只运行名为 typecheck 的脚本
pnpm test             # Vitest
pnpm test:e2e
```

命令名称和《公司项目脚手架规范》6.2 保持一致（`make setup`、`make check`、`make openapi`、`make openapi-check` 等），`make` 目标调用上面的 `pnpm` 脚本。

正确示例：`services/api/src/modules/example-items/`。
