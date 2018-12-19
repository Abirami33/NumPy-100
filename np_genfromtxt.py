#genfromtxt can process even unordered array
import numpy as np

'''
CONTENTS OF myfile.txt
Value1  Value2  Value3
0.2536  0.1008  0.3857
0.4839  0.4536  0.3561
0.1292  0.6875  0.5929
MISSING MISSING 0.4567
0.1781  0.3049  0.8928
0.6253  0.3486  0.8791
'''
#skipheader-->no.of lines to skip at the beginning
arr= np.genfromtxt('myfile.txt',skip_header=1,filling_values=0)

#fills the missing values as 0-->filling_values
print(arr)


#Output:
'''
stud@HP-246-Notebook-PC:~$ python np_genfromtxt.py
[[0.2536 0.1008 0.3857]
 [0.4839 0.4536 0.3561]
 [0.1292 0.6875 0.5929]
 [0.     0.     0.4567]
 [0.1781 0.3049 0.8928]
 [0.6253 0.3486 0.8791]]
 
'''