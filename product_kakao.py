import glob
import os
import sys
from collections import Counter
from tkinter import *
from tkinter import filedialog, messagebox
import requests
from PIL import ImageTk, Image, ImageDraw

def file_open():
    global file_img # file_img 전역 변수로 지정
    w.filename = filedialog.askopenfilename(initialdir='', title="파일 선택", filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*'))) # 열고자하는 파일 선택
    # Label(w, text=w.filename).pack() # 파일 경로 view
    file_img = ImageTk.PhotoImage(Image.open(w.filename)) # file_img : 파일열기로 가져온 이미지
    Label(w, image=file_img, width=700, height=500).pack() # file_img 크기 조절 및 창에 표시

API_URL = '' # Kakao vision api url
MYAPP_KEY = '' # 발급받은 Rest API 키

def detect_product(filename): # 파일 분석
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        files = { 'image' : open(filename, 'rb')} # 열어서 가져온 이미지
        resp = requests.post(API_URL, headers=headers, files=files)
        json_result = resp.json()  # json 응답
        # print(json_result)
        result = json_result['result']  # 'result': {}
        objects = result['objects']  # result {} 내부의 'objects' 값 가져오기
        class_list = []  # 담을 공간 초기화
        for x in range(len(objects)):
            ob = objects[x]  # {'키':값,'키':값,...} {..} {..} {...}
            # print(ob)
            # print(ob['class']) #shoes, tote bag, tote bag, one-piece
            class_list.append(ob['class'])  # 키가 class인 부분의 값을 추출하여 class_list라는 이름의 리스트에 담는다.
        print(class_list)
        # from collections import Counter
        count_result = Counter(class_list)  # 개수 세는 함수
        print('count_result:', count_result)
        # print(count_result.get('tote bag'))#2
        # print(count_result.most_common(1))#most_common은 순위를 알려주는것(튜플)
        print(count_result.most_common(len(count_result)))  # count_result의 전체 우선순위를 구해준다.
        order = count_result.most_common(len(count_result))

        print('이미지에서 가장 많이 검출된 상품은', order[0], '입니다.')
        priority_order = []
        for x in order:  # for-each문을 통해 list에서 튜플을 빼내준다. [('tote bag',값),('shoes', 값),('one-piece', 값)]
            print(x[0])  # tote bag, shoes, one-piece
            print(x[1])  # 값, 값, 값
            priority_order.append(x[0])
        # print('priority_order:', priority_order)

        print(priority_order[0])
        url = ''
        if priority_order[0] == 'tote bag':  # 가장 우선순위가 높은 것이 'tote bag'이라면..
            url = 'tote bag'  # tote bag에 맞는 url 추출..
            print(url)
        elif priority_order[0] == 'shoes':
            url = 'shoes'
            print(url)
        elif priority_order[0] == 'pants':
            url = 'pants'
            print(url)
        elif priority_order[0] == 't-shirts':
            url = 't-shirts'
            print(url)
        elif priority_order[0] == 'one-piece':
            url = 'one-piece'
            print(url)
        elif priority_order[0] == 'outer':
            url = 'outer'
            print(url)
        else:
            print(url)
            result.config(text='url입니다.')
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        # sys.exit(0) # 예외 발생 시 종료

def show_products(filename, detection_result):
    try:
        image = Image.open(filename) # 이미지 열기
    except Exception as e:
        print(str(e))
        sys.exit(0) # 예외 발생 시 종료
    draw = ImageDraw.Draw(image) # 이미지 위에 그리기
    # 대상의 분석 틀 생성
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1']*image.width)
        y1 = int(obj['y1']*image.height)
        x2 = int(obj['x2']*image.width)
        y2 = int(obj['y2']*image.height)
        draw.rectangle([(x1,y1), (x2, y2)], fill=None, outline=(255,0,0,255))
        draw.text((x1+5,y1+5), obj['class'], (255,0,0))
    del draw
    return image # 이미지 반환

def save_img(): # 분석된 이미지 저장
    global file_img  #
    w.filename = filedialog.askopenfilename(initialdir='', title="파일 선택", filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*'))) # 파일 하나 선택
    head = './image'
    #tail = w.filename
    # print('---' , w.filename) # --- C:/Users/hi/Desktop/python_project/pythonProject8/toyproject/image/girl.jpg
    file_result = w.filename.split('/') # w.filename에서 '/'을 빼고 리스트로 저장
    # print(file_result) # ['C:', 'Users', 'hi', 'Desktop', 'python_project', 'pythonProject8', 'toyproject', 'image', 'girl.jpg']
    file_name = file_result[len(file_result)-1] # 파일 이름은 file_result의 (file_result 길이- 1)번째
    # print(file_name) # girl.jpg
    detection_result = detect_product(w.filename)
    image = show_products(w.filename, detection_result)  # 불러온 이미지 분석
    image.save(head + '/detect_' + file_name, 'JPEG') # 분석한 이미지 저장
    # files = glob.glob('./image/*.jpg') # image 폴더 안의 jpg 파일을 모두 지정
    # for i in files:
    #     head, tail = os.path.split(i) # 저장되는 파일명의 head와 tail 경로 명시
    #     print(head)
    #     detection_result = detect_product(i) # 불러온 이미지 분석
    #     image = show_products(i, detection_result) # 불러온 이미지 분석
    #     image.save(head + '/detect_' + tail, 'JPEG') # 분석한 이미지 저장
    messagebox.showinfo('요청하신 분석에 대하여', "분석이 완료되었습니다.") # 이미지 분석 완료 시 나오게 하는 알림 창

w = Tk()
w.geometry("1000x700+100+100") # 창 크기 설정
w.title("tkinter 이미지 분석") # 창 제목 설정
detect_command = Button(w, text="파일 분석 & 저장", command=save_img).pack() # 이미지 분석 & 저장
result = Label(w, text='결과는 여기에', font=('궁서', 30)).pack() # 추천 url 표시
open_command = Button(w, text="파일 열기", command=file_open).pack() # 분석된 결과 이미지 열기
w.mainloop() # 루프 처리, 프로그램 흐름 마지막 단에 위치해야 함