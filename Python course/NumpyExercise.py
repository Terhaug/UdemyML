import numpy as np

# Create an array of 10 zeros:
arr_Zeros = np.zeros(10)
print(arr_Zeros)
print('--------------------------------')

# Create an array fo 10 ones:
arr_ones = np.ones(10)
print(arr_ones)
print('--------------------------------')

# Create an array of 10 fives:
arr_fives = np.ones(10) * 5
print(arr_fives)
print('--------------------------------')

# Create an array of the integers from 10 to 50
tenToFifty = np.arange(10, 51)
print(tenToFifty)
print('--------------------------------')

# Create an array of all the even integers from 10 to 50
evenTenToFifty = np.arange(10, 51, 2)
print(evenTenToFifty)
print('--------------------------------')

# Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)
print(matrix)
print('--------------------------------')

# Create a 3x3 identity matrix:
IMatrix = np.eye(3)
print(IMatrix)
print('--------------------------------')

# Use NumPy to generate a random number between 0 and 1:
randN = np.random.rand(1)
print(randN)
print('--------------------------------')

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution:
randNu = np.random.randn(25)
print(randNu)
print(randNu.shape)
print('--------------------------------')

# Create a given matrix:(0.01 to 1)
givenMatrix = np.linspace(0.01, 1, 100).reshape(10, 10)
print(givenMatrix)
print(givenMatrix.shape)
print('--------------------------------')

# Create an array of 20 linearly spaced points between 0 and 1:
linArr = np.linspace(0, 1, 20)
print(linArr)

# Given matrix, grab chunk from 12 to 25:
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print('Answer: ')
print(mat[2:, 1:])
print('--------------------------------')

# From the same matrix rab the single 20 digit:
print(mat[3, 4])
print('--------------------------------')

# Get the sum of all the values in the matrix:
sum = mat.sum()
print(sum)
print('--------------------------------')

# Get the standard deviation of the values in the matrix:
std = mat.std()
print(std)
print('--------------------------------')

# Get the sum of all the columns in the matrix:
sumColums = mat.sum(axis=0)
print(sumColums)
print('--------------------------------')



