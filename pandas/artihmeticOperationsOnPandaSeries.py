import pandas as pd

# Create a pandas series of the grocery items given in the list 'my_groceries'
fruits = pd.Series(data=[10, 6, 3,], index=['apples', 'oranges', 'bananas'])
print (fruits)

fruits + 2
print (fruits + 2)

fruits - 2
print (fruits - 2)

fruits * 2
print (fruits * 2)

fruits / 2
print (fruits / 2)


# We can also apply mathematical functions from NumPy, such as sqrt(x) to calculate the square root of each value in fruits.
import numpy as np

np.sqrt(fruits)
print (np.sqrt(fruits))

np.exp(fruits)
print (np.exp(fruits))

np.power(fruits,2)
print (np.power(fruits,2))

# We can also add Series together, which returns a third Series with the union of index pairs (all pairs of index 1 values are added together, all index 2 values, etc).
fruits['bananas'] + 2
print (fruits['bananas'] + 2)

fruits.iloc[0] - 2
print (fruits.iloc[0] - 2)

fruits.loc['oranges'] * 2
print (fruits.loc['oranges'] * 2)

fruits.loc['bananas'] / 2
print (fruits.loc['bananas'] / 2)

# We can also add two Series together, which returns a third Series with the union of index pairs (all pairs of index 1 values are added together, all index 2 values, etc).
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print (groceries)

# We can also add two Series together, which returns a third Series with the union of index pairs (all pairs of index 1 values are added together, all index 2 values, etc).
groceries * 2
print (groceries * 2)




