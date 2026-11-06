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
- 接口变化后，更新 `@nestjs/swagger` 的装饰器，重新生成 OpenAPI 和 `packages/api-types`，一起提交。
- DTO 中用 `@Expose({ name: 'snake_case_name' })` 或全局序列化配置，保证 JSON 字段是 `snake_case`。
