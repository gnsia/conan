import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv')

########################################

# pattern을 찾기 위해 Timestamp를 쪼개는 방식

########################################


df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
df['Minute'] = df['Timestamp'].dt.minute
df['Second'] = df['Timestamp'].dt.second

df.head()

df['Day'].unique()
df[df['Day'] == 24]['Hour'].unique()
df[df['Day'] == 25]['Hour'].unique()
df[df['Day'] == 26]['Hour'].unique()
df[df['Day'] == 27]['Hour'].unique()
df[df['Day'] == 28]['Hour'].unique()

df[(df['Day'] == 24) & (df['Hour'] == 10) & (df['Minute'] == 00) & (df['Second'] < 60)]['Host'].value_counts()

day = 24
hour = 10
result = {}
for i in df[(df['Day'] == day) & (df['Hour'] == hour)]['Minute'].unique():
    x = df[(df['Day'] == day) & (df['Hour'] == hour) & (df['Minute'] == i)]['Host'].value_counts().index[0]
    result[i] = [x]



result
result.values()
