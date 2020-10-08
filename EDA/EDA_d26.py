import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

d26 = pd.read_csv('./dataset/track1_d26.csv')

d26['Timestamp'] = pd.to_datetime(d26['Timestamp'])

d26['Hour'] = d26['Timestamp'].dt.hour
d26['Minute'] = d26['Timestamp'].dt.minute
d26['Second'] = d26['Timestamp'].dt.second

d26.head()

result_26 = {}
result_26

for i in range(0, 25):
    time_host_len = len(d26[d26['Hour'] == i]['Host'].unique())
    time_path_len = len(d26[d26['Hour'] == i]['Path'].unique())
    time_referer_len = len(d26[d26['Hour'] == i]['Referer'].unique())
    time_UA_len = len(d26[d26['Hour'] == i]['UA'].unique())
    result_26[i] = [time_host_len, time_path_len, time_referer_len, time_UA_len]

result_26
