import pandas as pd
import numpy as np
import random

#1. df로 읽어들이고
df=pd.read_csv(r'C:\Users\hi\PycharmProjects\0316dataframe\scientists.csv')
#r을 앞에 붙여주면 raw string으로 경로를 그대로 인식한다.
df

#2. df의 전체 데이터셋 타입을 확인
df.dtypes

#3. df의 컬럼리스트를 확인
df.columns

#4. df의 값을 확인
df.values

#5. df의 맨 마지막에 price 항목을 추가 (값은 임의대로 넣음, int)
df['price'] = df['Age']+random.randint(1000,5000)
df

#6. df의 맨 마지막에 percent항목을 추가(값을 임의대로 넣음. float)
df['percent'] = df['Age']*random.uniform(0.4,0.8)
a=[]
int_a =[]
for i in range(8):
    a.append(df['percent'].values[i])
    int_a.append(int(a[i])*0.01)
#int_a
df['percent'] = int_a
df['percent']
df

#7. df의 맨 마지막에 sale항목을 추가(price * percent)
df['sale'] = df['price']*df['percent']
df

#8. df의 Name컬럼 추출
df.columns[0]

#9. df의 인덱스 확인
df.index

#10. df의 Name컬럼의 값이 Rosaline인 행 추출
df.loc[0:0,]

#11. df의 Name컬럼 중 3~5사이의 행 추출
df.loc[3:5,]

#12. df의 Name, Died컬럼 추출
df.columns[0],df.columns[2]

#13. df의 Born컬럼부터 컬럼 끝까지 모든 행 추출
df.loc[0:8,'Born':'sale']

#14. df의 Born, Age컬럼의 5~7행 추출
df.loc[5:8,'Born']
df.loc[5:9,'Age']

#15. df.shape을 통해 몇행 몇열인지 확인해보세요.
df.shape

#16. df의 숫자 데이터의 상세 정보 확인
df.describe()

#17. Nurse라는 스트링 추출 (index와 컬럼명을 사용)
df.iloc[2,4]

#18. Alan Turing이라는 스트링 추출 (index와 컬럼명을 사용)
df.iloc[6,0]

#19. Biologist를 Scientist로 변경
df.iloc[4,4] = 'Scientist'
df


