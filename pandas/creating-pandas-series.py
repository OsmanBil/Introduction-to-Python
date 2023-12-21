import pandas as pd

# Create a pandas series of the grocery items given in the list 'my_groceries'
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print (groceries)   

# We can print information about a pandas Series in a similar fashion as a NumPy ndarray.
# We can print the shape of the Series, the index of the Series, the values of the Series, etc.
groceries.shape
print (groceries.shape)

# We can also check whether an index or value is part of a Series.
groceries.ndim
print (groceries.ndim)

# We can check the size of the Series, which is equivalent to the number of elements in the Series.
groceries.size
print (groceries.size)

# We can check the index of the Series.
groceries.index
print (groceries.index)

# We can print the values of the Series array.
groceries.values
print (groceries.values)

# We can check whether a value is in the Series.
'banana' in groceries
print ('banana' in groceries)

# We can also check whether a value is in a Series index.
'bread' in groceries
print ('bread' in groceries)