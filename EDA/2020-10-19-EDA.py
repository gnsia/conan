import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv', index_col='Timestamp')
df.index = pd.to_datetime(df.index)


## 개별 호스트가 접근한 수가 꺾이는 포인트가 두군데 있다.
df['Host'].value_counts()[0:200].plot()
df['Host'].value_counts()[40:300].plot()
df['Host'].value_counts().head().mean()

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

### 함수 만들기

def subplo(day, host, tick):
    d = int(day) # 24~28 일까지 중 선택
    host = int(host) # 몇 개의 아이피를 표시할지 선택
    hour = [i for i in range(24)]
    min = {'start':[0,10,20,30,40,50], 'end':[9,19,29,39,49,59]}
    for h in hour:
        plt.figure(figsize=(20,11))
        print(f'2020-08-{d} {h}시')
        for m, n in zip(range(len(min["end"])), range(1,7)):
            # print(m, n)
            x = df[f'2020-08-{d} {hour[h]}:{min["start"][m]}':f'2020-08-{d} {hour[h]}:{min["end"][m]}']['Host'].value_counts().head(host).index
            y = df[f'2020-08-{d} {hour[h]}:{min["start"][m]}':f'2020-08-{d} {hour[h]}:{min["end"][m]}']['Host'].value_counts().head(host)
            plt.subplot(3, 3, n)
            plt.title(f'08-{d} {h}:{min["start"][m]}~{min["end"][m]}')
            plt.ylim([0,tick]) # 확인하고 싶은 y축 크기를 선택
            plt.bar(x, y)
        plt.show()

subplo(27, 3, 1000)




def subplo2(day, host, tick):
    d = int(day) # 24~28 일 중에 원하는 날짜를 입력
    host = int(host) # 원하는 호스트 갯수 입력
    hour = [i for i in range(24)]
    min = {'start':[0,10,20,30,40,50], 'end':[9,19,29,39,49,59]}
    for h in hour:
        plt.figure(figsize=(16,10))
        print(f'2020-08-{d} {h}시')
        for m, n in zip(range(len(min["end"])), range(1,7)):
            # print(m, n)
            host_x = df[f'2020-08-{d} {hour[h]}:{min["start"][m]}':f'2020-08-{d} {hour[h]}:{min["end"][m]}']['Host'].value_counts().head(host).index
            host_y = df[f'2020-08-{d} {hour[h]}:{min["start"][m]}':f'2020-08-{d} {hour[h]}:{min["end"][m]}']['Host'].value_counts().head(host)
            # x = df[f'2020-08-{d} {hour[h]}:{min["start"][m]}':f'2020-08-{d} {hour[h]}:{min["end"][m]}']['Host'].value_counts().head(host).index
            # y = df[f'2020-08-{d} {hour[h]}:{min["start"][m]}':f'2020-08-{d} {hour[h]}:{min["end"][m]}']['Host'].value_counts().head(host)
            plt.subplot(3, 3, n)
            plt.title(f'08-{d} {h}:{min["start"][m]}~{min["end"][m]}')
            plt.xticks(rotation = 45)
            plt.ylim([0,tick]) # 원하는 Y값 범위 입력
            # plt.margins(0.2)
            plt.tight_layout()
            plt.bar(host_x, host_y)
        plt.show()

subplo2(27, 10, 1000)

host_x
