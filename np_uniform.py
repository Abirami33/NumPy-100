import numpy as np

n= 500   #n is the number of samples drawn

#The values for the weight matrices should be chosen randomly and not arbitrarily.
#There are various ways to initialize the weight matrices randomly.
#The first one we will introduce is the unity function from numpy.random.
#It creates samples which are uniformly distributed
#over the half-open interval [low, high), which means that low is included and high is excluded. 
#Each value within the given interval is equally likely to be drawn by 'uniform'.

low = -1
high = 0
s = np.random.uniform(low, high, n) # (low, high,size)

# all values of s are within the half open interval [-1, 0) :
print(np.all(s >= -1))
print(np.all(s < 0))

# whether it lies within -1 and 0
print(np.all(s >= -1) and np.all(s < 0) )

'''
OUTPUT:
stud@HP-246-Notebook-PC:~$ python np_ML.py
True
True
True
'''