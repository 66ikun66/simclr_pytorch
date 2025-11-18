@echo off
REM 设置控制台为UTF-8编码
chcp 65001 >nul

echo ====================================
echo 分析训练模型
echo ====================================
echo.

echo 正在激活 simclr_pytorch 环境...
call D:\Anaconda\Scripts\activate.bat simclr_pytorch

echo.
python analyze_results.py

echo.
echo ====================================
pause
