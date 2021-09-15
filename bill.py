import columns as columns
import inline as inline
import matplotlib as matplotlib
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_excel('bill.xlsx',)
print('Data read into a pandas dataframe!')

df = df.transpose()
print(df.head())

df_person = df.loc[['Lei', 'Fiby', 'Sharlo', 'Kevin', 'Abby'], 32]
print(df_person)
df_person.plot(kind='barh')
plt.show()