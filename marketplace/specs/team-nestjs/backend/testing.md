# 后端测试

> 工具选择在 NestJS 模板中验证，下面以模板的验证结果为准。

- **测试框架：Vitest。** NestJS 依赖装饰器元数据（`emitDecoratorMetadata`），Vitest 默认的 esbuild 不保留它，需要用 SWC 插件。能跑通就统一用 Vitest；跑不通时保留 Jest，并在模板的 `docs/adr/` 写一条 ADR 说明原因（全公司 TS 项目统一 Vitest 是目标，不是不能例外）。
- 单元测试与源文件放在一起，命名为 `*.spec.ts`。
- 接口测试使用 Vitest（或 Jest）+ Supertest，放在 `test/`，命名为 `*.e2e-spec.ts`；覆盖正常、错误、未登录、无权限和跨组织访问。
- 需要数据库的测试使用独立的测试数据库，每个测试的数据互不影响。
- CI 只提供 `DATABASE_URL` 和 `APP_ENV=test`：测试需要的其他配置在测试的初始化代码里设置测试值，不要为了让测试通过而放宽生产环境的配置校验。
- 外部服务（模型 API、微信、对象存储）在测试中使用模拟实现，通过 Nest 的依赖注入替换。
- 后台任务的测试覆盖成功、失败和重试，确认具有幂等性。
- AI 功能除了单元测试，还要运行 `evals/` 中的评估。
- 检查和格式用 Biome。Biome 不覆盖依赖类型信息的规则，类型错误靠 `pnpm typecheck`（`tsc --noEmit`）。
