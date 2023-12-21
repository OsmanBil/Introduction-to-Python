
import numpy as np

# slicing ndarrays
# ndarray[start:end]
# ndarray[start:]
# ndarray[:end]

# ndarray[start:end, start:end]
x = np.arange(1, 21).reshape(4, 5)
print(x)

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
z = x[1:4, 2:5]
print(z)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
z = x[1:, 2:]
print(z)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
z = x[:3, 2:]
print(z)

# We select all the elements in the 3rd row
z = x[:, 2]
print(z)

# We select all the elements in the 3rd column
z = x[:, 2:3]
print(z)

# We select all the elements in the 3rd column but return a rank 1 ndarray
z = x[1:, 2:]
print(z)


z[2,2] = 555
print(z)


x = np.arange(1, 21).reshape(4, 5)
print(x)