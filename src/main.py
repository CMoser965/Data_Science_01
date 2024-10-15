import pandas as pd
import numpy as np

df = pd.read_csv('dataset/generated/synthetic_manufacturing_data.csv')

df.isnull().sum()

df.dropna()
df.fillna(value=0)

df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])

df['Calculated_Duration'] = (df['End_Time'] - df['Start_Time']).dt.total_seconds() / 100

print(df)