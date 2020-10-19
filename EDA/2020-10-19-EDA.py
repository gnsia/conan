import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv', index_col='Timestamp')
df.index = pd.to_datetime(df.index)


## 개별 호스트가 접근한 수가 꺾이는 포인트가 두군데 있다.
df['Host'].value_counts()[0:20].plot()
df['Host'].value_counts()[40:200].plot()
df['Host'].value_counts().head(200).mean()

### 2020-08-25 10시를 10분 단위로 슬라이싱하여 상위 두 개의 호스트를 뽑는다.

x0 = df['2020-08-25 10:00':'2020-08-25 10:09']['Host'].value_counts().head(2).index
y0 = df['2020-08-25 10:00':'2020-08-25 10:09']['Host'].value_counts().head(2)

x1 = df['2020-08-25 10:10':'2020-08-25 10:19']['Host'].value_counts().head(2).index
y1 = df['2020-08-25 10:10':'2020-08-25 10:19']['Host'].value_counts().head(2)

x2 = df['2020-08-25 10:20':'2020-08-25 10:29']['Host'].value_counts().head(2).index
y2 = df['2020-08-25 10:20':'2020-08-25 10:29']['Host'].value_counts().head(2)

x3 = df['2020-08-25 10:30':'2020-08-25 10:39']['Host'].value_counts().head(2).index
y3 = df['2020-08-25 10:30':'2020-08-25 10:39']['Host'].value_counts().head(2)

x4 = df['2020-08-25 10:40':'2020-08-25 10:49']['Host'].value_counts().head(2).index
y4 = df['2020-08-25 10:40':'2020-08-25 10:49']['Host'].value_counts().head(2)

x5 = df['2020-08-25 10:50':'2020-08-25 10:59']['Host'].value_counts().head(2).index
y5 = df['2020-08-25 10:50':'2020-08-25 10:59']['Host'].value_counts().head(2)



def subplo_six():
    plt.figure(figsize=(16,10))

    plt.subplot(3, 3, 1)
    plt.title('08-25 10:00~09')
    plt.ylim([0,5000])
    plt.bar(x0, y0)

    plt.subplot(3, 3, 2)
    plt.title('08-25 10:10~19')
    plt.ylim([0,5000])
    plt.bar(x1, y1)

    plt.subplot(3, 3, 3)
    plt.title('08-25 10:20~29')
    plt.ylim([0,5000])
    plt.bar(x2, y2)

    plt.subplot(3, 3, 4)
    plt.title('08-25 10:30~39')
    plt.ylim([0,5000])
    plt.bar(x3, y3)

    plt.subplot(3, 3, 5)
    plt.title('08-25 10:40~49')
    plt.ylim([0,5000])
    plt.bar(x4, y4)

    plt.subplot(3, 3, 6)
    plt.title('08-25 10:50~59')
    plt.ylim([0,5000])
    plt.bar(x5, y5)

    plt.show()

subplo_six()

df['Path'].value_counts()[0:5].plot()


x0 = df['2020-08-25 10:00':'2020-08-25 10:09']['Bytes'].value_counts().head(2).index
y0 = df['2020-08-25 10:00':'2020-08-25 10:09']['Bytes'].value_counts().head(2)

x1 = df['2020-08-25 10:10':'2020-08-25 10:19']['Bytes'].value_counts().head(2).index
y1 = df['2020-08-25 10:10':'2020-08-25 10:19']['Bytes'].value_counts().head(2)

x2 = df['2020-08-25 10:20':'2020-08-25 10:29']['Bytes'].value_counts().head(2).index
y2 = df['2020-08-25 10:20':'2020-08-25 10:29']['Bytes'].value_counts().head(2)

x3 = df['2020-08-25 10:30':'2020-08-25 10:39']['Bytes'].value_counts().head(2).index
y3 = df['2020-08-25 10:30':'2020-08-25 10:39']['Bytes'].value_counts().head(2)

x4 = df['2020-08-25 10:40':'2020-08-25 10:49']['Bytes'].value_counts().head(2).index
y4 = df['2020-08-25 10:40':'2020-08-25 10:49']['Bytes'].value_counts().head(2)

x5 = df['2020-08-25 10:50':'2020-08-25 10:59']['Bytes'].value_counts().head(2).index
y5 = df['2020-08-25 10:50':'2020-08-25 10:59']['Bytes'].value_counts().head(2)



def subplo_six():
    plt.figure(figsize=(16,10))

    plt.subplot(3, 3, 1)
    plt.title('08-25 10:00~09')
    plt.ylim([0,5000])
    plt.bar(x0, y0)

    plt.subplot(3, 3, 2)
    plt.title('08-25 10:10~19')
    plt.ylim([0,5000])
    plt.bar(x1, y1)

    plt.subplot(3, 3, 3)
    plt.title('08-25 10:20~29')
    plt.ylim([0,5000])
    plt.bar(x2, y2)

    plt.subplot(3, 3, 4)
    plt.title('08-25 10:30~39')
    plt.ylim([0,5000])
    plt.bar(x3, y3)

    plt.subplot(3, 3, 5)
    plt.title('08-25 10:40~49')
    plt.ylim([0,5000])
    plt.bar(x4, y4)

    plt.subplot(3, 3, 6)
    plt.title('08-25 10:50~59')
    plt.ylim([0,5000])
    plt.bar(x5, y5)

    plt.show()

subplo_six()








normal_log = log.loc[log.Status.astype(str).str.isnumeric(), :].copy()


### df에서 host컬럼을 이용해 이상치 제거
log = df.loc[df.Status.astype(str).str.isnumeric(), :].copy()
len(df)
len(log)

### 줄어든 UA 수
len(df['UA'].unique())
len(log['UA'].unique())

### UA에서 가장 빈도수가 높은 UA부터 정렬
UA_sort = log['UA'].value_counts().index

### 해당 UA의 이름과 수량
UA_sort[0]
len(log[log['UA'] == UA_sort[0]])

### 해당 UA가 접근한 파일
log[log['UA'] == UA_sort[0]]['Referer'].value_counts()

### 해당 UA가 사용한 통신방식

log[log['UA'] == UA_sort[0]]['Protocol'].value_counts()



### 해당 UA를 이용한 Host
log[log['UA'] == UA_sort[0]]['Host'].value_counts()


log[log['UA'] == UA_sort[0]].value_counts()


log[log['UA'] == UA_sort[1]]




plt.figure(figsize=(16,9))
plt.bar()

df.index
