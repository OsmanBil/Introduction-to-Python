import numpy as np

# create a rank 2 ndarray of random integers between 0 and 5000 inclusive with 1000 rows and 20 colums.

X = np.random.randint(0, 5001, size=(1000, 20))

# print the shape of X
print(X.shape)

# Average of the values in each column of X
ave_cols = np.mean(X, axis=0)

# Standard Deviation of the values in each column of X
std_cols = np.std(X, axis=0)

# Print the shape of ave_cols
print("The shape of ave_cols is: ", ave_cols.shape)

# Print the shape of std_cols
print("The shape of std_cols is: ", std_cols.shape)

# Mean normalize X
X_norm = (X - ave_cols) / std_cols

# Print the average of all the values of X_norm
# You can use either the function or a method. So, there are multiple ways to solve. 
print("The average of all the values of X_norm is: ")
print(np.mean(X_norm))
print(X_norm.mean())

# Print the average of the minimum value in each column of X_norm
print("The average of the minimum value in each column of X_norm is: ")
print(X_norm.min(axis = 0).mean())
print(np.mean(np.sort(X_norm, axis=0)[0]))

# Print the average of the maximum value in each column of X_norm
print("The average of the maximum value in each column of X_norm is: ")
print(np.mean(np.sort(X_norm, axis=0)[-1]))
print(X_norm.max(axis = 0).mean())

# We create a random permutation of integers 0 to 4
np.random.permutation(5)

# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
row_indices = np.random.permutation(X_norm.shape[0])

# Make any necessary calculations.
# You can save your calculations into variables to use later.

# You have to extract the number of rows in each set using row_indices.
# Note that the row_indices are random integers in a 1-D array. 
# Hence, if you use row_indices for slicing, it will NOT give the correct result.

# Let's get the count of 60% rows. Since, len(X_norm) has a lenght 1000, therefore, 60% = 600
sixty = int(len(X_norm) * 0.6)

# Let's get the count of 80% rows
eighty = int(len(X_norm) * 0.8)

# Create a Training Set
# Here row_indices[:sixty] will give you first 600 values, e.g., [93 255 976 505 281 292 977,.....]
# Those 600 values will will be random, because row_indices is a 1-D array of random integers.
# Next, extract all rows represented by these 600 indices, as X_norm[row_indices[:sixty], :]
X_train = X_norm[row_indices[:sixty], :]

# Create a Cross Validation Set
X_crossVal = X_norm[row_indices[sixty: eighty], :]

# Create a Test Set
X_test = X_norm[row_indices[eighty: ], :]

# Print the shape of X_train
print(X_train.shape)

# Print the shape of X_crossVal
print(X_crossVal.shape)

# Print the shape of X_test
print(X_test.shape)

