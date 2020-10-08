import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

d25 = pd.read_csv('./dataset/track1_d25.csv')

d25['Timestamp'] = pd.to_datetime(d25['Timestamp'])

d25['Hour'] = d25['Timestamp'].dt.hour
d25['Minute'] = d25['Timestamp'].dt.minute
d25['Second'] = d25['Timestamp'].dt.second

d25.head()

result_25 = {}
result_25

for i in range(0, 25):
    time_host_len = len(d25[d25['Hour'] == i]['Host'].unique())
    time_path_len = len(d25[d25['Hour'] == i]['Path'].unique())
    time_referer_len = len(d25[d25['Hour'] == i]['Referer'].unique())
    time_UA_len = len(d25[d25['Hour'] == i]['UA'].unique())
    result_25[i] = [time_host_len, time_path_len, time_referer_len, time_UA_len]

result_25
