import numpy as np

#base is a multi dimensional array containing 2 arrays
base=np.array([[2,3,4],['Raj','Ram','Yak']])

print(base)

print(type(base))

print("Dimension is: " , base.ndim)

print("Shape is: ",base.shape)

print("Size is: ", base.size)

print("Data type object is: ", base.dtype)


#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python npbasic.py
[['2' '3' '4']
 ['Raj' 'Ram' 'Yak']]
<class 'numpy.ndarray'>
Dimension is:  2
Shape is:  (2, 3)
Size is:  6
Data type object is:  <U11

'''
