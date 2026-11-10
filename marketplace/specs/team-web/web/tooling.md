# 工具链和测试

全公司的 TypeScript 项目（网页、NestJS、小程序、桌面）使用同一套工具，不让每个模板各用一套。

## 检查和格式：Biome

- `pnpm lint` 运行 Biome（检查和格式、导入排序）。CI 只运行项目的 `lint` 脚本，用什么工具由项目决定，公司统一用 Biome。
- Biome 不覆盖依赖类型信息的规则（typescript-eslint 的类型感知规则），类型错误靠 `pnpm typecheck`（`tsc --noEmit`），两者都要通过。
- 生成的代码（`packages/api-client`、路由生成文件、`components/ui/`）在 Biome 配置里排除，不手改。

## 接口 SDK：@hey-api/openapi-ts

1. 后端 `make openapi` 导出 `services/api/openapi.json` 并提交。
2. `@hey-api/openapi-ts` 读取它，生成 `packages/api-client`：接口 SDK 和 TanStack Query 代码。生成命令写进 `packages/api-client` 的脚本，生成结果提交到仓库。
3. CI 重新生成一遍并与提交的代码比对，不一致时失败（这一项还没有做，在网页模板中加入）。
4. 方法名来自 `operationId`（`标签-函数名`），见后端规范的 `api.md`。

## 测试

- **Vitest + Testing Library：** 单元测试和组件测试，放在源文件旁边。覆盖逻辑、表单校验、加载/空/错误/无权限四种状态。
- **Playwright：** 端到端冒烟，覆盖登录和主要业务流程，脚本名 `test:e2e`。CI 通过 `node-ci.yml` 的 `e2e-script` 运行，会先安装浏览器。不依赖真实的第三方服务：AI 和支付用后端的模拟服务商或测试模式。
- 不删除、跳过或放宽测试来通过检查，见 `shared/testing.md`。
