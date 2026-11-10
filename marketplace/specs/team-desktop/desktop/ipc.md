# 进程通信规范

## 结构

```text
apps/desktop/src/
├── main/       # 主进程：ipc/、services/、db/
├── preload/    # 只暴露必要的函数
├── renderer/   # React 界面
└── shared/     # ipc-contract.ts：IPC 参数定义
```

## 规则

- 开启 `contextIsolation` 和进程沙箱，渲染进程不开启 Node 集成。
- preload 只暴露具体的函数，不暴露原始的 `ipcRenderer`。
- 每个 IPC 通道在 `shared/ipc-contract.ts` 中用 Zod 定义参数，主进程收到后先校验。
- 检查消息来源，只处理来自本应用页面的请求。
- 文件路径只能在允许的目录内，拒绝 `..` 和绝对路径的越界访问。
- 渲染进程不直接访问数据库和文件系统。
- 不把不可信的内容传给 `shell.openExternal`，限制页面跳转和新窗口。
- 通道命名为 `<模块>:<动作>`，例如 `notes:create`。
