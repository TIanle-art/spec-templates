# 本地数据规范

## 数据库

- 数据库文件放在 `app.getPath("userData")`。
- 使用 Drizzle 定义结构，迁移文件随应用打包，启动时自动执行。
- 执行迁移前自动备份数据库文件。
- 已发布的迁移不修改。
- 提供数据导出和恢复功能。

## 敏感信息

- 登录令牌用 `safeStorage` 加密保存，普通设置用 electron-store。
- Linux 上没有系统密钥环时，`safeStorage` 的保护很弱。启动时检查 `safeStorage.getSelectedStorageBackend()`，返回 `basic_text` 时提示用户，或缩短令牌有效期。
- 不在本地保存公司的 API Key。

## 原生模块

- better-sqlite3 是原生模块，要按 Electron 版本、各平台和架构分别编译。
- `package.json` 的 `postinstall` 运行 `electron-builder install-app-deps`。
- 打包时把 better-sqlite3 从 asar 中解包。

## 离线

- 已授权的用户在断网时仍能使用本地功能。
- 离线超过约定时间（默认 7 天）后要求联网验证，但用户仍能导出数据。
- 没有网络时，AI 功能给出明确的提示。

## 上报

只上报版本、功能使用次数和错误信息，不上传用户的文件和输入内容。上报范围要告知用户。
