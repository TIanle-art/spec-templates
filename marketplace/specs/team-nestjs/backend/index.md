# 后端规范（NestJS）

技术栈：TypeScript、NestJS、Prisma（锁定 7.x）、PostgreSQL、pnpm。

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
pnpm lint
pnpm typecheck        # package.json 中定义为 tsc --noEmit；CI 只运行名为 typecheck 的脚本
pnpm test
pnpm test:e2e
```

正确示例：`services/api/src/modules/example-items/`。
