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
