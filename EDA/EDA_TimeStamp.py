import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv', index_col='Timestamp')

df.head(1)
df.index = pd.to_datetime(df.index)

df.index[0]
