import numpy as np

#Return the identity array with ones on the main diagonal.
arr=np.identity(3)
print(arr)
print(type(arr))

print("\n")

#Return the array with dtype int
arr=np.identity(2,dtype='int')
print(arr)
print(type(arr))

#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_id.py
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
<class 'numpy.ndarray'>


[[1 0]
 [0 1]]
<class 'numpy.ndarray'>
'''