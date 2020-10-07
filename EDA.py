import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/track1.csv')

# 같은 UA 같은 IP로 접근하면서 같은 Referer로 접근하는 로그를 잡아보자

df.head()

##############################

# 가장 접근을 많이 한 UA top 50
# 특이사항 없음

##############################

df['UA'].value_counts().head(50)

##############################

# 문자열 'bot'이 포함된 행 추출
# 결과 : 0
# 가정 : 일반적인 웹사이트는 검색노출을 위해 수시로 봇들이 접근하지만
# 해당 웹 페이지는 데이터 생성용 더미사이트라 공개가 안 되어있을 수도 있다.
# 크롤러 또는 스크랩퍼에 헤더 변경은 매우 간단하므로 변경하여 사용하는게 일반적이다.

##############################

bot = df['UA'].str.contains('bot', na = False)
UA_bot = df[bot]
UA_bot

##############################

# 문자열 'python'이 포함된 행 추출
# 결과 : 72
# 스크랩퍼에 헤더 내용을 변경하지 않고 접근한 로그내역

##############################

python = df['UA'].str.contains('python', na = False)
UA_python = df[python]
UA_python.head()
len(UA_python)

# When?? 2020-08-24 15:46 ~ 16:23 _ 37분간 지속된 접근
UA_python['Timestamp'].unique()[0]
UA_python['Timestamp'].unique()[-1]

# Where?Who? 단일 IP '101.224.32.28'
UA_python['Host'].unique()
py_crawler = UA_python['Host'].unique()[0]
py_crawler

# 전체 데이터 셋에서보면 다른 UA로 접근한 흔적이 있다.
anomaly_1 = df[df['Host'] == py_crawler]
anomaly_1.head()

# 로그도 많이 찍혀있다.
len(anomaly_1)

# When?
anomaly_1['Timestamp'].unique()[0]
anomaly_1['Timestamp'].unique()[-1]



UA_python['Method'].unique()
UA_python['Status'].unique()
UA_python['Path'].unique()



##############################

# 가장 접근 많이한 UA_1으로 분석시도

##############################

UA_1 = df[df['UA'] == 'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.0 Version/10.00' ]
UA_1.head()

# UA_1을 사용한 Host = 6개
# 그중 4개의 IP가 3번째자리까지 중복된다.

UA_1['Host'].value_counts()




result_Chrome = df[result_bot]
result_Chrome.head()
result_opera.head()
