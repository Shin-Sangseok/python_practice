import random
import threading
import time
from tkinter import *
from tkinter import messagebox


class RacingCar:
    #멤버변수
    name = '' #인스턴스 변수
    counter = 0 #클래스 변수

    #초기화함수
    def __init__(self, name ,label, x1, y1):
        #self: 클래스로 생성한 객체!
        #c1 = RacingCar('appleCar') , c2, c3
        #self == c1
        #c1.name = 'appleCar'
        self.name = name
        self.label = label
        self.x1 = x1
        self.y1 = y1

    #멤버함수
    def runCar(self):
        while True:
            # 랜덤하게 움직일 값을 생성해서
            # 랜덤생성한 jump값을 기존의 x에 더해준다.
            # y축 값은 변하지 않음.
            jump = random.randint(1,20)
            self.x1 = self.x1 + jump
            if self.x1>=500:
                messagebox.showinfo('결과>>', self.name)
                break
            self.label.place(x=self.x1, y=self.y1)
            time.sleep(0.1)

def run_start():
    #라벨 객체를 만들어서 window에 끼워넣어야 함.
    print('call ok!!')

    c1 = RacingCar('appleCar',car_label1,10,100)
    c2 = RacingCar('summerCar',car_label2,10,150)
    c3 = RacingCar('springCar',car_label3,10,200)
    t1 = threading.Thread(target=c1.runCar)
    t2 = threading.Thread(target=c2.runCar)
    t3 = threading.Thread(target=c3.runCar)

    t1.start()
    t2.start()
    t3.start()
    #자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.

if __name__ == '__main__':
    window = Tk()
    window.geometry("500x250")
    window.title('멀티 스레드 자동차 경주')

    b = Button(window, text = '멀티 스레드 시작', command=run_start)
    b.pack(side = TOP, fill=X, ipadx = 10 ,ipady = 10, padx = 10, pady = 10)#fill x,y축 가득 채우는 것. ipadx 여백
    car1_img = PhotoImage(file = 'car1.gif')
    car2_img = PhotoImage(file = 'car2.gif')
    car3_img = PhotoImage(file = 'car3.gif')

    car_label1 = Label(window, image =car1_img)
    car_label1.place(x =10, y = 100)

    car_label2 = Label(window, image =car2_img)
    car_label2.place(x = 10, y = 150)

    car_label3 = Label(window, image =car3_img)
    car_label3.place(x = 10, y = 200)

    window.mainloop()





