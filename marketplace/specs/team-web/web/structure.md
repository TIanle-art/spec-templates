# 代码结构

```text
apps/web/src/
├── app/           # 路由、Provider、全局布局
├── features/      # 按业务功能组织
│   └── <功能名>/
│       ├── components/
│       ├── hooks/
│       ├── api.ts      # 本功能的接口调用
│       └── index.ts    # 对外导出
├── components/    # 通用组件
│   └── ui/        # shadcn/ui 组件
├── lib/           # 请求客户端的配置（令牌、刷新、错误）、工具函数
└── styles/        # 设计变量
```

## 规则

- 业务代码放在 `features/` 下，一个功能一个目录。
- 一个功能只在两个以上的地方使用时，才提取到 `components/` 或 `lib/`。
- 功能之间通过 `index.ts` 导出的内容引用，不直接引用别的功能的内部文件。
- 接口 SDK 和类型从 `packages/api-client` 引入（`@hey-api/openapi-ts` 根据后端提交的 `openapi.json` 生成），不手写重复的类型和请求代码，不手改生成的文件。
- 开启 TypeScript 严格模式，不使用 `any`。
