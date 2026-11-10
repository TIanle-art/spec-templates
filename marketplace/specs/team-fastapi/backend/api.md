# 接口规范

FastAPI 和 NestJS 后端遵守同一套约定，客户端不需要区分后端。

| 项目 | 约定 |
|---|---|
| 路径 | `/api/v1/<资源复数>`，例如 `/api/v1/documents` |
| 字段 | JSON 字段统一使用 `snake_case` |
| 时间 | ISO 8601，带时区；服务端存 UTC |
| 分页 | 请求 `page`、`page_size`；响应 `items`、`total`、`page`、`page_size` |
| 认证 | `Authorization: Bearer <访问令牌>` |
| 健康检查 | `/healthz`（进程存活）、`/readyz`（依赖可用） |
| `operationId` | `标签-函数名`，例如 `auth-login`、`example_items-create_item`，见下 |

## 错误格式

```json
{
  "error": {
    "code": "QUOTA_EXCEEDED",
    "message": "本月 AI 用量已达上限",
    "request_id": "req_123"
  }
}
```

- `code` 是稳定的错误码，给程序判断；`message` 给人看。
- 响应头带 `X-Request-ID`，日志使用同一个 ID。
- 不向客户端返回堆栈和内部错误。

## 规则

- 写操作都校验权限；跨组织访问返回 404。
- 支付、回调和重要的创建操作支持幂等。
- 已发布的接口不做破坏性修改。优先新增字段；不兼容的改动走新版本路径。
- 接口变化后，运行 `make openapi` 重新导出 `services/api/openapi.json` 并一起提交。`make openapi-check`（包含在 `make check` 里，CI 也会运行）检查它是不是最新的。
- 前端用 `@hey-api/openapi-ts` 根据这个文件生成 `packages/api-client`（SDK 和 TanStack Query 代码），不手写重复的类型和请求代码。
- 需要登录的接口用 `CurrentUser` 依赖；需要角色的用 `require_role`，见 [auth.md](auth.md)。
- 列表接口的 `page` 和路径里的 `id` 都要有上界（`Query(le=...)`、`Path(le=...)`）：超出数据库整数范围的值会让数据库驱动抛错，变成 500。

## operationId

客户端 SDK 的方法名由 `operationId` 决定，所以它是接口约定的一部分。

- 格式是 `标签-函数名`，每个接口都必须有标签。标签就是模块名，例如 `auth`、`users`、`example_items`。
- **标签不能含连字符**，多个单词用下划线（`example_items`，不是 `example-items`）。原因：生成 SDK 时按第一个连字符去掉标签前缀。URL 路径仍然用连字符（`/api/v1/example-items`），两者不冲突。
- 同一个标签下，函数名不能重复。
- 在 `main.py` 里用 `FastAPI(generate_unique_id_function=custom_generate_unique_id)` 实现，`tests/test_evals_and_openapi.py` 会检查唯一性、前缀和标签。
- 改函数名或标签，会改变生成的 SDK 方法名，属于接口变更，要通知客户端的负责人。
