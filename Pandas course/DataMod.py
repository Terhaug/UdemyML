import numpy as np
import pandas as pd

# Missing data:
d = {'A':[1, 2, np.nan], 'B':[5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
print('----------------------------------')

# Drop missing values:
# Dropping rows with missing values
print(df.dropna())
print('----------------------------------')

# Drop columns with missing values:
print(df.dropna(axis=1))
print('----------------------------------')

# Setting a threshold if you want rows/columns with a set am of values:
print(df.dropna(thresh=2))
print('----------------------------------')

# Fill values to missing value:
print(df.fillna(value='FILL VALUE'))
print(df.fillna(value=df['A'].mean()))
print('----------------------------------')

# Groupby:
# Allows you to group together rows based on columns:

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Tom', 'Amy', 'John', 'Bob', 'Emma'],
        'Sales': [200, 120, 340, 124, 243, 250]}

df2 = pd.DataFrame(data)
print(df2)
print('----------------------------------')

# Groupby-func.
byCompany = df2.groupby('Company')
print('Mean by company')
print(byCompany.mean())
print('----------------------------------')

print('Printing sum of company')
print(byCompany.sum())
print('----------------------------------')

# Finding sales-sum of FB:
print(byCompany.sum().loc['FB'])
print('----------------------------------')

# Typical oneliner:
print(df2.groupby('Company').sum().loc['FB'])
# Other methods such as count, max/min, and together with describe-method is useful
print('------------------------------------')


# Merging and joining
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

# Concatinating: Glues the df's together:
print(pd.concat([df1, df2, df3]))
print('------------------------------------')

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})


# Merging (Similare to SQL), merging on column key:
print(pd.merge(left, right, how='inner', on='key'))
print('------------------------------------')

# Joining ( Similare to SQL)
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                    index=['K0', 'K1', 'K2', 'K3'])

right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                    index=['K0', 'K1', 'K2', 'K3'])

print(left.join(right))
print('------------------------------------')

print(left.join(right, how='outer'))
print('------------------------------------')
