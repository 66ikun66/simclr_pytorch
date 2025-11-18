import torch
import torchvision
import sys

# 修复 Windows 控制台编码问题
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

print('Python 环境检查:')
print('PyTorch 版本:', torch.__version__)
print('TorchVision 版本:', torchvision.__version__)
print('CUDA 可用:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('CUDA 版本:', torch.version.cuda)
    print('GPU 设备:', torch.cuda.get_device_name(0))
else:
    print('CUDA 版本: N/A')
    print('GPU 设备: N/A')
