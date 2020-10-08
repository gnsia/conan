import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

d24 = pd.read_csv('./dataset/track1_d24.csv')

d24.tail()


d24['Timestamp'] = pd.to_datetime(d24['Timestamp'])

d24['Hour'] = d24['Timestamp'].dt.hour
d24['Minute'] = d24['Timestamp'].dt.minute
d24['Second'] = d24['Timestamp'].dt.second

############################################################

# 08-24 10시에 접근한 IP중 유난히 접근이 많은 분때
# result = []
result = {}

for i in range(10, 21):
    time_host_len = len(d24[d24['Hour'] == i]['Host'].unique())
    time_path_len = len(d24[d24['Hour'] == i]['Path'].unique())
    time_referer_len = len(d24[d24['Hour'] == i]['Referer'].unique())
    time_UA_len = len(d24[d24['Hour'] == i]['UA'].unique())
    time_Minute_len = d24[d24['Hour'] == i]['Minute'].value_counts().index[0]
    result[i] = [time_host_len, time_path_len, time_referer_len, time_UA_len, time_Minute_len]

result


plt.scatter(d24[d24['Hour'] == 10]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 10]['Minute'].value_counts().sort_index().index)
len(d24[d24['Hour'] == 10]['Host'].unique())
len(d24[d24['Hour'] == 10]['Path'].unique())
len(d24[d24['Hour'] == 10]['Referer'].unique())

# 08-24 11시에 접근한 IP중 유난히 접근이 많은 분때

plt.scatter(d24[d24['Hour'] == 11]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 11]['Minute'].value_counts().sort_index().index)
len(d24[d24['Hour'] == 11]['Host'].unique())
# 08-24 11시에 접근한 IP중 유난히 접근이 많은 분때

plt.scatter(d24[d24['Hour'] == 12]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 12]['Minute'].value_counts().sort_index().index)
len(d24[d24['Hour'] == 12]['Host'].unique())
# 08-24 11시에 접근한 IP중 유난히 접근이 많은 분때

plt.scatter(d24[d24['Hour'] == 13]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 13]['Minute'].value_counts().sort_index().index)
len(d24[d24['Hour'] == 13]['Host'].unique())
# 08-24 11시에 접근한 IP중 유난히 접근이 많은 분때

plt.scatter(d24[d24['Hour'] == 14]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 14]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 14]['Host'].unique())
# 08-24 11시에 접근한 IP중 유난히 접근이 많은 분때

plt.scatter(d24[d24['Hour'] == 15]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 15]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 15]['Host'].unique())
# 08-24 11시에 접근한 IP중 유난히 접근이 많은 분때

plt.scatter(d24[d24['Hour'] == 16]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 16]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 16]['Host'].unique())

plt.scatter(d24[d24['Hour'] == 17]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 17]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 17]['Host'].unique())



plt.scatter(d24[d24['Hour'] == 18]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 18]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 18]['Host'].unique())

plt.scatter(d24[d24['Hour'] == 19]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 19]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 19]['Host'].unique())

plt.scatter(d24[d24['Hour'] == 20]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 20]['Minute'].value_counts().sort_index().index)

len(d24[d24['Hour'] == 20]['Host'].unique())

plt.scatter(d24[d24['Hour'] == 21]['Minute'].value_counts().sort_index(), d24[d24['Hour'] == 21]['Minute'].value_counts().sort_index().index)

############################################################
