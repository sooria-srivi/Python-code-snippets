import numpy as np

a = np.array([23,67,45,89,34,67])
print(a)

a[2] = 100
print("after changing 2nd element",a)
a[3:5] = 200,300
print("after changing 3rd 4th element",a)
d = a[1:4]
print("slicing from 1 to 3",d)

#vector additiom using numpy

a1 = np.array([2,5,6])
b1 = np.array([5,7,8])

z1 = a1+b1
print("adding 2 numpy arrays",z1)
#vector additiom using list
z = []
for n,m in zip(a1,b1):
    z.append(n+m)

print("adding 2 list a1+b1",z)

#vector multiplication using numpy

a1 = np.array([2,5,6])

z1 = 3*a1
print("multiplication of numpy array with scalar ",z1)
#vector multiplication using list

z = []
for n in a1:
    z.append(3*n)

print("multiplication of list with scalar ",z)

#vector product using numpy

a1 = np.array([2,5,6])
b1 = np.array([2,4,3])
z1 = a1*b1
print("product using numpy",z1)
#vector product using list

z = []
for n,m in zip(a1,b1):
    z.append(n*m)

print("product using list",z)

#dot product using numpy

a1 = np.array([2,5,6])
b1 = np.array([2,4,3])
z1 = np.dot(a1,b1)
print("dot product a1.b1 ",z1)

"""broadcasting property - numpy. 
 if a scalar value is added to array, each element in the array will be added with that
scalar value"""

z1 = a1+5
print("after broadcasting(a1+5) the array is",z1)

#universal funtions to numpy array

""" to calculate mean of array"""

z1 = a1.mean()
print("mean of a1 ",z1)
print("max element in array a1 ",a1.max())
print("min element in array a1 ",a1.min())
print("print value of pi ",np.pi)
x = np.array([0,np.pi/2,np.pi])
print("array created with pi ",x)
y = np.sin(x)
print("sin(x) ",y)
