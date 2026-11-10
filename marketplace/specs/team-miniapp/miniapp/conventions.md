# 开发规范

## 结构

```text
apps/miniapp/src/
├── app.config.ts
├── pages/          # 主包页面，尽量少
├── subpackages/    # 分包
├── features/
├── components/
├── services/       # request.ts、auth.ts、stream.ts
└── stores/
```

## 规则

- 主包只放启动必需的页面，其他页面放分包，从一开始控制包体积。
- 所有接口都通过 `services/request.ts`，它负责令牌、刷新和统一的错误处理。
- 接口 SDK 和类型从 `packages/api-client` 引入（`@hey-api/openapi-ts` 生成），不手写重复的类型。**注意：** 小程序里没有浏览器的 `XMLHttpRequest` 和 `fetch`，请求要通过 `Taro.request`（或 `wx.request`）发出，所以 openapi-ts 默认的 axios 或 fetch 客户端很可能不能直接用，需要自定义客户端或适配器，并保持令牌、刷新和统一错误处理仍然走 `services/request.ts`。在小程序模板中验证。
- 登录时只把 code 发给后端；`session_key` 只保存在服务端。
- 支付金额由后端决定，前端不传金额。
- 不在小程序代码中放任何密钥。
- 用户隐私授权按微信的要求处理，未授权时提供可用的替代流程。

## 检查和测试

- 检查和格式用 Biome（全公司统一），类型错误靠 `tsc --noEmit`。Biome 不覆盖依赖类型信息的规则。
- Taro 脚手架自带的 ESLint 配置里有 Taro 专用的规则，换成 Biome 后会丢失哪些，在小程序模板中验证，结论写进模板的 ADR。**验证之前不要直接删掉 Taro 自带的 ESLint 配置。**
- 单元测试用 Vitest。

## AI 流式输出

小程序不能直接使用网页的 SSE 代码。具体做法以微信官方文档和真机测试为准，必须在 iOS 和 Android 真机上验证。

## 兼容旧版本

用户可能长期使用旧版小程序。后端接口保持兼容，新功能不要求所有用户立即更新。
