import numpy as np

# boolean indexing

x = np.arange(1, 21).reshape(4, 5)
print(x)

# We print x greater than 10
print (x[x > 10])

# We print x less than or equal to 7
print (x[x <= 7])

# we print x between 10 and 17
print (x[(x>10) & (x<17)])

# We print x greater than 10 but less than or equal to 17
x[(x>10) & (x<17)] = -1
print(x)


# set operations
x = np.array([1,2,3,4,5])
y = np.array([6,7,2,8,4])

print(np.intersect1d(x,y))
print(np.setdiff1d(x,y))
print(np.union1d(x,y))


# sorting

x = np.random.randint(1,11,size=(10,))
print(x)

print(np.sort(x))
print(x)