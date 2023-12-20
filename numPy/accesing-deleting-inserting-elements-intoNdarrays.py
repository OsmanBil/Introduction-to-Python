import numpy as np

x = np.array([1, 2, 3, 4, 5])
print('x = ', x)

# We access elements in an ndarray using indices inside square brackets.
print('1st element: ', x[0])
print('2nd element: ', x[1])
print('5th element: ', x[4])

print('1st element: ', x[-5])
print('2nd element: ', x[-4])
print('5th element: ', x[-1])

# We can Modyfying ndarrays using indices and assignment operators.
x[3] = 20
print('Modified x = ', x)

# We can also use negative indices.
x = np.arange(1, 10).reshape((3, 3))
print('Element at (0,0): ', x[0, 0])
print('Element at (0,1): ', x[0, 1])
print('Element at (2,2): ', x[2, 2])

x[0, 0] = 20
print(x)

# Adding and deleting elements

# Deletion of elements
x = np.array([1, 2, 3, 4, 5])
print('x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0, 4])
print(x)

y = np.arange(1, 10).reshape((3, 3))
print(y)

w = np.delete(y, 0, axis=0)
print(w)

v = np.delete(y, [0, 2], axis=1)
print(v)

# Adding elements (append)

x = np.array([1, 2, 3, 4, 5])
print(x)

# We append the integer 6 to x
x = np.append(x, 6)
print(x)

x = np.append(x, [7, 8])
print(x)

y = np.append(y, [[7, 8, 9]], axis=0)
print(y)

v = np.append(y, [[10], [20], [30]], axis=1)
print(v)

# Inserting elements
# We create a rank 1 ndarray
x = np.array([1, 2, 5, 6, 7])
print(x)

# We insert the integer 3 and 4 between 2 and 5 in x. We also insert the integer 8 and 9 between 7 and 6 in x.
x = np.insert(x, 2, [3, 4])
print(x)

y = np.array([[1, 2, 3], [7, 8, 9]])
print(y)

# We insert a row between the first and last row of y
w = np.insert(y, 1, [4, 5, 6], axis=0)
print(w)

# We insert a column full of 5s between the first and second column of y
v = np.insert(y, 1, 5, axis=1)
print(v)

# Stacking arrays
# We create two rank 1 ndarrays
x = np.array([1, 2])
y = np.array([3, 4])
print(x)
print(y)

# We stack x and y vertically
z = np.vstack((x, y))
print(z)

# We stack x and y horizontally
w = np.hstack((x, y))
print(w)





