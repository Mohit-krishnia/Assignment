import numpy as np

# Creating a NULL Vector of size 10 but 5th value is 1
x=np.zeros(10)
x[4]=1
print(x)

# Create a vector with values ranging from 10 to 49
x=np.arange(10,50)
print(x)

# Create a 3x3 matrix with values from 0 to 8
x =  np.arange(0,9)
x = x.reshape(3,3)
print(x)

# Find indices of non-zero elements from [1,2,0,0,4,0]
x = [1,2,0,0,4,0]
np.nonzero(x)

# Create a 10x10 array with random values and find the minimum and maximum values
x = np.random.random((10,10))
xmin,xmax = x.min(),x.max()
print(xmin,xmax)

# Create a random vector of size 30 and find the mean value
Z = np.random.random(30)
m = Z.mean()
print(m)