import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

d28 = pd.read_csv('./dataset/track1_d28.csv')

d28['Timestamp'] = pd.to_datetime(d28['Timestamp'])

d28['Hour'] = d28['Timestamp'].dt.hour
d28['Minute'] = d28['Timestamp'].dt.minute
d28['Second'] = d28['Timestamp'].dt.second

d28.head()

result_28 = {}
result_28

for i in range(0, 25):
    time_host_len = len(d28[d28['Hour'] == i]['Host'].unique())
    time_path_len = len(d28[d28['Hour'] == i]['Path'].unique())
    time_referer_len = len(d28[d28['Hour'] == i]['Referer'].unique())
    time_UA_len = len(d28[d28['Hour'] == i]['UA'].unique())
    result_28[i] = [time_host_len, time_path_len, time_referer_len, time_UA_len]

result_28
