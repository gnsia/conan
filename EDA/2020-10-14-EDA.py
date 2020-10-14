import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv', index_col='Timestamp')
df.index = pd.to_datetime(df.index)

len(df['UA'][9].split(' '))
df['UA_1'] = df['UA'].str.split(' ').str[0]
df['UA_2'] = df['UA'].str.split(' ').str[-3]
df['UA_3'] = df['UA'].str.split(' ').str[-2]
df['UA_4'] = df['UA'].str.split(' ').str[-1]
df[['UA_1','UA_2','UA_3','UA_4']]

df['OS_1'] = df['UA'].str.split('(').str[1]
df['OS'] = df['OS_1'].str.split(')').str[0]

df['OS'].unique()

date = ['2020-08-24', '2020-08-25', '2020-08-26', '2020-08-27', '2020-08-28']

moz_5 = []
opera_9_8 = []
moz_4 = []
py_xml = []
win = []
mac = []
linux = []
chrome = []
safari = []

for i in date:
    x = len(df[i:i][df[i:i]['UA'].str.contains('Safari', na=False)])
    safari.append(x)


win
mac
linux
chrome
safari

plt.figure(figsize=(16,9))
# plt.plot(date, moz_5, label='Mozilla/5.0')
plt.plot(date, win, label='Windows')
plt.plot(date, mac, label='Mac')
plt.plot(date, linux, label='Linux')
plt.plot(date, chrome, label='Linux')
plt.plot(date, safari, label='Linux')
plt.legend()
plt.show()
