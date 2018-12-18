import numpy as np
import random

#2 random values 1D array
q1=np.random.rand(2)
print("1D random matrix:")
print(q1)

print("\n")

#4*4 random matrix
q2=np.random.rand(4,4)
print("2D random matrix:")
print(q2)

print("\n")

#3*3 random matrix using tuple format
q3=np.random.random((3,3))
print("2D tupled random matrix:")
print(q3)

#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_options3.py
1D random matrix:
[0.4486862  0.23145038]


2D random matrix:
[[0.64537764 0.21350449 0.95769696 0.30623651]
 [0.34062855 0.10729718 0.82974543 0.24063598]
 [0.44706953 0.67171899 0.05207992 0.74832117]
 [0.2313878  0.12660356 0.04516504 0.8435473 ]]


2D tupled random matrix:
[[0.55785373 0.09793257 0.85556524]
 [0.84765479 0.85618044 0.091721  ]
 [0.60297235 0.95994546 0.52400399]]
'''