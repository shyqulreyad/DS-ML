'''
pytorch is a python package that provides two high-level features:
    1. Tensor computation (like numpy) with strong GPU acceleration
    2. Deep Neural Networks built on a tape-based autograd system
    
'''

import torch

# print(torch.__version__)

# Tensor
# A tensor is a generalization of vectors and matrices to potentially higher dimensions.
# Internally, pytorch represents tensors as n-dimensional arrays of base datatypes.
# A tensor can be constructed from a Python list or sequence using the torch.tensor() constructor.

#Scalar
'''
x = torch.tensor(3.14159)
print(x)
print(type(x))
print(x.ndim)
print(x.shape)
print(x.item())
'''

#Vector
'''
vactor = torch.tensor([1,2,3,4,5])
print(vactor)
print(vactor.ndim)
print(vactor.shape)
'''
#Matrix
matrix = torch.tensor([[1,2,3],[4,5,6]])
print(matrix)
print(matrix.ndim)
print(matrix.shape)
print(matrix[0][0])

#Tensor
tensor = torch.tensor([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)
print(tensor.shape)