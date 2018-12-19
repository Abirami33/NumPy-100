import numpy as np

#creation of a tuple
t1=(100,200,300,400)
print(t1)

#prints type as tuple
print(type(t1))

#conversion of tuple to np array
d2=np.array(t1)

print(d2)

#prints type as ndarray
print(type(d2))

#OUTPUT:
'''
(100, 200, 300, 400)
<class 'tuple'>
[100 200 300 400]
<class 'numpy.ndarray'>

'''