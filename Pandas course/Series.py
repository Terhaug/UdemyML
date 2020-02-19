# Pandas!
# - Is a one source library built on NumPy.
# - It has built in visualization features.
# - Works with data from a wide variety of sources.
import numpy as np
import pandas as pd

# Series using pandas:
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

# my_series = pd.Series(data=my_data, index=labels)
my_series = pd.Series(data=my_data, index=labels)
print(my_series)
print('-----------------------------')

my_series = pd.Series(arr, labels)
print(arr)
print(my_series)
print('-----------------------------')

my_series = pd.Series(d)
print(d)
print(my_series)
print('-----------------------------')

# Using the series:
ser1 = pd.Series([1, 2, 3, 4], ['Norway', 'Sweden', 'Denmark', 'England'])
print(ser1)
print('-----------------------------')

ser2 = pd.Series([1, 2, 5, 4], ['Norway', 'Sweden', 'Italy', 'England'])
print(ser2)
print('Norway is indexed at', ser1['Norway'])
print('-----------------------------')

# Not matched = NaN, and turns to float to withold all information
sum_series = ser1 + ser2
print(sum_series)



