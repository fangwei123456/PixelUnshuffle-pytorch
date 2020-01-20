# PixelUnshuffle-pytorch
PixelUnshuffle, inverse operation of PixelShuffle.



| in pytorch                                           | inverse in PixelUnshuffle                  |
| ---------------------------------------------------- | ------------------------------------------ |
| `nn.PixelShuffle(upscale_factor)`                    | `PixelUnshuffle(downscale_factor)`         |
| `nn.functional.pixel_shuffle(input, upscale_factor)` | `pixel_unshuffle(input, downscale_factor)` |



**Installation:**

```
1.Clone this repo.
2.Copy "PixelUnshuffle" folder in your project.
```

**Example:**

```python
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
```

output:

```python
x:
torch.Size([1, 8, 2, 2])
tensor([[[[ 0.,  1.],
          [ 2.,  3.]],

         [[ 4.,  5.],
          [ 6.,  7.]],

         [[ 8.,  9.],
          [10., 11.]],

         [[12., 13.],
          [14., 15.]],

         [[16., 17.],
          [18., 19.]],

         [[20., 21.],
          [22., 23.]],

         [[24., 25.],
          [26., 27.]],

         [[28., 29.],
          [30., 31.]]]])
y:
torch.Size([1, 2, 4, 4])
tensor([[[[ 0.,  4.,  1.,  5.],
          [ 8., 12.,  9., 13.],
          [ 2.,  6.,  3.,  7.],
          [10., 14., 11., 15.]],

         [[16., 20., 17., 21.],
          [24., 28., 25., 29.],
          [18., 22., 19., 23.],
          [26., 30., 27., 31.]]]])
x_:
torch.Size([1, 8, 2, 2])
tensor([[[[ 0.,  1.],
          [ 2.,  3.]],

         [[ 4.,  5.],
          [ 6.,  7.]],

         [[ 8.,  9.],
          [10., 11.]],

         [[12., 13.],
          [14., 15.]],

         [[16., 17.],
          [18., 19.]],

         [[20., 21.],
          [22., 23.]],

         [[24., 25.],
          [26., 27.]],

         [[28., 29.],
          [30., 31.]]]])

```

A neat way can be found here:
[pytorch/pytorch#2456](https://github.com/pytorch/pytorch/issues/2456)
