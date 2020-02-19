# Pandas - DataFrames:
import numpy as np
import pandas as pd
from numpy.random import randn

rs = np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print('Printing out DataFrame:')
print(df)
print('-----------------------------------------')

print('Printing out first column: ')
print(df['W'])
print('-----------------------------------------')

df['new'] = df['W'] + df['Y']
print('Created new column')
print(df)
print('-----------------------------------------')

# Need to set axis and inplace = True.
# This also works for rows, however the axis needs to be set to 0
df.drop('new', axis=1, inplace=True)
print('Deleted the new column')
print(df)
print('-----------------------------------------')

# Selecting rows:
row1 = df.loc['A']
row1_ = df.iloc[0]
print('Selecting first row in 2 ways: ')
print(row1)
print(row1_)
print('-----------------------------------------')

# Conditional selection (Similare to NumPy):
boolser = df > 0
print('DataFrame > 0: ')
print(boolser)
print('-----------------------------------------')

# Result of colum W > 0 is every line except C, showing Y and X colums:
# Also works with multiple condition, but use '&' instead of 'and'
GreaterThenZero = df[df['W'] > 0][['Y', 'X']]
print(GreaterThenZero)
print('-----------------------------------------')

newind = 'AU OS TR FI RO'.split()
print(newind)
df['States'] = newind
print(df)
print('-----------------------------------------')

# Setting states as index. (To do save this to memory set inplace = True
print(df.set_index('States'))
print('-----------------------------------------')

# Index-hierarchy
outside = ('G1 G1 G1 G2 G2 G2').split()
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
print('-----------------------------------------')

# Creating multi-index dataFrame
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)
print('-----------------------------------------')

# Grabbing from the dataframe
print(df.loc['G1'].loc[1])
print('-----------------------------------------')
print(df.loc['G2'].loc[2]['B'])
print('-----------------------------------------')

# Labeling the indexations:
labeled_index = df.index.names = ['Groups', 'Num']
print(df)
print('-----------------------------------------')

# Using cross-section(xs) instead of locate can cross-grabbing abit easier
# Grabbing the rows where num-rows
print(df.xs(1, level='Num'))
print('-----------------------------------------')




