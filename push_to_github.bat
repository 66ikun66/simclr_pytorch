@echo off
chcp 65001 >nul
echo ====================================
echo 推送项目到 GitHub
echo ====================================
echo.

echo [步骤 1/5] 检查 Git 状态...
git status
echo.

echo [步骤 2/5] 添加所有文件到暂存区...
git add .
echo ✓ 文件已添加
echo.

echo [步骤 3/5] 查看将要提交的文件...
git status
echo.
pause

echo [步骤 4/5] 提交更改...
set /p commit_message="请输入提交信息 (默认: Update SimCLR project with Chinese documentation): "
if "%commit_message%"=="" set commit_message=Update SimCLR project with Chinese documentation

git commit -m "%commit_message%"
echo ✓ 更改已提交
echo.

echo [步骤 5/5] 推送到 GitHub...
echo.
echo 正在推送到 origin/master...
git push origin master

if %errorlevel% neq 0 (
    echo.
    echo ❌ 推送失败！
    echo.
    echo 可能的原因:
    echo 1. 没有设置远程仓库（需要先在 GitHub 创建仓库）
    echo 2. 需要身份验证（GitHub Personal Access Token）
    echo 3. 网络连接问题
    echo.
    echo 请按照以下步骤操作:
    echo.
    echo === 如果还没有创建 GitHub 仓库 ===
    echo 1. 访问 https://github.com/new
    echo 2. 创建新仓库（不要初始化 README）
    echo 3. 复制仓库 URL
    echo 4. 运行: git remote set-url origin YOUR_REPO_URL
    echo 5. 再次运行本脚本
    echo.
    echo === 如果需要配置身份验证 ===
    echo 1. 生成 Personal Access Token:
    echo    https://github.com/settings/tokens
    echo 2. 使用 token 作为密码推送
    echo.
) else (
    echo.
    echo ====================================
    echo ✓ 推送成功！
    echo ====================================
    echo.
    echo 你的项目已成功推送到 GitHub
    echo.
)

pause
