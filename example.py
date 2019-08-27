import PixelUnshuffle
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.range(start=0, end=31).reshape([1, 8, 2, 2])
print('x:')
print(x.shape)
print(x)
y = F.pixel_shuffle(x, 2)
print('y:')
print(y.shape)
print(y)
x_ = PixelUnshuffle.pixel_unshuffle(y, 2)
print('x_:')
print(x_.shape)
print(x_)