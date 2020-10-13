##############################################

# 1. 딱 한번만 접근한 IP주소는 정상행위로 가정한다.
# 2. 특정 분(minute)에서 가장 많이 접근한 IP주소와 두번째로 많이 접근한 IP주소가 100번 넘게 차이나면
# 가장 많이 접근한 IP주소를 이상접근으로 가정한다.
# 3. UA에 기본 브라우저가 아닌 라이브러리 및 스크립트로 접근
# 4. Referer가 "-"로 되어있는 모든 데이터
##############################################


import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv')
df.head(1)
df.info()

# Timestamp 나누기

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Date'] = df['Timestamp'].dt.date
df['Hour'] = df['Timestamp'].dt.hour
df['Min'] = df['Timestamp'].dt.minute
df['Sec'] = df['Timestamp'].dt.second


# Host 별 접근 통계

df.Host.value_counts().mean()
df.Host.value_counts().median()
df.Host.value_counts().max()
df.Host.value_counts().min()

# 전송량 통계

df.Bytes.mean()
df.Bytes.median()
df.Bytes.max()
df.Bytes.min()

# Referer가 "-" 로 찍힌 데이터
rf_mask = df['Referer'].str.contains('"-"')
df[rf_mask.fillna(False)]['Host'].value_counts()


# Referer가 "-"로 찍힌 놈들이 다녀간 Referer
df[df['Host'] == df[rf_mask.fillna(False)]['Host'].value_counts().index[4]]['Referer'].value_counts()

# Referer가 "-"로 찍힌 놈들이 다녀간 Path
df[df['Host'] == df[rf_mask.fillna(False)]['Host'].value_counts().index[4]]['Path'].value_counts()

# Referer가 "-"로 찍힌 놈들이 사용한 UA
df[df['Host'] == df[rf_mask.fillna(False)]['Host'].value_counts().index[4]]['UA'].value_counts()

# Referer가 "-"로 찍힌 놈들이 다녀간 날짜와 시간
df[df['Host'] == df[rf_mask.fillna(False)]['Host'].value_counts().index[4]]['Date'].value_counts()
df[df['Host'] == df[rf_mask.fillna(False)]['Host'].value_counts().index[4]]['Hour'].value_counts().sort_index()



host_counts = pd.DataFrame(df.Host.value_counts())
host_counts[host_counts['Host'] > 1000].plot()

df[df['Host'] == host_counts[host_counts['Host'] > 3000].index[-1]]['Hour'].value_counts().sort_index()

df[df['Referer'] == '"']['Host'].value_counts()


##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########
##########################################날짜별로 나누기#########


d = []
for i in range(len(df['Date'].unique())):
    x = df[df['Date'] == df['Date'].unique()[i]]
    d.append(x)

# 8/24 분석

len(d[0]['Hour'].value_counts().sort_index())
d[0]['Hour'].unique()
d[0][d[0]['Hour'] == d[0]['Hour'].unique()[0]]


def subplott():
    plt.figure(figsize=(20,20))
    for i in range(1,11):
        plt.subplot(12,1,i)
        plt.plot(d[0][d[0]['Hour'] == d[0]['Hour'].unique()[i]]['Min'].value_counts().sort_index())
        plt.title("f{i}")
        plt.grid()
    plt.show()

subplott()















##########################################################


d[1]['Host'].value_counts()

d[1]['Hour'].value_counts().sort_index().plot()

####################################################################

d[2]['Host'].value_counts()

d[2]['Hour'].value_counts().sort_index().plot()

################################################################

d[3]['Host'].value_counts()
d[3]['Hour'].value_counts().sort_index().plot()
############################################################

d[4]['Host'].value_counts()
d[4]['Hour'].value_counts().sort_index().plot()



plt.figure(figsize=(10,10))
plt.title("good")
plt.xlabel('min')
plt.ylabel('sec')
plt.scatter(X, Y, c='black', marker='o')
plt.scatter(X_ano_0, Y_ano_0, c='r', marker='*')
plt.scatter(X_ano_1, Y_ano_1, c='b', marker='^')
plt.show()
