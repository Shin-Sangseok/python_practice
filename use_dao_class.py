from db.dao_class import *

if __name__ == '__main__':
    dao = DAO()  # init()호출함. db연결 -> cursor 객체 생성
    vo = input('id,name, url,img>>').split(',')
    dao.create(vo)  # sql만들어 전송, 결과받아 오는 것.



