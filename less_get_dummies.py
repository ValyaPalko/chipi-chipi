import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:")
print(data.head())
unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)
print("\nDataFrame с one-hot encoding:")
print(data.head())
