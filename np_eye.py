import numpy as np

#Return a 2-D array with ones on the diagonal and zeros elsewhere.
arr1=np.eye(3)
print(arr1)

#Return upper triangular matrix with main diagonal zero if k=+ve value
arr1=np.eye(3,k=1)
print(arr1)

##Return lower triangular matrix with main diagonal zero if k=-ve value
arr1=np.eye(3,k=-1)
print(arr1)

#Return dtype with int
arr1=np.eye(2,dtype='int')
print(arr1)

#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_eye.py
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
 
[[0. 1. 0.]
 [0. 0. 1.]
 [0. 0. 0.]]
 
[[0. 0. 0.]
 [1. 0. 0.]
 [0. 1. 0.]]
 
[[1 0]
 [0 1]]
'''