import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/track1.csv')

# 같은 UA 같은 IP로 접근하면서 같은 Referer로 접근하는 로그를 잡아보자

df.tail()


##############################

# 가장많이 접근한 IP

##############################

df['Host'].value_counts().head()


##############################

# 가장 접근을 많이 한 UA top 50
# 특이사항 없음

##############################

df['UA'].value_counts().head(50)

##############################

# 문자열 'bot' or 'Bot'이 포함된 행 추출
# 결과 : 0
# 가정 : 일반적인 웹사이트는 검색노출을 위해 수시로 봇들이 접근하지만
# 해당 웹 페이지는 데이터 생성용 더미사이트라 공개가 안 되어있을 수도 있다.
# 크롤러 또는 스크랩퍼에 헤더 변경은 매우 간단하므로 변경하여 사용하는게 일반적이다.

##############################

bot = df['UA'].str.contains('bot', na = False)
UA_bot = df[bot]
len(UA_bot)

Bot = df['UA'].str.contains('Bot', na = False)
UA_Bot = df[Bot]
len(UA_Bot)

##############################

# 문자열 'Python' or 'python'이 포함된 행 추출
# 결과 : 16771, 72
# 스크랩퍼에 헤더 내용을 변경하지 않고 접근한 로그내역

##############################

Python = df['UA'].str.contains('Python', na = False)
UA_Python = df[Python]
len(UA_Python)
UA_Python

python = df['UA'].str.contains('python', na = False)
UA_python = df[python]
len(UA_python)

##############################

# Python or python UA를 이용한 IP주소
# 같은 놈이다.

##############################

UA_Python['Host'].unique()
UA_python['Host'].unique()

##############################

# When?? 2020-08-24 15:46 ~ 16:23 _ 37분간 지속된 접근
UA_python['Timestamp'].unique()[0]
UA_python['Timestamp'].unique()[-1]

# When?? 2020-08-24 16:24 ~ 2020-08-27 15:33 _ 3박 4일간 끈질길 접근
UA_Python['Timestamp'].unique()[0]
UA_Python['Timestamp'].unique()[-1]

##############################

# 가장 많이 접근한 UA를
# 가장 많이 이용한 IP가
# 사용한 UA
# 'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.0 Version/10.00',
# 'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.0 Version/9.00',
# 'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.0 Version/8.00'
# 버전만 다른 Presto

##############################

UA_1 = df[df['UA'] == 'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.0 Version/10.00']
UA_1_IPS = UA_1['Host'].value_counts()
UA_1_IPS
UA_1_IPS.index[0]

UA_1_IPS_UA = []

for i in range(len(UA_1_IPS)):
    UA_1_IPS_n = df[df['Host'] == UA_1_IPS.index[i]]
    UA_1_IPS_n_UA = UA_1_IPS_n['UA'].unique()
    UA_1_IPS_UA.append(UA_1_IPS_n_UA)

UA_1_IPS_UA
