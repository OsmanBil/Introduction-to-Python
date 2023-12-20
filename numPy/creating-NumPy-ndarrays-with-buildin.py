import numpy as np

# We create a 1D ndarray that contains only integers
x = np.zeros((3, 4), dtype=int)
print(x)

# We print information about x
print('dtype:', x.dtype)

# We create a 1D ndarray that contains only integers
x = np.ones((4, 5))
print(x)

# We create a 1D ndarray that contains only integers
x = np.full((4, 3), 5)
print(x)
print('dtype:', x.dtype)

# We create identity matrices of size 5x5
x = np.eye(5)
print(x)

# We create a 4x4 diagonal matrix that contains the numbers 10,20,30, and 50
x = np.diag([10, 20, 30, 50])
print(x)

# We create a rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)
print(x)

# We create a rank 1 ndarray that has sequential integers from 4 to 9
x = np.arange(4, 10)
print(x)

# We create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
x = np.arange(1, 14, 3)
print(x)

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0, 25, 10)
print(x)

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25, with 25 excluded.
x = np.linspace(0, 25, 10, endpoint=False)
print(x)

# We create a numpy array x containing a sequence of numbers from 0 to 19.
x = np.arange(20)
print(x)

# We reshape x into a 4 x 5 ndarray of integers
x = np.reshape(x, (10,2))
print(x)

# Same as above. We reshape x into a 4 x 5 ndarray of integers
# We reshape x into a 4 x 5 ndarray of integers
y = np.arange(20).reshape((10,2))
print(y)

# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
x = np.linspace(0, 50, 10, endpoint=False).reshape(5,2)
print(x)

# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
x = np.random.random((3, 3))
print(x)

# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
x = np.random.randint(4, 15, (3, 2))
print(x)

# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
x = np.random.normal(0, 0.1, size=(1000, 1000))
print(x)