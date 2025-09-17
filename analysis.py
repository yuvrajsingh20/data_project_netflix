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


def classify_rating(vote_average):
    """
    Convert a numeric rating (0–100) into a label.
    - 0–25%   → "Not Interested"
    - 26–50% → "Average"
    - 51–75% → "Good"
    - 76–100 → "Likable"
    """
    if vote_average <= 25:
        return "Not Interested"
    elif vote_average <= 50:
        return "Average"
    elif vote_average <= 75:
        return "Good"
    else:
        return "Likable"

    