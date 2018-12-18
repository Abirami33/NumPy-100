import numpy as np

#conversion of list to np array
l1=[1,2,3,4]
print(l1)
print(type(l1))
d1=np.array(l1)
print(d1)
print(type(d1))

#conversion of tuple to np array
t1=(100,200,300,400)
print(t1)
print(type(t1))
d2=np.array(t1)
print(d2)
print(type(d2))

#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_options2.py
[1, 2, 3, 4]
<class 'list'>
[1 2 3 4]
<class 'numpy.ndarray'>
(100, 200, 300, 400)
<class 'tuple'>
[100 200 300 400]
<class 'numpy.ndarray'>
'''