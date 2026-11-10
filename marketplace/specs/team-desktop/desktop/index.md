# 桌面软件规范

技术栈：Electron、electron-vite、React、TypeScript、SQLite、better-sqlite3、Drizzle。支持 Windows、macOS 和 Linux。工具链（全公司 TS 项目统一）：Biome（检查和格式，类型错误靠 `tsc --noEmit`）、Vitest（单元测试）、Playwright（端到端冒烟）、`@hey-api/openapi-ts`（有云端接口时生成 `packages/api-client`）。

| 文件 | 什么时候读 |
|---|---|
| [ipc.md](ipc.md) | 主进程和界面之间通信时 |
| [local-data.md](local-data.md) | 读写本地数据库、文件和敏感信息时 |
| [packaging.md](packaging.md) | 打包、签名、更新和发布时 |

## 核心原则

凡是不能让用户自己说了算的，都由服务器判定。Electron 的代码可以被解包查看和修改，所以：

- 本地的权限判断只用来控制界面。
- 会员、授权和付费额度由服务器决定。
- 公司的 API Key 不进入客户端。
- 需要保密的核心算法放在服务器上。
