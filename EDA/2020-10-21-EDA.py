import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv', index_col='Timestamp')
df.index = pd.to_datetime(df.index)
pd.set_option('display.max_row', 100)


df[df['UA'] == "wp.hotpost.kr"]


def min_1(day, hour):
    result = {}
    ano = {}
    ano_min = []
    for i in range(60):
        x = len(df[f'2020-08-{day} {hour}:{i}'])
        result[i] = x
        if x > 1000:
            ano_min.append(i)
            ano[hour] = ano_min
    x = result.keys()
    # y = result.values()
    # plt.figure(figsize=(12,8))
    # plt.title(f'date : {day}, hour : {hour}')
    # plt.ylim(0,1000)
    # plt.bar(x, y)
    # plt.show()
    print(ano)

### 1분당 1000번 이상 접근한 시간들
###################################################################24일

for i in range(10, 24):
    min_1(24, i)

## 1000이 넘지 않는 대조군 시간대와 1000이 넘는 시간대를 묶어둔다.
d24_ano1 = df['2020-08-24 10:41']
d24_ano2 = df['2020-08-24 10:42']
d24_ano3 = df['2020-08-24 16:31']
d24_no1 = df['2020-08-24 10:40'] ## 1000번 넘는 접근이 있기 바로 직전
d24_no2 = df['2020-08-24 14:14'] ## 무작위로 선정한 시간
d24_no3 = df['2020-08-24 18:30'] ## 무작위로 선정한 시간

### 동일한 호스트가 혼자서 1000번이 넘는 접근을 시도했다.
d24_ano1['Host'].value_counts().head(3)

d24_ano2['Host'].value_counts().head(3)

d24_ano3['Host'].value_counts().head(3)

## 바로 직전 시간대에도 동일한 아이피의 접근이라는 것을 알 수 있다.

d24_no1['Host'].value_counts().head(3)

d24_no2['Host'].value_counts().head(3)

d24_no3['Host'].value_counts().head(3)

df[df['Host'] == '101.224.32.28'] # 24일만 활동하는 것이 아닌 27일까지 다양한 시간대 접근을 시도한다.


#########################################################################25일


for i in range(24):
    min_1(25, i)

### 단 3분만에 단일 호스트가 9000번이 넘는 접근을 시도했다.
df['2020-08-25 10:19':'2020-08-25 10:21']['Host'].value_counts()


df[df['Host'] == '231.211.11.16'] ## 25일 하루동안 여기저기서 등장할 예정이다.

## 단일 UA를 사용했다.
df[df['Host'] == '231.211.11.16']['UA'].value_counts()

df[df['Host'] == '231.211.11.16']['Bytes'].max()
df[df['Host'] == '231.211.11.16']['Bytes'].min()
df[df['Host'] == '231.211.11.16']['Bytes'].mean()
df[df['Host'] == '231.211.11.16']['Bytes'].median()


#######################################################################################
for i in range(24):
    min_1(26, i)
for i in range(24):
    min_1(27, i)
for i in range(19):
    min_1(28, i)

df['2020-08-24 10:']
