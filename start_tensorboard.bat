@echo off
REM 设置控制台为UTF-8编码
chcp 65001 >nul

echo ====================================
echo 启动 TensorBoard 查看训练结果
echo ====================================
echo.

echo 正在激活 simclr_pytorch 环境...
call D:\Anaconda\Scripts\activate.bat simclr_pytorch

echo.
echo ====================================
echo TensorBoard 已启动！
echo ====================================
echo.
echo 请在浏览器中打开以下地址查看训练可视化：
echo.
echo     http://localhost:6006
echo.
echo ====================================
echo 按 Ctrl+C 停止 TensorBoard
echo ====================================
echo.

tensorboard --logdir=./runs --host=localhost --port=6006
