import numpy as np

'''
#Contentsof myfile.txt
Value1  Value2  Value3
0.2536  0.1008  0.3857
0.4839  0.4536  0.3561
0.1292  0.6875  0.5929
0.1781  0.3049  0.8928
0.6253  0.3486  0.8791
'''

x, y, z = np.loadtxt('myfile.txt',skiprows=1,unpack=True)

#skiprows : int, optional
#Skip the first skiprows lines; default: 0.


#unpack : bool, optional
#If True, the returned array is transposed, 
#so that arguments may be unpacked


print(x, y, z)

'''
OUTPUT:
stud@HP-246-Notebook-PC:~$ python np_load.py
[0.2536 0.4839 0.1292 0.1781 0.6253]
[0.1008 0.4536 0.6875 0.3049 0.3486] 
[0.3857 0.3561 0.5929 0.8928 0.8791]
'''
