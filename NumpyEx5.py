import numpy as np

a = np.arange(10000).reshape(100,100)
print(a)
#np.set_printoptions(threshold=np.nan)
#print(a)

print(np.nan)

A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )
print(A * B)         # elementwise product
print(A @ B)         # matrix product (use @ symbol for matrix product)
print(A.dot(B))      # another matrix product

"""
zeros_like Return an array of zeros with the same shape and type as a given array.
empty_like Return an empty array with shape and type of input.
ones_like Return an array of ones with shape and type of input.
"""

x = np.arange(6).reshape((2, 3))
print(x)
print(np.zeros_like(x))

y = np.arange(3, dtype=float)
print(y)
print(np.zeros_like(y))

"""
Create an array of the given shape and populate it with random samples from a 
uniform distribution over [0, 1).
"""

print(np.random.rand(3,4))
print(np.random.randn(3,4)) # n stands for normal distribution

a = np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
print(a)

a = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
print(a)


