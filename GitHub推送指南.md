# GitHub 推送完整指南

> 如何将 SimCLR 项目推送到 GitHub

---

## 🎯 快速推送（3种方法）

### 方法 1: 使用自动脚本（最简单）⭐

```powershell
.\push_to_github.bat
```

这个脚本会自动完成所有步骤。

---

### 方法 2: 手动推送（推荐理解每一步）

#### 步骤 1: 添加文件到暂存区

```powershell
# 添加所有文件
git add .

# 或选择性添加
git add *.py *.bat *.md
```

#### 步骤 2: 提交更改

```powershell
git commit -m "Update SimCLR with Chinese docs and Windows optimization"
```

#### 步骤 3: 推送到 GitHub

```powershell
git push origin master
```

---

### 方法 3: 一条命令推送

```powershell
git add . ; git commit -m "Update project" ; git push origin master
```

---

## 🆕 首次推送到新仓库

### 步骤 1: 在 GitHub 创建新仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `simclr-pytorch` 或你喜欢的名字
   - **Description**: `SimCLR self-supervised learning with Chinese docs`
   - **Public** 或 **Private**: 根据需要选择
   - ⚠️ **不要**勾选 "Initialize this repository with a README"

3. 点击 "Create repository"

### 步骤 2: 连接本地仓库到 GitHub

GitHub 会显示快速设置指南。由于你已经有本地仓库，选择 "push an existing repository"：

```powershell
# 如果需要更改远程仓库地址
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 或者添加新的远程仓库
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送到主分支
git push -u origin master
```

### 步骤 3: 验证推送

访问你的 GitHub 仓库页面，应该能看到所有文件。

---

## 🔐 身份验证

### GitHub 不再支持密码验证

从 2021年8月13日起，GitHub 要求使用 **Personal Access Token (PAT)** 或 **SSH Key**。

### 方法 A: 使用 Personal Access Token（推荐）

#### 1. 生成 Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 设置：
   - **Note**: `SimCLR Project`
   - **Expiration**: 选择有效期
   - **Scopes**: 勾选 `repo`（完整仓库访问权限）
4. 点击 "Generate token"
5. ⚠️ **立即复制 token**（只显示一次！）

#### 2. 使用 Token 推送

```powershell
# 第一次推送时会要求输入用户名和密码
git push origin master

# 输入：
# Username: YOUR_GITHUB_USERNAME
# Password: YOUR_PERSONAL_ACCESS_TOKEN (粘贴刚才复制的 token)
```

#### 3. 保存凭据（可选，避免每次输入）

```powershell
# 使用凭据管理器保存
git config --global credential.helper wincred
```

---

### 方法 B: 使用 SSH Key

#### 1. 生成 SSH Key

```powershell
# 生成新的 SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# 按 Enter 使用默认位置
# 可选：输入密码短语（或直接 Enter 跳过）
```

#### 2. 添加 SSH Key 到 GitHub

```powershell
# 复制公钥到剪贴板
Get-Content ~/.ssh/id_ed25519.pub | clip
```

然后：
1. 访问 https://github.com/settings/keys
2. 点击 "New SSH key"
3. 粘贴公钥
4. 点击 "Add SSH key"

#### 3. 更改远程 URL 为 SSH

```powershell
git remote set-url origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
```

#### 4. 推送

```powershell
git push origin master
```

---

## 📋 推送前检查清单

### 必须检查的项目

- [ ] `.gitignore` 文件已创建（排除大文件和敏感信息）
- [ ] 训练数据和模型文件已排除（在 `.gitignore` 中）
- [ ] 没有包含敏感信息（密码、API密钥等）
- [ ] 所有重要文件都已添加

### 可选检查

- [ ] README 文件完整
- [ ] 许可证文件存在
- [ ] 文档齐全

---

## 🗂️ 应该推送的文件

### ✅ 推送这些文件

```
✓ 所有 .py 源代码文件
✓ 所有 .bat 批处理文件
✓ 所有 .md 文档文件
✓ requirements.txt
✓ env.yml
✓ .gitignore
✓ LICENSE.txt
```

### ❌ 不要推送这些

```
✗ __pycache__/ (Python 缓存)
✗ datasets/ (数据集，太大)
✗ runs/ (训练结果，太大)
✗ *.pth, *.pth.tar (模型文件，太大)
✗ .vscode/, .idea/ (IDE 配置)
```

已在 `.gitignore` 中排除。

---

## 🔧 常见问题解决

### Q1: 推送被拒绝 (rejected)

```
! [rejected] master -> master (fetch first)
```

**原因**: 远程仓库有本地没有的提交。

**解决**:
```powershell
# 拉取远程更改
git pull origin master --rebase

# 然后再推送
git push origin master
```

---

### Q2: 文件太大无法推送

```
remote: error: File xxx is 100.00 MB; this exceeds GitHub's file size limit of 100.00 MB
```

**解决**:
```powershell
# 1. 从暂存区移除大文件
git rm --cached path/to/large/file

# 2. 添加到 .gitignore
echo "path/to/large/file" >> .gitignore

# 3. 重新提交
git commit --amend -m "Remove large files"

# 4. 强制推送（谨慎使用）
git push origin master --force
```

---

### Q3: 身份验证失败

```
remote: Support for password authentication was removed
```

**解决**: 使用 Personal Access Token 或 SSH Key（见上文）。

---

### Q4: 忘记 .gitignore，已经提交了大文件

```powershell
# 从 git 历史中完全删除大文件
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file" \
  --prune-empty --tag-name-filter cat -- --all

# 强制推送
git push origin --force --all
```

⚠️ **警告**: 这会重写历史，谨慎使用！

---

### Q5: 推送很慢

**优化方法**:
```powershell
# 使用浅克隆（仅推送最新更改）
git push origin master --depth 1

# 或增加缓冲区大小
git config --global http.postBuffer 524288000
```

---

## 📊 推送后验证

### 1. 检查 GitHub 仓库

访问你的仓库：`https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`

应该能看到：
- ✅ 所有源代码文件
- ✅ 文档文件（README_CN.md, 完整使用指南.md 等）
- ✅ 批处理脚本
- ✅ 最新的提交信息

### 2. 克隆测试（可选）

```powershell
# 在其他目录测试克隆
cd D:\test
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 检查文件是否完整
ls
```

---

## 🎨 美化你的 GitHub 仓库

### 1. 添加 README 徽章

在 `README_CN.md` 顶部添加：

```markdown
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 1.4+](https://img.shields.io/badge/pytorch-1.4+-orange.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/YOUR_REPO_NAME.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/stargazers)
```

### 2. 添加主题标签

在 GitHub 仓库页面：
- 点击 "About" 旁边的齿轮图标
- 添加主题：`deep-learning`, `pytorch`, `simclr`, `self-supervised-learning`, `computer-vision`

### 3. 设置仓库描述

在 "About" 中添加：
```
SimCLR 自监督学习框架 | PyTorch 实现 | 完整中文文档 | Windows 优化
```

---

## 📝 推送命令速查表

```powershell
# === 查看状态 ===
git status                          # 查看当前状态
git log --oneline                   # 查看提交历史

# === 添加文件 ===
git add .                           # 添加所有文件
git add *.py                        # 只添加 Python 文件

# === 提交 ===
git commit -m "message"             # 提交更改
git commit --amend                  # 修改上次提交

# === 推送 ===
git push origin master              # 推送到主分支
git push -f origin master           # 强制推送（谨慎！）
git push --all origin               # 推送所有分支

# === 远程仓库 ===
git remote -v                       # 查看远程仓库
git remote add origin URL           # 添加远程仓库
git remote set-url origin URL       # 更改远程仓库地址

# === 拉取更新 ===
git pull origin master              # 拉取并合并
git fetch origin                    # 仅拉取不合并
```

---

## 🚀 完整推送流程示例

```powershell
# 1. 进入项目目录
cd D:\COMP5541\project\simclr-pytorch

# 2. 检查状态
git status

# 3. 添加所有文件
git add .

# 4. 提交更改
git commit -m "Add Chinese documentation and Windows optimization"

# 5. 推送到 GitHub
git push origin master

# 如果是新仓库，首次推送需要设置上游分支
git push -u origin master
```

---

## 📞 需要帮助？

遇到问题时：

1. ✅ 检查 `.gitignore` 是否正确配置
2. ✅ 确认 GitHub 凭据是否有效
3. ✅ 查看错误信息并搜索解决方案
4. ✅ 访问 GitHub Docs: https://docs.github.com/

---

**一键推送命令**：
```powershell
.\push_to_github.bat
```

**祝推送顺利！** 🎉
