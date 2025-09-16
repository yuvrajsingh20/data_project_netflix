# To install numpy, run: pip install numpy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('D:\project\mymoviedb.csv', lineterminator='\n')
print(df.describe())

df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
print(df['Release_Date'].dtype)
df['Release_Date'] = df['Release_Date'].dt.year
print(df['Release_Date'])

# drop columns which are not required

cols=['Overview', 'Original_Language', 'Poster_Url']
df.drop(cols, axis = 1,  inplace=True)
df.columns
print(df.head())


def catezories_colo(de, col, lables):
    