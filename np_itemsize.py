import numpy as np

#Length of one array element in bytes.
arr=np.array([[1,2],[3,4]])

print(arr.itemsize)

arr1=np.array([[1,2,3],[4,5],[6]])

print(arr1.itemsize)

arr2=np.array([1,2,3,4,5],dtype="float")
print(arr2.itemsize)

arr2=np.array([1,2,3,4,5],dtype="complex")
print(arr2.itemsize)

#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_item_flag.py
4
4
8
16
'''