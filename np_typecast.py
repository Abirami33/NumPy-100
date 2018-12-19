import numpy as np

#can change the type of the np array
b=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], dtype="double")
print(b)

b=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], dtype="complex")
print(b)

b=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], dtype="float")
print(b)

b=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], dtype="int")
print(b)





#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_typecast.py
[[1. 2. 3.]
 [3. 4. 5.]
 [5. 6. 7.]]
 
[[1.+0.j 2.+0.j 3.+0.j]
 [3.+0.j 4.+0.j 5.+0.j]
 [5.+0.j 6.+0.j 7.+0.j]]
 
[[1. 2. 3.]
 [3. 4. 5.]
 [5. 6. 7.]]
 
[[1 2 3]
 [3 4 5]
 [5 6 7]]

'''