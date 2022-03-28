import matplotlib

# !pip install matplotlib=버전

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np
import random

xpoints = np.array([1,2,3,4,5]) #차원 리스트
xpoints1 = np.array([1,2,3,4,5]) #차원 리스트

print(type(xpoints))

ypoints = np.array([30,50,20,100,10]) #
ypoints2 = np.array([50,100,50,40,80]) #

print(type(ypoints))


line1 = plt.plot(xpoints, ypoints, marker='^', linestyle='dotted')
line2 = plt.plot(xpoints1, ypoints2, marker='o')

plt.legend(['term1','term2'])

plt.xlabel('numbers of students')
plt.ylabel('counts')

plt.show()

x = []
y = []
for i in range(1,101):
    x.append(i)
    y.append(random.randint(1,100))
print(x[:10]) #수량이 너무 많이 나올 때는 10개 정도 출력해본다.
y[:10]

xpoints = np.array(x) #차원 리스트
ypoints = np.array(y) #

plt.scatter(xpoints, ypoints, marker='o') #점으로 그림을 그려줌.
plt.show()

