import sys
import argparse
from tkinter import messagebox

import requests #알트+엔터(cmd+1)
from io import BytesIO
from collections import Counter
#kakao연결 + 신청해놨던 키.
API_URL = ''
MYAPP_KEY = ''

def multi_tag(image_url):
    header = {'' % MYAPP_KEY}
    img_data = {'': image_url}
    response = requests.post(API_URL,
                             headers=header,
                             data = img_data)
    json_result = response.json()
    #print(json_result)
    result = json_result['result']
    #print(result)
    lable_kr = result['label_kr']
    print(lable_kr)
    return lable_kr #리스트

if __name__ == '__main__':
    img_list = []
    result_list = []
    for img in img_list:
        lable_result = multi_tag(img)
        result_list += lable_result
        print(result_list)

        #from collections import Counter
        count_result = Counter(result_list)
        print(count_result)
        print(count_result.get('사람'))
        print(count_result.most_common(1))
        print(count_result.most_common(2)) #most_common은 순위를 알려주는 것.
                                           #하나하나가 튜플이다.
        order_5 = count_result.most_common(5)
        print(order_5[0])
        order_1 = order_5[0]
        print(order_1[0])
        print('제일 빈도수가 높은 단어는 ', order_1[0])

        tour = ''
        if order_1[0] == '사람':
            tour = ''
        elif order_1[0] == '남성':
            tour = ''
        else:
            tour = ''
        messagebox.showinfo('추천', '당신에게' +tour+ '를 추천합니다.')


