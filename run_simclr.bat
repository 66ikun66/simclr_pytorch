@echo off
REM 设置控制台为UTF-8编码
chcp 65001 >nul

echo ====================================
echo SimCLR 启动脚本 - simclr_pytorch环境
echo ====================================
echo.

echo 正在激活 simclr_pytorch 环境...
call D:\Anaconda\Scripts\activate.bat simclr_pytorch

echo.
echo 当前 Python 环境:
python --version
echo.

echo 检查 GPU 配置...
python check_env.py
echo.

echo ====================================
echo 开始运行 SimCLR 训练
echo ====================================
echo.

python simple_run.py

echo.
echo ====================================
echo 完成！
echo ====================================
pause
