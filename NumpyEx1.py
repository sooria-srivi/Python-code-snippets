import numpy as np

arr = np.array([(1,2,3),(3,4,5),(6,8,9)])
arr2 = np.array([(2.5,3.23),(2.5,6.1),(9.09,0.9),(4.78,8.4)])
arr3 = np.array([[(2,3),(3,4)],[(3,4),(34,87)]])
arr4 = np.array([('hai','hello')])

print("type of array1 : ",type(arr))

print("dimenstion of array1 : ",arr.ndim)
print("dimenstion of array2 : ",arr2.ndim)
print("dimenstion of array3 : ",arr3.ndim)
print("dimenstion of array4 : ",arr4.ndim)

#rows & cols
print("shape of array1 : ",arr.shape)
print("shape of array2 : ",arr2.shape)
print("shape of array3 : ",arr3.shape)
print("shape of array4 : ",arr4.shape)

#no of elements
print("size of array1 : ",arr.size)
print("size of array2 : ",arr2.size)
print("size of array3 : ",arr3.size)
print("size of array4 : ",arr4.size)

#data type of each element
print("data type of array1 : ",arr.dtype)
print("data type of array2 : ",arr2.dtype)
print("data type of array3 : ",arr3.dtype)
print("date type of array4 : ",arr4.dtype)

#memory size of each element
print("memory size of each element in array1 : ",arr.itemsize)
print("memory size of each element in array2 : ",arr2.itemsize)
print("memory size of each element in array3 : ",arr3.itemsize)
print("memory size of each element in array4 : ",arr4.itemsize)

print("data of each element in array4 : ",arr4.data)
print("data of each element in array3 : ",arr3.data)
