import numpy as np

arr = np.arange(20).reshape(4,5)
print("array1 : \n",arr)

arr2 = np.arange(100,120).reshape(4,5)
print("array2 : \n",arr2)

arr3 = np.array([(10,76,76),(65,98,54)], dtype = 'complex')
print("array3 : \n",arr3)

arr4 = np.zeros((2,2,2))
print("array4 : \n",arr4)

arr5 = np.ones((2,5),dtype=np.int32)
print("array5 : \n",arr5)

arr6 = np.empty((2,5))
print("array6 : \n",arr6)

arr7 = np.ones((2,5),dtype='int')
print("array7 : \n",arr7)

arr8 = np.arange( 10, 30, 4 )
print("array8 : \n",arr8) # 10, 10+4, 14+4, 18+4, 22+4

arr11 = np.arange( 10, 30, 5 )
print("array11 : \n",arr11)

arr9 = np.arange( 0, 2, 0.3 )     
print("array9 : \n",arr9)

"""
When arange is used with floating point arguments, it is generally not possible
to predict the number of elements obtained,  due to the finite floating point 
precision. For this reason, it is usually better to use the function linspace 
that receives as an argument the number of elements that we want, instead of
the step: 
"""

arr10 = np.linspace( 0, 2, 9 ) #totally no elements, so it will split accordingly  
print("array10 : \n",arr10)

arr12 = np.linspace( 0, 2, 3 ) #totally no elements, so it will split accordingly  
print("array10 : \n",arr12)
