"""
查看 SimCLR 训练结果
"""
import os
import glob
from datetime import datetime
import sys

# 修复 Windows 控制台编码问题
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

print("=" * 70)
print("SimCLR 训练结果查看器")
print("=" * 70)

# 查找所有训练运行
runs_dir = "./runs"
if not os.path.exists(runs_dir):
    print("错误：未找到训练结果目录")
    exit(1)

# 获取所有运行目录
run_dirs = [d for d in glob.glob(os.path.join(runs_dir, "*")) if os.path.isdir(d)]
run_dirs.sort(key=lambda x: os.path.getmtime(x), reverse=True)

print(f"\n找到 {len(run_dirs)} 个训练运行记录:\n")

for i, run_dir in enumerate(run_dirs[:5], 1):  # 显示最近5个
    dir_name = os.path.basename(run_dir)
    mod_time = os.path.getmtime(run_dir)
    mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"{i}. {dir_name}")
    print(f"   时间: {mod_time_str}")
    
    # 检查是否有日志文件
    log_file = os.path.join(run_dir, "training.log")
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            print(f"   日志行数: {len(lines)}")
            
            # 提取关键信息
            for line in lines:
                if "epochs" in line.lower():
                    print(f"   {line.strip()}")
                elif "Loss:" in line and "Top1 accuracy:" in line:
                    print(f"   {line.strip()}")
                elif "finished" in line.lower():
                    print(f"   {line.strip()}")
    
    # 检查是否有模型检查点
    checkpoints = glob.glob(os.path.join(run_dir, "*.pth.tar"))
    if checkpoints:
        print(f"   模型检查点: {len(checkpoints)} 个")
        for cp in checkpoints:
            size_mb = os.path.getsize(cp) / (1024 * 1024)
            print(f"     - {os.path.basename(cp)} ({size_mb:.2f} MB)")
    
    print()

# 最新的训练运行
if run_dirs:
    latest_run = run_dirs[0]
    print("=" * 70)
    print(f"最新训练运行: {os.path.basename(latest_run)}")
    print("=" * 70)
    
    log_file = os.path.join(latest_run, "training.log")
    if os.path.exists(log_file):
        print("\n完整训练日志:")
        print("-" * 70)
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            print(f.read())
        print("-" * 70)

print("\n" + "=" * 70)
print("查看训练详细可视化的方法:")
print("=" * 70)
print("\n方法 1: 启动 TensorBoard (推荐)")
print("  命令: tensorboard --logdir=./runs")
print("  然后在浏览器中打开: http://localhost:6006")
print("\n方法 2: 查看训练日志文件")
print(f"  位置: {latest_run}\\training.log")
print("\n方法 3: 加载模型检查点")
print(f"  位置: {latest_run}\\checkpoint_*.pth.tar")
print("\n" + "=" * 70)
