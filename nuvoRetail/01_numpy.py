import numpy as np

# 1. Initializing Numpy Array
mat_A = np.array([
    [
        [1,2,3,2],
        [1,2,3,2],
        [1,2,3,2],
    ],
    [
        [1,2,3,1],
        [1,2,3,1],
        [1,2,3,1],
    ],
], dtype=np.float32)

# print(mat_A)

# print(mat_A.shape, mat_A.ndim)

# print(mat_A.size) # Total Number of Elements

# print(mat_A.dtype)

# print(mat_A[0,2,2])

# 2. Filling Numpy Arrays

a = np.full((3,2,2),1)

a = np.zeros((3,2,2))

a = np.ones((3,2,2))

a = np.empty((3,3,1)) 
# It initializes the numpy array with the value in the memmory (garbage). It is little faster than np.zeros or np.ones because it does not have to assign the value in numpy in RAM. It takes the values present in memory as is

# print(a)

# arange function --> arange the values with a fixed spacing
x_values = np.arange(2, 10, 2)
# print(x_values)

# linspace function --> Give the n values with Linear Spacing
x_values = np.linspace(2, 10, 3) # Here 3 --> number values to get in an array
# print(x_values)


# 3. nan, inf --> Null and Infinite

# print(f"np.nan --> {np.nan}")
# print(f"np.inf --> {np.inf}")

# print(np.isnan(np.nan))


# print(np.isnan(np.sqrt(-1)))

# print(np.isinf(np.inf))

# print(np.isinf(np.array([10])[0] /0))
# print(np.isinf(np.array([10,0]) /0))

# 4. Mathematical Operation with Numpy

l1 = np.array([1,2,3,4])
l2 = np.array([
    [1],
    [2]
])

# print(l1 + l2)
# print(l1 * l2)
# print(l1 - l2)
# print(l1 / l2)

# print(np.sin(l1))
# print(np.tan(l1))
# print(np.log10(l1))
# print(np.log(l1))

# 5. Numpy Array Methods

a = np.array([1,2,3])


a = np.append(a, [7,8,9])

a = np.insert(a, 3,[4,5,6])

# print(a)

b = np.array([
    [1,2,3],
    [4,5,6],
])

# print(np.delete(b,1))
# print(np.delete(b,3))
# print(np.delete(b,5))

# print(np.delete(b,1,0))  # 3rd parameter is axis --> If 0 remove row
# print(np.delete(b,1,1))  # 3rd parameter is axis --> If 1 remove column

# 6. Structuring Function

a = np.array([
    [1,2,3,4],
    [1,2,3,4],
])

# print(a.shape)

# print(a.reshape((4,2)))
# print(a.reshape((2,2,2)))

# print(a.shape)

# a.resize(4,2) # It is same as reshape but it apply it permanently

# print(a)

# print(a.flatten()) # It return a copy of flattened data
# print(a.ravel()) # It gives the view and it will be linked with the prev np array

# var = a.ravel()

# var[1] = 1000

# print(a) #

# print(var) # Var is linekd to a --> np array


# print(a.T)
# print(a.transpose())

# print(a.swapaxes(0,1)) #--> Same effect as T but it effective in lage dim np array to swap only a certain axes


# 7. Concatenating, Stacking, Splitting

a1 = np.array([
    [1,2,3],
    [4,5,6],
])

a2 = np.array([
    [4,5,6],
    [7,8,9],
])

# print(np.concatenate((a1,a2),axis=0)) # o --> for rows
# print(np.concatenate((a1,a2),axis=1)) # o --> for columns

# print(np.stack((a1,a2)))

# print(np.vstack((a1,a2))) # same as concatenate for axis = 0
# print(np.hstack((a1,a2))) # same as concatenate for axis = 1

a3 = np.array([
    [1,2,3,4,],
    [1,2,3,4,],
    [1,2,3,4,],
    [1,2,3,4,],
])

# print(np.split(a3, 2, axis=0)) # axis = 0 --> Splitting Row wise
# print(np.split(a3, 2, axis=1)) # axis = 0 --> Splitting Column wise

# print(np.resize(np.arange(1,17,1),(4,4)))


# 8. Aggregate Function

# print(a3.min())
# print(a3.max())
# print(a3.mean())
# print(a3.sum())
# print(np.median(a3))

value, count = np.unique(a3, return_counts=True)

# print(value,count)

# 9. Numpy Random

number = np.random.randint(100)

# Random integer
numbers = np.random.randint(2, 10, size=(2,2,4))

# Binomial Distribution --> 10 --> 0 - 10 | p --> probability | size --> size of Numpy Array 
numbers = np.random.binomial(10, p=0.5, size=(3,4))

# Normal Distribution --> loc --> mean | scale --> Standard Deviation
numbers = np.random.normal(loc=100, scale=3, size=(3,4))

# Random Choices 
numbers = np.random.choice([1,2,3,4], size=(2,4))

print(numbers)


