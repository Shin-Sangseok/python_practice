import pandas as pd
import numpy as np
import random

#dataframe == schema (db, table)

#dataframe을 만드는 방법
#1. 외부파일을 읽어온다.(csv, xlsx)
#2. 데이터구조를 가지고 dataframe을 만들어주면 된다.
#    dic, list

# 항목명1  항목명2,  항목명3  ==> dic(key)
#---------------------------
#100        200       300     ==> dic(val, list)
#200        220       330

#{"항목명1": [100, 200], "항목명2": [200, 220]}

df= pd.DataFrame({
             "name": ['홍길동', '박길동'],
             "age": [100, 30],
             "ex": [1,2]
             })
df

df['name']
df['age']

df['age'][df['age']>50] #컬럼 추출 후 뒤에 대괄호로 조건을 줄 수 있다.
                        #df[컬럼명][조건]: 조건이 True인 것만 추출!

df.loc[0] #loc[행]

df.loc[ : , 'age'] #df.loc[행, 열]

df.age

df.loc[:,'name']

df.loc[:,'name':'age']
df.loc[:,'name':'ex']
df.loc[0:2, 'age':'ex'] #0~1행, age~ex열 추출

df['add_column'] = df['age']+ df['ex']
#기존의 컬럼에다가 새로운 컬럼 추가 가능(파생한다,파생 컬럼, 파생변수)
#df[새로 만들고 싶은 컬럼명] = df[기존 컬럼] + df[기존 컬럼]
df

df['next_age']= df['age']+1
df

df.loc[0,'name']

df.iloc[0,0]

df.loc[0,'add_column']

df.loc[0,'add_column']= 200
df

df.iloc[1,4] = 300
df

df.iloc[1,4]

df.columns

df.index

df.values ##중요! --> ndarray클래스
# n : 숫자(차원수, 1차원이면 1, 2차원이면 2)
# d : 차원(dimension)
# array: 리스트
#판다스에는 여러 차원의 데이터를 하나의 클래스로 처리하기(다루기) 위해서
#여러 차원의 데이터를 다룰 수 있는 ndarray를 만들어 놓았음.

df['ex']

df.describe() #수치항목에 대해서만! 요약
#갯수, 평균(mean), std(표준편차), min(최소), max(최대)
# 25%, 50%, 75%, 100%(사분위 수)

name_list = []
age_list = []
ex_list = []
for i in range(1000):
    name_list.append('이름' + str(i))
    age_list.append(random.randint(1, 120))
    ex_list.append(random.randint(1, 2))
len(name_list), len(age_list), len(ex_list)

name_list[:5] #index 0~4, 5개를 print

name_list[995:]

age_list[:5]

ex_list[:5]

df2 = pd.DataFrame({
            "name":name_list,
            "age":age_list,
            "ex":ex_list
            })
#1. df로 만들어보고,
#2. 데이터타입을 확인해보고,
#3. 각 컬럼을 추출해보고,
#4. 숫자형 컬럼의 요약을 해보세요.
df2

type(df2['name'])

df2.dtypes #name: object(str), age(int64),

df2['age'] #데이터프레임[컬럼명]

df2.age

df2['age']>50 #브로드캐스팅

df2['age']-10 #브로드캐스팅
#원본을 가져다가 처리하므로, df2는 바뀌지 않음.
#(비파괴 연산)

df2['age']

df2['age'] = df2['age']-10
df2['age']

df2['name'] = df2['name']+ '님'
df2['name']

df2.describe()


