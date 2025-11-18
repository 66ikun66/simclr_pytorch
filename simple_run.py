import sys
import os

# 强制禁用输出缓冲，确保实时显示
sys.stdout.reconfigure(line_buffering=True) if hasattr(sys.stdout, 'reconfigure') else None
os.environ['PYTHONUNBUFFERED'] = '1'

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse
import torch
import torch.backends.cudnn as cudnn
from torchvision import models
from data_aug.contrastive_learning_dataset import ContrastiveLearningDataset
from models.resnet_simclr import ResNetSimCLR
from simclr import SimCLR

# 创建参数
class Args:
    def __init__(self):
        self.data = './datasets'
        self.dataset_name = 'cifar10'
        self.arch = 'resnet18'
        self.workers = 0  # Windows上设置为0避免多进程问题
        self.epochs = 10
        self.batch_size = 256
        self.lr = 0.0003
        self.weight_decay = 1e-4
        self.seed = None
        self.disable_cuda = False
        self.fp16_precision = False
        self.out_dim = 128
        self.log_every_n_steps = 10
        self.temperature = 0.07
        self.n_views = 2
        self.gpu_index = 0

def main():
    print("开始导入模块...", flush=True)
    print("模块导入成功!", flush=True)
    print(f"PyTorch版本: {torch.__version__}", flush=True)
    print(f"CUDA可用: {torch.cuda.is_available()}", flush=True)
    if torch.cuda.is_available():
        print(f"GPU设备: {torch.cuda.get_device_name(0)}", flush=True)

    args = Args()

    print("\n配置参数:", flush=True)
    print(f"  数据集: {args.dataset_name}", flush=True)
    print(f"  模型架构: {args.arch}", flush=True)
    print(f"  训练轮数: {args.epochs}", flush=True)
    print(f"  批次大小: {args.batch_size}", flush=True)
    print(f"  学习率: {args.lr}", flush=True)
    print(f"  工作进程数: {args.workers} (Windows兼容模式)", flush=True)

    # 检查设备
    if not args.disable_cuda and torch.cuda.is_available():
        args.device = torch.device('cuda')
        cudnn.deterministic = True
        cudnn.benchmark = True
        print(f"  使用设备: GPU (CUDA)", flush=True)
    else:
        args.device = torch.device('cpu')
        args.gpu_index = -1
        print(f"  使用设备: CPU", flush=True)

    print("\n准备数据集...", flush=True)
    dataset = ContrastiveLearningDataset(args.data)
    train_dataset = dataset.get_dataset(args.dataset_name, args.n_views)
    print(f"数据集加载成功! 样本数: {len(train_dataset)}", flush=True)

    print("\n创建数据加载器...", flush=True)
    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=True,
        num_workers=args.workers, pin_memory=True, drop_last=True)
    print(f"数据加载器创建成功! 批次数: {len(train_loader)}", flush=True)

    print("\n创建模型...", flush=True)
    model = ResNetSimCLR(base_model=args.arch, out_dim=args.out_dim)
    print("模型创建成功!", flush=True)

    print("\n创建优化器和调度器...", flush=True)
    optimizer = torch.optim.Adam(model.parameters(), args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=len(train_loader), eta_min=0, last_epoch=-1)
    print("优化器和调度器创建成功!", flush=True)

    print("\n" + "="*60, flush=True)
    print("开始训练 SimCLR 模型...", flush=True)
    print("="*60 + "\n", flush=True)

    with torch.cuda.device(args.gpu_index):
        simclr = SimCLR(model=model, optimizer=optimizer, scheduler=scheduler, args=args)
        simclr.train(train_loader)

    print("\n" + "="*60, flush=True)
    print("训练完成!", flush=True)
    print("="*60, flush=True)

if __name__ == '__main__':
    main()
