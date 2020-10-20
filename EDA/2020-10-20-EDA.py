import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv')
df['Timeindex'] = pd.to_datetime(df['Timestamp'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df.set_index('Timeindex', inplace=True)
df.head()
day = ['2020-08-24', '2020-08-25', '2020-08-26', '2020-08-27', '2020-08-28']
result = {}
mins = []
def ten_min_length():
    hour = [i for i in range(24)]
    min = {'start':[0,10,20,30,40,50], 'end':[9,19,29,39,49,59]}
    for h in hour:
        mins = []
        for m in range(6):
            x = len(df[f'2020-08-26 {h}:{min["start"][m]}':f'2020-08-26 {h}:{min["end"][m]}']['Host'].unique())
            mins.append(x)
            result[h] = mins
    return result


ten_min_length()

# hostGrouped = df.groupby('Host')
# funcAvgDifftime = lambda g:np.mean(g['Timestamp'].diff().dt.seconds.div(1, fill_value=0))
# funcStdDifftime = lambda g:np.std(g['Timestamp'].diff().dt.seconds.div(1, fill_value=0))
# avgDifftime = hostGrouped.apply(funcAvgDifftime)
# stdDifftime = hostGrouped.apply(funcStdDifftime)

test1 = df[f'{day[1]} 13:10' : f'{day[1]} 13:29']

hostGrouped = test1.groupby('Host')
funcAvgDifftime = lambda g:np.mean(g['Timestamp'].diff().dt.seconds.div(1, fill_value=0))
funcStdDifftime = lambda g:np.std(g['Timestamp'].diff().dt.seconds.div(1, fill_value=0))
avgDifftime = hostGrouped.apply(funcAvgDifftime)
stdDifftime = hostGrouped.apply(funcStdDifftime)

timediff = pd.concat([(hostGrouped['Timestamp'].count().rename('Count')), avgDifftime.rename('mean_diff_time'), stdDifftime.rename('std_diff_time')], axis=1)

timediff = timediff.sort_values(by='Count', ascending=False)


timediff.head(60)


test1[test1['Host'] == '208.128.121.60'].loc[:, ['Referer', 'Path', 'Payload']].head(40)
