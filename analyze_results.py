"""
详细分析 SimCLR 训练结果
"""
import torch
import os
import json
import sys

# 修复 Windows 控制台编码问题
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

print("=" * 70)
print("SimCLR 训练结果详细分析")
print("=" * 70)

# 最新的检查点
checkpoint_path = "./runs/Nov18_13-33-26
_MyDevice/checkpoint_0001.pth.tar"

if not os.path.exists(checkpoint_path):
    print(f"\n错误：未找到检查点文件: {checkpoint_path}")
    exit(1)

print(f"\n检查点文件: {checkpoint_path}")
print(f"文件大小: {os.path.getsize(checkpoint_path) / (1024*1024):.2f} MB")

# 加载检查点
print("\n正在加载检查点...")
checkpoint = torch.load(checkpoint_path, map_location='cpu')

print("\n" + "=" * 70)
print("模型训练信息:")
print("=" * 70)

# 显示检查点内容
for key in checkpoint.keys():
    print(f"\n{key}:")
    if key == 'state_dict':
        print(f"  模型参数数量: {len(checkpoint[key])} 层")
        print("  前5层:")
        for i, (param_name, param) in enumerate(list(checkpoint[key].items())[:5]):
            print(f"    {i+1}. {param_name}: {param.shape}")
        print("  ...")
        print("  后5层:")
        for i, (param_name, param) in enumerate(list(checkpoint[key].items())[-5:]):
            print(f"    {i+1}. {param_name}: {param.shape}")
    elif key == 'optimizer':
        print(f"  优化器状态已保存")
    else:
        print(f"  {checkpoint[key]}")

# 计算总参数量
total_params = sum(p.numel() for p in checkpoint['state_dict'].values())
print(f"\n总参数量: {total_params:,} ({total_params/1e6:.2f}M)")

print("\n" + "=" * 70)
print("训练总结:")
print("=" * 70)
print(f"✓ 训练架构: {checkpoint['arch']}")
print(f"✓ 训练轮数: {checkpoint['epoch']} epochs")
print(f"✓ 模型已保存并可用于:")
print("  1. 特征提取 (Feature Extraction)")
print("  2. 迁移学习 (Transfer Learning)")
print("  3. 下游任务微调 (Fine-tuning)")
print("\n" + "=" * 70)

# 提供使用示例
print("\n如何使用训练好的模型:")
print("-" * 70)
print("""
# 示例代码：加载预训练模型

import torch
from models.resnet_simclr import ResNetSimCLR

# 加载模型
model = ResNetSimCLR(base_model='resnet18', out_dim=128)
checkpoint = torch.load('./runs/Nov17_21-59-10_MyDevice/checkpoint_0002.pth.tar')
model.load_state_dict(checkpoint['state_dict'])
model.eval()

# 使用模型提取特征
with torch.no_grad():
    features = model(your_images)
    # features 可用于下游任务
""")
print("-" * 70)

print("\n查看训练曲线和详细指标:")
print("  运行: start_tensorboard.bat")
print("  或执行: tensorboard --logdir=./runs")
print("\n" + "=" * 70)
