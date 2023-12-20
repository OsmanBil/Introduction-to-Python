## We import NumPy into Python
import numpy as np

## We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

## Let's print the ndarray we just created using the print() command
print('x = ', x)


# Rank of an Array (numpy.ndarray.ndim)

## 1-D array
x = np.array([1, 2, 3])
x.ndim

## 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
Y.ndim

## Here the`zeros()` is an inbuilt function that you'll study on the next page. 
## The tuple (2, 3, 4( passed as an argument represents the shape of the ndarray
y = np.zeros((2, 3, 4))
y.ndim

# Example 1.a - Using a 1-D Array of Integers
## We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

## We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)



