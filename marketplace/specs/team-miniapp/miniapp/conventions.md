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
- 接口类型从 `packages/api-types` 引入。
- 登录时只把 code 发给后端；`session_key` 只保存在服务端。
- 支付金额由后端决定，前端不传金额。
- 不在小程序代码中放任何密钥。
- 用户隐私授权按微信的要求处理，未授权时提供可用的替代流程。

## AI 流式输出

小程序不能直接使用网页的 SSE 代码。具体做法以微信官方文档和真机测试为准，必须在 iOS 和 Android 真机上验证。

## 兼容旧版本

用户可能长期使用旧版小程序。后端接口保持兼容，新功能不要求所有用户立即更新。
