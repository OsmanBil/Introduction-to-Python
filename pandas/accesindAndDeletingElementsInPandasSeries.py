import pandas as pd

# Create a pandas series of the grocery items given in the list 'my_groceries'
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print (groceries)

# We access elements in a Series in similar ways as we would in NumPy ndarrays.
groceries['eggs']
print (groceries['eggs'])

# We can also access multiple elements in a Series in similar ways as we would in NumPy ndarrays.
groceries[['milk', 'bread']]
print (groceries[['milk', 'bread']])

# We can use loc attribute to access elements in a Series.
#groceries[0]
#print (groceries[0])

# We can access multiple elements in a Series using loc attribute.
groceries.loc[['eggs', 'apples']]
print (groceries.loc[['eggs', 'apples']])

# We can also access elements in a Series using numerical indices.
groceries.iloc[[2, 3]]
print (groceries.iloc[[2, 3]])

# We can modify an existing element in a Series.
groceries['eggs'] = 2
print (groceries['eggs'])

# We can also delete items from a Series inplace without having to reassign the Series to a new variable.
groceries.drop('apples')
print (groceries.drop('apples'))

