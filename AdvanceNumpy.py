
import numpy as np
from pandas import array

x = np.arange(12).reshape(4,3)
x = np.sort(x)

y = np.array([101,11,21,99,90])
print("Y = " , y)
print(np.sort(y))

z = np.array([[21,21,22],[3,99,1],[22,2000,1]])
print("\n Z = \n" , z)
print("Sorting \n" , np.sort(z,axis=0))


# Defining Data Type
dt = (np.dtype([('name','S10'),('cell' , int)]))
listOfStd = (np.array([('imtiaz',33),('ilyas' , 55),('Fayyaz',21)], dtype=dt))
print(listOfStd)
print("Sorted List = " , np.sort(listOfStd , order='name'))
# print(np.typename(listOfStd))



