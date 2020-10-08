import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

d27 = pd.read_csv('./dataset/track1_d27.csv')

d27['Timestamp'] = pd.to_datetime(d27['Timestamp'])

d27['Hour'] = d27['Timestamp'].dt.hour
d27['Minute'] = d27['Timestamp'].dt.minute
d27['Second'] = d27['Timestamp'].dt.second

d27.head()

result_27 = {}
result_27

for i in range(0, 25):
    time_host_len = len(d27[d27['Hour'] == i]['Host'].unique())
    time_path_len = len(d27[d27['Hour'] == i]['Path'].unique())
    time_referer_len = len(d27[d27['Hour'] == i]['Referer'].unique())
    time_UA_len = len(d27[d27['Hour'] == i]['UA'].unique())
    result_27[i] = [time_host_len, time_path_len, time_referer_len, time_UA_len]

result_27
