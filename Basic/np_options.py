import numpy as np

#can change the type of the np array
b=np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], dtype="double")
print(b)

#a matrix full of zeros
b1=np.zeros((4, 4))
print(b1)

#a matrix full of const values
b2=np.full((2, 3),3)
print(b2)

#from 1 to 10 skip 2 and print
b3=np.arange(1, 10, 2)
print(b3)

#prints 7 values between 1 and 10
b4=np.linspace(1, 10, 7)
print(b4)

#reshaping array
b5=b.reshape(3, 3)
print(b5)

#flattening array
b6=b.flatten()
print(b6)

#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_options.py
[[1. 2. 3.]
 [3. 4. 5.]
 [5. 6. 7.]]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[3 3 3]
 [3 3 3]]
[1 3 5 7 9]
[ 1.   2.5  4.   5.5  7.   8.5 10. ]
[[1. 2. 3.]
 [3. 4. 5.]
 [5. 6. 7.]]
stud@HP-246-Notebook-PC:~$ python np_options.py
[[1. 2. 3.]
 [3. 4. 5.]
 [5. 6. 7.]]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[3 3 3]
 [3 3 3]]
[1 3 5 7 9]
[ 1.   2.5  4.   5.5  7.   8.5 10. ]
[[1. 2. 3.]
 [3. 4. 5.]
 [5. 6. 7.]]
[1. 2. 3. 3. 4. 5. 5. 6. 7.]
'''