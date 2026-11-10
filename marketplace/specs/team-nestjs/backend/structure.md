# 代码结构

```text
services/api/src/
├── main.ts
├── app.module.ts
├── config/          # 环境变量校验（Zod）
├── common/          # 错误过滤器、Guard、拦截器、装饰器
├── prisma/          # PrismaService
├── modules/
│   └── <模块名>/
│       ├── <模块名>.module.ts
│       ├── <模块名>.controller.ts   # 只处理请求、响应和参数校验
│       ├── <模块名>.service.ts      # 业务逻辑
│       └── dto/                     # 请求和响应 DTO
└── generated/prisma/  # Prisma 生成，不提交
```

## 分层规则

- `controller` 不写业务逻辑，不直接访问 `PrismaService`。
- `service` 写业务逻辑，通过 `PrismaService` 访问数据库。
- 请求和响应都使用 DTO，不直接返回 Prisma 模型。
- 模块之间通过导出的 service 调用，不直接查询别的模块的数据表。
- 配置统一通过 `ConfigService` 读取，不在业务代码中读取 `process.env`。

## 新增模块

1. 复制 `modules/example-items/` 的结构。
2. 在 `app.module.ts` 中导入模块。
3. 新增数据表时写 Prisma 迁移。
4. 补充 e2e 测试，包括权限和错误场景。

## 风格

- 开启 TypeScript 严格模式，不使用 `any`；确实需要时写明原因。
- 检查和格式用 Biome（全公司 TS 项目统一）。Biome 不覆盖依赖类型信息的规则，类型错误靠 `tsc --noEmit`，所以 `typecheck` 不能省。装饰器的解析配置在 NestJS 模板中验证。
- 全局 `ValidationPipe` 开启 `whitelist` 和 `forbidNonWhitelisted`。
- 外部调用都设置超时，并支持 `AbortSignal`。
- 不吞掉异常；需要转换时，抛出项目定义的业务异常，由全局过滤器转成统一的错误格式。
