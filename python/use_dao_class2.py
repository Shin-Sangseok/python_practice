from db.dao_class2 import *

if __name__ == '__main__':
    vo = input('id,name,url,img>>').split(',')
    dao = DAO() #DAO라는 틀을 통해 실제로 쓸 수 있는 dao를 만들어주세요 라는 의미
                #실제 벽돌1 = 벽돌틀()
    dao.create(vo)






