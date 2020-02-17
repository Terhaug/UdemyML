# Linear Algebra Library
# Essisential for vectors and matrices


# Numpy-Arrays:
import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)
print('----------------------------------')

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = np.array(my_mat)
print(mat)
print('----------------------------------')

# Start, stop, stepzise
print(np.arange(0, 11, 2))
print('----------------------------------')

arrZero = np.zeros(3)
print(arrZero)
print('----------------------------------')

matZeroes = np.zeros((2, 3))
print(matZeroes)
print('----------------------------------')

linSpace = np.linspace(0, 5, 54)
print(linSpace)
print('----------------------------------')

# Identity-Matrix
I = np.eye(4)
print(I)
print('----------------------------------')

# One-dimentional
random = np.random.rand(5)
print(random)
print('----------------------------------')

# Two-dimentional
random = np.random.rand(5, 5)
print(random)
print('----------------------------------')

# Random number:
print(np.random.randn(2))
print('----------------------------------')

# 10 random integer from 1 to 100
print(np.random.randint(1, 100, 10))
print('----------------------------------')

arr = np.arange(25)
print(arr)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print('----------------------------------')

# Reshaping arr, need to fill out the range completely
arr = arr.reshape(5, 5)
print(arr)
print(arr.shape)

# Min and max of ranarr
print('Min: ' + str(ranarr.min()))
print('Max: ' + str(ranarr.max()))
print('Location of max: ' + str(ranarr.argmax()))
print('Location of min: ' + str(ranarr.argmin()))
print('----------------------------------')

# Inexing and Selection
arr = np.arange(0, 11)
# Printing values from index 0 to index 5
print(arr[:5])
# Printing from 4 up end:
print(arr[4:])
print('----------------------------------')

# Broadcasting
arr[0:5] = 100
print(arr)
arr = np.arange(0, 11)
slice_of_arr = arr[0:6]
print(slice_of_arr)
# Be aware that changes to sliced makes changes to actual array because of memory-complications
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)
print('----------------------------------')

# Use copy of array:
arr = np.arange(0, 11)
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
print(arr)
print('----------------------------------')

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
# Row indexed 1 and column indexed 0:
print(arr_2d[1, 0])

# Getting chunks of the array:
# Grav all colums from indexed 1 and up, and grap all rows up to indexed 2 (:rows, colums:
print(arr_2d[:2, 1:])
print('--------------------------------')

# Conditional selections:
arr = np.arange(1, 11)
print(arr)
bool_array = arr > 5
print(bool_array)
print('--------------------------------')
print('Printing only values bigger then 5: ')
print(arr[bool_array])

# Doing the same thing in one line:
print(arr[arr > 5])
print('--------------------------------')

# Grabbing chunks of bigger arrays:
arr_2d = np.arange(50).reshape(5, 10)
print(arr_2d)
print(arr_2d[1:4, 3:6])
print('--------------------------------')

# Operations:
arr = np.arange(0, 11)
print(arr)
# Adding, subtracting etc,,
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr + 100)
print(arr * 10)
print(arr ** 2)
print('--------------------------------')

# Array-functions:
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))









