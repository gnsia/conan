##############################################

# 1. 딱 한번만 접근한 IP주소는 정상행위로 가정한다.
# 2. 특정 분(minute)에서 가장 많이 접근한 IP주소와 두번째로 많이 접근한 IP주소가 100번 넘게 차이나면
# 가장 많이 접근한 IP주소를 이상접근으로 가정한다.
# 3. UA에 기본 브라우저가 아닌 라이브러리 및 스크립트로 접근

##############################################


import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/track1.csv')

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

df.loc[:,'Bytes']

d = []
for i in range(len(df['Date'].unique())):
    x = df[df['Date'] == df['Date'].unique()[i]]
    d.append(x)

d[0]['Host'].value_counts()
d[1]['Host'].value_counts()
d[2]['Host'].value_counts()
d[3]['Host'].value_counts()
d[4]['Host'].value_counts()



d24t10 = d24[d24['Hour'] == d24['Hour'].unique()[0]]

d24t10_ano_IP_0 = d24t10[d24t10['Host'] == d24t10['Host'].value_counts().index[0]]
d24t10_ano_IP_1 = d24t10[d24t10['Host'] == d24t10['Host'].value_counts().index[1]]

X = d24t10['Min']
Y = d24t10['Sec']
X_ano_0 = d24t10_ano_IP_0['Min']
Y_ano_0 = d24t10_ano_IP_0['Sec']
X_ano_1 = d24t10_ano_IP_1['Min']
Y_ano_1 = d24t10_ano_IP_1['Sec']


plt.figure(figsize=(10,10))
plt.title("good")
plt.xlabel('min')
plt.ylabel('sec')
plt.scatter(X, Y, c='black', marker='o')
plt.scatter(X_ano_0, Y_ano_0, c='r', marker='*')
plt.scatter(X_ano_1, Y_ano_1, c='b', marker='^')
plt.show()
