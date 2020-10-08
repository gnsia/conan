import pandas as pd
import numpy as np
import datetime as dt

df = pd.read_csv('./dataset/track1.csv')

########################################

# pattern을 찾기 위해 Timestamp를 쪼개는 방식

########################################


df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df.info()

df['Date'] = df['Timestamp'].dt.date
df['Date'].value_counts().sort_index()

d24 = df[df['Date'] == df['Date'].value_counts().sort_index().index[0]]
d24.to_csv('./dataset/track1_d24.csv')

d25 = df[df['Date'] == df['Date'].value_counts().sort_index().index[1]]
d25.to_csv('./dataset/track1_d25.csv')

d26 = df[df['Date'] == df['Date'].value_counts().sort_index().index[2]]
d26.to_csv('./dataset/track1_d26.csv')

d27 = df[df['Date'] == df['Date'].value_counts().sort_index().index[3]]
d27.to_csv('./dataset/track1_d27.csv')

d28 = df[df['Date'] == df['Date'].value_counts().sort_index().index[4]]
d28.to_csv('./dataset/track1_d28.csv')
