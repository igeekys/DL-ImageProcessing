import torch
import torchvision
import PIL
print(torch.__version__,torch.cuda.is_available())
print(torch.rand(10).cuda())
print(torch.__version__)