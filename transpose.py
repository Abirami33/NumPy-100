import numpy as np

#original array
arr = np.array([1, 2, 3])
print("Oringinal array is: ",arr)
print("Original array's shape is: ",arr.shape)

arr = np.array(arr, ndmin=2).T
print("Transposed array is: ")
print(arr)
print("Transposed array's shape is: ",arr.shape)

'''
OUTPUT:

stud@HP-246-Notebook-PC:~$ python transpose.py
Oringinal array is:  [ 1  2 3]
Original array's shape is:  (3,)
Transposed array is: 
[[ 1]
 [ 2]
 [3]]
Transposed array's shape is:  (3, 1)

'''