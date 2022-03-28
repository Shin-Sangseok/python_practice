import pymysql
#data access module
#crud기능
#def 4개 필요
class DAO:
    #인스턴스 변수
    conn = None #변수 생성된 위치가 중요
                #클래스 바로 아래에 생긴 변수는 클래스 안 전체에서 쓸 수 있다.
                #이것을 전역변수(글로벌 변수)라고 부른다.
                
    cur = None

    def __init__(self):
        #함수내에서 처음으로 만들어진 변수(지역변수, 로컬변수)는
        #함수밖에서는 인식 불가
        #변수의 위치가 중요하다. (변수가 함수내에서 만들면 함수내에서만 쓰겠다는 의미)
        #(클래스 안에서 만들어지면 클래스 안에서 사용하겠다는 의미)
        #파이썬에서 변수는 언제 만들어지나?
        #변수명 = 초기값 (이 때 만들어진다)


        # 객체 생성할 때 객체의 초기화 담당
        # 멤버변수 초기화
        # 객체생성할 때 무조건 호출되므로
        # 객체생성하고 나서 꼭 실행하고 싶은 내용을
        # init 함수에 정의하면 실행됌.
        # instance변수를 self를 통해서 접근한다.
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3366,
                user='root',
                password='1234',
                db='big3',
                charset='utf8'
            )

            print('연결 성공', self.conn.host_info)  # host_info는 어디에 연결됐는지 보여줌.
            # 연결된 통로(stream)을 통해 , SQL문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는)커서 객체를 획득

            cur = self.conn.cursor()

        except Exception as e:
        print('db연결 중 에러 발생')
        print('에러 정보>>', e)

    def create(self, vo):
        try:

            # 3. sql문을 보내보자.
            sql = "insert into member values(%s, %s, %s, %s)"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>>', result)

            self.conn.commit()  # insert한 것 반영해줘.
            self.conn.close()

    def read(self, id):
        try:

            # 3. sql문을 보내보자.
            sql = "select * from member where id = %s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, (id))
            print('sql문 전송 결과>>', result)

            #read인 경우 , 커서로 연결통로(스트림) 검색결과를 꺼내주어야 한다.
            row = self.cur.fetchone() #row하나만 꺼내
            print(row)
            #select는 commit을 하지 않음.(반영할 게 없음)
            self.conn.close()
            return row #검색결과를 return

    def update(self, id, pw, tel):
        try:

            # 3. sql문을 보내보자.
            sql = "update member set pw = %s ,tel = %s where id = %s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, (pw, tel, id))
            print('sql문 전송 결과>>', result)

            self.conn.commit()  # insert한 것 반영해줘.
            self.conn.close()


    def delete(self, id):
        try:

            # 3. sql문을 보내보자.
            sql = "delete from member where id = %s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, id)
            print('sql문 전송 결과>>', result)

            self.conn.commit()  # insert한 것 반영해줘.
            self.conn.close()

    def all(self):
        try:

            # 3. sql문을 보내보자.
            sql = "select * from member"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql)
            print('sql문 전송 결과>>', result)

            #row = cur.fetchone() #row 하나만 꺼내
            row = self.cur.fetchall() #모두 꺼내
            print(row)
            #row = cur.fetchmany()#row 개수를 정해서 꺼내

            # select는 commit을 하지 않음.(반영할 게 없음)
            self.conn.close()
            return row  # 검색결과를 return
