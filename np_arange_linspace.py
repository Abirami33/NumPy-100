import numpy as np

#from 1 to 10 skip 2 and print
b3=np.arange(1, 10, 2)
print(b3)

#NOTE: Arange is Similar to linspace, but uses a step size (instead of the number of samples).

#prints 7 values between 1 and 10
b4=np.linspace(1, 10, 7)
print(b4)

#OUTPUT:
'''
[1 3 5 7 9]

[ 1.   2.5  4.   5.5  7.   8.5 10. ]

'''
