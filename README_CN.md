# SimCLR PyTorch 实现

> 自监督对比学习框架 - 在 Windows + Anaconda 环境下优化

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 1.4+](https://img.shields.io/badge/pytorch-1.4+-orange.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)

---

## 📖 项目简介

**SimCLR** (Simple Framework for Contrastive Learning of Visual Representations) 是一个强大的自监督学习框架，能够在无标注数据的情况下学习高质量的视觉表示。

### 主要特点

- ✅ **自监督学习**：无需人工标注即可训练
- ✅ **对比学习**：通过数据增强学习不变特征
- ✅ **即插即用**：可用于各种下游视觉任务
- ✅ **GPU 加速**：支持 CUDA 加速训练
- ✅ **Windows 优化**：已修复 Windows 多进程和编码问题

---

## 🚀 5分钟快速开始

### 1️⃣ 检查环境
```powershell
.\check_environment.bat
```

### 2️⃣ 开始训练
```powershell
.\run_simclr.bat
```

### 3️⃣ 查看结果
```powershell
.\start_tensorboard.bat
```
然后访问：http://localhost:6006

**详细说明**：查看 [快速开始.md](./快速开始.md)

---

## 📁 项目结构

```
simclr-pytorch/
├── 📄 快速开始.md                    # ⭐ 5分钟快速入门
├── 📄 完整使用指南.md                # ⭐ 详细文档
├── 📄 TRAINING_RESULTS.md           # 训练结果总结
│
├── 🚀 run_simclr.bat                # ⭐ 一键训练
├── 📊 start_tensorboard.bat         # ⭐ 启动可视化
├── ✅ check_environment.bat         # 环境检查
├── 📈 view_training_results.bat    # 查看结果摘要
├── 🔍 analyze_model.bat             # 模型分析
│
├── 🐍 run.py                        # 原始训练脚本
├── 🐍 simple_run.py                 # 简化训练脚本（推荐）
├── 🐍 simclr.py                     # SimCLR 核心实现
├── 🐍 utils.py                      # 工具函数
│
├── 📂 models/                       # 模型定义
│   └── resnet_simclr.py
├── 📂 data_aug/                     # 数据增强
│   ├── contrastive_learning_dataset.py
│   ├── gaussian_blur.py
│   └── view_generator.py
├── 📂 datasets/                     # 数据集（自动下载）
└── 📂 runs/                         # 训练结果和日志
```

---

## 💻 环境要求

### 必需环境
- **操作系统**：Windows 10/11
- **Python**：3.7+
- **Anaconda**：已安装并配置
- **GPU**：NVIDIA GPU（支持 CUDA）

### 必需依赖
```
torch >= 1.4.0
torchvision >= 0.5.0
tensorboard >= 2.1
tqdm
pyyaml
```

### 环境安装

**方法 1：使用 conda 环境文件**
```powershell
conda env create -f env.yml
conda activate simclr
```

**方法 2：手动安装**
```powershell
conda create -n simclr_pytorch python=3.12
conda activate simclr_pytorch
pip install torch torchvision tensorboard tqdm pyyaml
```

---

## 🎯 使用方法

### 基础训练

**使用批处理文件（推荐）**：
```powershell
.\run_simclr.bat
```

**使用 Python 脚本**：
```powershell
conda activate simclr_pytorch
python simple_run.py
```

### 自定义训练

编辑 `simple_run.py` 中的参数：
```python
class Args:
    def __init__(self):
        self.epochs = 100              # 训练轮数
        self.batch_size = 128          # 批次大小
        self.dataset_name = 'cifar10'  # 数据集：cifar10 或 stl10
        self.arch = 'resnet18'         # 模型：resnet18 或 resnet50
        # ... 更多参数
```

或使用命令行参数：
```powershell
python run.py ^
  -data ./datasets ^
  -dataset-name cifar10 ^
  --arch resnet18 ^
  --epochs 100 ^
  --batch-size 128
```

---

## 📊 查看训练结果

### TensorBoard 可视化（推荐）
```powershell
.\start_tensorboard.bat
```
访问：http://localhost:6006

### 查看摘要
```powershell
.\view_training_results.bat
```

### 详细分析
```powershell
.\analyze_model.bat
```

---

## 🔬 使用训练好的模型

### 特征提取
```python
import torch
from models.resnet_simclr import ResNetSimCLR

# 加载模型
model = ResNetSimCLR(base_model='resnet18', out_dim=128)
checkpoint = torch.load('runs/最新目录/checkpoint_*.pth.tar')
model.load_state_dict(checkpoint['state_dict'])
model.eval()

# 提取特征
with torch.no_grad():
    features = model(images)  # [batch_size, 128]
```

### 迁移学习
```python
# 冻结特征提取器
for param in model.backbone.parameters():
    param.requires_grad = False

# 添加分类头
classifier = nn.Linear(128, num_classes)

# 训练分类器
# ...
```

详细示例：查看 [完整使用指南.md](./完整使用指南.md)

---

## 📈 训练结果示例

基于 CIFAR-10 数据集，2 epochs 快速测试：

| Epoch | Loss | Top-1 Accuracy | 耗时 |
|-------|------|----------------|------|
| 0 | 4.114 | 12.5% | ~2.5 分钟 |
| 1 | 3.490 | 17.97% | ~2.5 分钟 |

**注意**：这是对比学习任务的准确率，不是分类准确率。完整训练建议 100-1000 epochs。

---

## 📚 文档

- **快速开始**：[快速开始.md](./快速开始.md) - 5分钟入门
- **完整指南**：[完整使用指南.md](./完整使用指南.md) - 详细文档
- **训练结果**：[TRAINING_RESULTS.md](./TRAINING_RESULTS.md) - 结果分析

---

## ❓ 常见问题

### Q: 控制台显示乱码怎么办？
**A**: 使用提供的 `.bat` 批处理文件运行，已包含编码修复。

### Q: 训练报错 multiprocessing error？
**A**: 已修复，`simple_run.py` 中设置了 `workers=0`。

### Q: GPU 内存不足怎么办？
**A**: 减小 `batch_size` 参数，例如设置为 32 或 64。

### Q: 准确率为什么这么低？
**A**: 这是对比学习任务的准确率，要评估真实性能需要进行线性评估。

更多问题：查看 [完整使用指南.md](./完整使用指南.md)

---

## 🔧 已修复的问题

本项目针对 Windows 环境做了以下优化：

- ✅ 修复了 Windows 多进程启动错误
- ✅ 修复了控制台中文乱码问题
- ✅ 添加了一键启动批处理脚本
- ✅ 优化了 DataLoader workers 设置
- ✅ 添加了详细的中文文档

---

## 📄 许可证

本项目基于 MIT 许可证开源。详见 [LICENSE.txt](LICENSE.txt)

---

## 🙏 致谢

- 原始论文：[SimCLR: A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)
- 原始实现：[sthalles/SimCLR](https://github.com/sthalles/SimCLR)
- Google Research：[google-research/simclr](https://github.com/google-research/simclr)

---

## 📞 支持

- 查看文档：[完整使用指南.md](./完整使用指南.md)
- 检查环境：`.\check_environment.bat`
- 查看日志：`runs/*/training.log`

---

**快速开始训练：`.\run_simclr.bat`** 🚀

**查看可视化结果：`.\start_tensorboard.bat`** 📊
