# 打包和发布规范

## 只打包运行时需要的内容

不能进入安装包：`src/`、测试、`docs/`、`openspec/`、`.trellis/`、`.agents/`、`.claude/`、`AGENTS.md`、`CLAUDE.md`、`.github/`、`.env`、密钥和证书、Source Map。

打包后运行 `scripts/check-package.sh <app.asar 路径>` 检查。Source Map 上传到错误监控平台。

## 三个平台

| 平台 | 安装包 | 签名 |
|---|---|---|
| Windows | NSIS | OV 证书，私钥在硬件令牌或云端 HSM |
| macOS | DMG，另需 ZIP 供自动更新 | Developer ID 签名 + 公证；不签名就不能自动更新 |
| Linux | AppImage，按需加 DEB | 发布页提供 SHA256 校验值 |

- 每个平台都在对应的系统上构建。
- 签名凭据不放进 GitHub，在维护者的设备上签名。

## Electron Fuses

打包配置中关闭 `runAsNode`、`enableNodeOptionsEnvironmentVariable`、`enableNodeCliInspectArguments`，开启 `enableEmbeddedAsarIntegrityValidation` 和 `onlyLoadAppFromAsar`。打包后用 `npx @electron/fuses read --app <应用路径>` 确认。

## 发布前在干净的机器上逐个平台验证

- 首次安装和启动
- 从上一个版本覆盖升级，本地数据迁移成功
- 自动更新和更新失败后的重试
- 卸载
- 断网时的行为
- 崩溃日志能否上报

## 发布

- 先灰度（例如 5%、20%、50%），观察崩溃和错误后再全量。
- 有问题的版本立即停止推送，通过发布更高版本的修复包来回滚。
- 后端要兼容旧版本的客户端。
