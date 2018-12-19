import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

#The data pointer indicates the memory address of the first byte in the array.
print(arr.data)

#The strides are the number of bytes that should be skipped in memory to go to the next element. 
#If your strides are (12,4),
#12 bytes to locate the next row
#4 bytes to locate the next column 
print(arr.strides)


#OUTPUT:
'''
stud@HP-246-Notebook-PC:~$ python np_data_strides.py
<memory at 0xb6190c6c>
(12, 4)
'''