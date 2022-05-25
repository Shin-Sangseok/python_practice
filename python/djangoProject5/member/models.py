from django.db import models

# Create your models here.
#장고는 sql을 몰라도 테이블을 생성할 수 있도록 제공하고 있음
#ORM을 models.py에 정의해주세요
#테이블하나당 클래스하나로 정의
class Member(models.Model):
    #멤버변수를 생성해주면,
    #1. vo변수의 역할
    #2. table의 항목을 생성
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_tel = models.CharField(max_length=255)

#java vo에서의 toString()역할
    def __str__(self):
        return self.user_id+","+\
            self.user_pw+","+\
            self.user_name + ","+\
            self.user_tel

class Test(models.Model):
    ##id는 default로 만들어진다
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)

    ##python ovrride
    def __str__(self):
        return str(self.id)+", "+self.name +", "+\
            self.tel +", "+self.addr

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    question_writer = models.CharField(default='blank', max_length=500)
    pub_date = models.DateTimeField('')

    def __str__(self):
        return str(self.id) + "," +\
            self.question_text + "," +\
            self.question_writer + "," +\
            str(self.pub_date)

