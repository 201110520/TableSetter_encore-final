import pymysql
import POSvariable
import time

conn = pymysql.connect(
 host=POSvariable.loginVariable['host'],
 port=POSvariable.loginVariable['port'],
 user=POSvariable.loginVariable['user'], 
 password=POSvariable.loginVariable['password'], 
 db=POSvariable.loginVariable['db'],
 charset=POSvariable.loginVariable['charset'] )
curs = conn.cursor()

class LoginCtrl:
    def loginCheck(self,ID, PW):
        try:
            sql = "SELECT Store_Admin.id, Store_Admin.pw FROM Store_Admin WHERE Store_Admin.id = '"+ID+"' AND Store_Admin.pw = password('"+PW+"')"
            curs.execute(sql)
            row = curs.fetchone()

            if row != None:
                print("로그인에 성공하였습니다. %s 님!" % ID)
                sql = "SELECT Store_Admin.store_num FROM Store_Admin WHERE Store_Admin.id = '"+ID+"'"
                curs.execute(sql)
                Store_ID = curs.fetchone()
                #print(Store_ID[0])
            conn.commit()
            
            return ID, Store_ID[0]

        except:
            errText = '로그인에 실패하였습니다! ID와 PW를 다시 확인해주세요!'
            print(errText)
            y = 0
            conn.commit()
            
            return errText, y

class AddUserCtrl:
    def AddUser(self, ID, PW, Explain):
        try:
            #print(ID, PW, Explain)
            sql='INSERT INTO Store_User VALUES ("'+ ID +'", password("'+ PW +'$3@1"),"'+ Explain +'","'+ POSvariable.STORE_ID +'")'
            curs.execute(sql)
            conn.commit()
            return_text = ID+"계정등록이 완료 되었습니다."
            
            return return_text

        except:
            
            #print(sql)
            errText = '이미 사용중인 ID 입니다.'
            
            return errText

class Tablectrl:
    def TableMenuLoad(self):
        try:
            rows=0
            print(rows)
            sql='SELECT F.NAME, F.price,F.category_num FROM Menu M, Food F WHERE M.Food_num = F.num and M.Store_num = "'+POSvariable.STORE_ID+'"'
            curs.execute(sql)
            rows = curs.fetchall()
            conn.commit()
            return rows
        except:
            print('error: ')
    
    def billLoad(self,table_num):
        try:
            rows=0
            sql='SELECT F.NAME, F.price , O.amount, O.pay_code FROM Food F, OrderDetail O, OrderHistory H WHERE F.num=O.Food_num and O.Order_num = H.num AND H.pay_state=0 and H.Store_num = "'+ POSvariable.STORE_ID +'" AND H.table_num= '+str(table_num)+''
            curs.execute(sql)
            rows = curs.fetchall()
            conn.commit()
            card = 0
            cash = 0
            for i in range(len(rows)):
                name, price, amount, paycode = rows[i]
                if paycode == 1:
                    card += int(price)*amount
                elif paycode !=1:
                    cash += int(price)*amount
            return rows, card, cash
        except:
            print("error: billLoad")
    
    def orderTotal(self,table_num):
        try:
            rows = []
            total = 0
            sql = 'SELECT F.price , O.amount FROM Food F, OrderDetail O, OrderHistory H WHERE F.num=O.Food_num and O.Order_num = H.num AND H.pay_state=0 and H.Store_num = "'+ POSvariable.STORE_ID +'" AND H.table_num= '+str(table_num)+''
            curs.execute(sql)
            rows = curs.fetchall()
            conn.commit()
            #print('orderTotal:',rows)
            #print(len(rows))
            for i in range(len(rows)):
                price, amount = rows[i]
                #print(int(price),amount)
                total += int(price)*amount
            return total
        except:
            print('error: orderTotal')

    def addlist1(self,table_num,count):
        try:
            list1 = count.items()
            list2 = list(list1)
            for i in range(len(list1)):
                sql= 'INSERT INTO OrderDetail(Order_num, Food_num, amount, pay_code) SELECT  (SELECT H.num FROM OrderHistory H WHERE H.pay_state = \'0\' and H.Store_num ="'+ POSvariable.STORE_ID +'" AND H.table_num = '+str(table_num)+'),(SELECT Food.num FROM Food WHERE Food.name = "'+ list2[i][0] +'"),"'+ str(list2[i][1]) +'",\'3\' '
                curs.execute(sql)
                conn.commit()
        except:
            print('error: addlist')
            sql2 = 'INSERT INTO OrderHistory(Store_num, order_date, table_num) VALUES ("'+ POSvariable.STORE_ID +'",NOW(),'+str(table_num)+')' 
            curs.execute(sql2)
            conn.commit()
            self.addlist1(table_num,count)

    def payment(self,table_num):
        try:
            sql = 'UPDATE OrderHistory H SET H.pay_state=1 WHERE H.Store_num = "'+ POSvariable.STORE_ID +'" AND H.table_num= '+str(table_num)+''
            curs.execute(sql)
            conn.commit()
            print('정상 결제 되었습니다.')
        except:
            print('error: payment')
    
class AccCtrl:
    def get_data_day(self, date):
        try:
            key = "'" + date + "%'"
            sql = 'SELECT H.order_date, F.NAME, O.pay_code FROM OrderHistory H JOIN OrderDetail O ON H.num=O.Order_num JOIN Food F ON O.Food_num=F.num WHERE H.Store_num = "'+ POSvariable.STORE_ID +'" AND DATE(H.order_date)= '+key+''
            curs.execute(sql)
            fetch_payment = curs.fetchall()
            return list(fetch_payment)
        except:
            print('error: searching by day failed')

    def get_day_total(self, date):
        try:
            key = "'" + date + "%'"
            curs.execute("""SELECT Pprice FROM t_payment
            WHERE Ptime LIKE %s""" % key)
            fetch_num = curs.fetchall()
            total_int = 0
            for i in range(0, len(fetch_num)):
                total_int += int(fetch_num[i][0])
            return total_int
        except:
            print('error:')

    def get_month_total(self, date):
        try:
            key = "'" + date + "%'"
            curs.execute("""SELECT Pprice FROM t_payment
            WHERE Ptime LIKE %s""" % key)
            fetch_num = curs.fetchall()
            total_int = 0
            for i in range(0, len(fetch_num)):
                total_int += int(fetch_num[i][0])
            return total_int
        except:
            print('error:')

    def get_method_day(self, date):
        try:
            key = "'" + date + "%'"
            sql = 'SELECT F.price, O.amount , O.pay_code FROM OrderHistory H JOIN OrderDetail O ON H.num=O.Order_num JOIN Food F ON O.Food_num=F.num WHERE H.Store_num = "'+ POSvariable.STORE_ID +'" AND DATE(H.order_date)= '+key+''
            curs.execute(sql)
            fetch_method = curs.fetchall()

            on = 0
            off = 0
            total = 0

            for i in range(0, len(fetch_method)):
                #m_string = str(fetch_method[i])
                #sp_buf = m_string[2:-3].split(',')
                if fetch_method[i][2] == 1:
                    on += int(fetch_method[i][0]) * int(fetch_method[i][1])
                else:
                    off += int(fetch_method[i][0]) * int(fetch_method[i][1])

            total = on + off
            method_output = [on, off, total]  # card, cash, point, total
            return method_output

        except:
            print('error:')



    def get_method_month(self, date):
        try:
            key = "'" + date + "%'"
            sql = 'SELECT F.price, O.amount , O.pay_code FROM OrderHistory H JOIN OrderDetail O ON H.num=O.Order_num JOIN Food F ON O.Food_num=F.num WHERE H.Store_num = "'+ POSvariable.STORE_ID +'" AND H.order_date LIKE '+key+''
            curs.execute(sql)
            fetch_method = curs.fetchall()

            on = 0
            off = 0
            total = 0

            for i in range(0, len(fetch_method)):
                #m_string = str(fetch_method[i])
                #sp_buf = m_string[2:-3].split(',')
                if fetch_method[i][2] == 1:
                    on += int(fetch_method[i][0]) * int(fetch_method[i][1])
                else:
                    off += int(fetch_method[i][0]) * int(fetch_method[i][1])

            total = on + off
            method_output = [on, off, total]  # card, cash, point, total
            return method_output

        except:
            print('error:')


    def get_data_day_method(self, date):
        try:
            key = "'" + date + "%'"
            curs.execute("""SELECT Pmethod FROM t_payment
            WHERE Ptime LIKE %s""" % key)
            fetch_payment = curs.fetchall()
            return list(fetch_payment)
        except:
            print('error: searching by day failed')

    def get_amount(self, date):
        try:
            key = "'" + date + "%'"
            sql = 'SELECT COUNT(*) FROM OrderHistory H JOIN OrderDetail O ON H.num=O.Order_num JOIN Food F ON O.Food_num=F.num WHERE H.Store_num = "'+ POSvariable.STORE_ID +'" AND DATE(H.order_date)= '+key+''
            curs.execute(sql)
            fetch_amount = curs.fetchone()
            return fetch_amount[0]
        except:
            print('error: counting failed')

class Menuctrl:
    def cateinfo(self):
        try:    
            rows=0
            cate=[]
            sql = 'SELECT C.NAME FROM Category C WHERE C.Store_num = "'+ POSvariable.STORE_ID +'"'
            curs.execute(sql)
            rows = curs.fetchall()
            conn.commit()
            print(rows)
            for i in range(len(rows)):
                name = rows[i][0]
                cate.insert(i,name)
            print(cate)
            return cate
        except:
            print('error: cateinfo')

    def menuLoad(self):
        try:
            rows = 0
            count = 0
            sql = 'SELECT F.NAME,F.price,F.`STATUS` FROM Food F, Menu M WHERE M.Food_num = F.num AND M.Store_num = "'+ POSvariable.STORE_ID +'"'
            curs.execute(sql)
            rows = curs.fetchall()
            conn.commit()
            count = len(rows)
            print(rows, count)
            return rows, count
        except:
            print('error: menuLoad')
    
    def cellselet(self,name):
        try:
            sql = 'SELECT F.num, C.NAME,F.NAME,F.img_src,F.price,F.description FROM Food F, Category C WHERE F.category_num=C.num AND C.Store_num="'+ POSvariable.STORE_ID +'" AND F.NAME = "'+ name +'"'
            curs.execute(sql)
            row = curs.fetchone()
            conn.commit()
            print(row)
            return row
        except:
            print('error: cellselet')
    
    def menuAdd(self, rows):
        try:
            #-----------------------이미지 파일 이름 생성?-------------
            print(rows)
            Fname = rows[-1].split('/')[-1]
            url = 'https://untact-order-system-images.s3.ap-northeast-2.amazonaws.com/'+ POSvariable.STORE_ID +'/'+ Fname +''
            print(url)
            #-----------------------카테고리 값 가져오기------------
            sql = 'SELECT C.num FROM Category C WHERE C.Store_num = "'+ POSvariable.STORE_ID +'"AND C.NAME="'+ rows[0] +'"'
            curs.execute(sql)
            category = curs.fetchone()
            conn.commit
            print(category)
            #----------------food 테이블에 삽입-------------
            sql2 = "INSERT INTO Food( category_num, NAME,img_src,price,description) VALUES ('"+str(category[0])+"','"+rows[1]+"','"+url+"','"+rows[2]+"','"+rows[3]+"')"
            curs.execute(sql2)
            conn.commit
            #time.sleep(2)
            #------Food.num 가져오기------
            sql3 = 'SELECT F.num FROM Food F WHERE F.NAME="'+ rows[1] +'" and F.img_src="'+ url +'"'
            curs.execute(sql3)
            Fnum = curs.fetchone()
            conn.commit
            print(Fnum)
            #-----menu 테이블에 삽입-----------
            sql4 = "INSERT INTO Menu( Store_num,Food_num) VALUES('"+POSvariable.STORE_ID+"','"+str(Fnum[0])+"')"
            curs.execute(sql4)
            conn.commit
        except:
            print('error:menuAdd')

    def menuOpenClose(self, rows):
        try:
            sql= 'UPDATE Food F JOIN Menu M ON F.num=M.Food_num SET F.`STATUS` = "'+ str(rows[2]) +'" WHERE M.Store_num = "'+ POSvariable.STORE_ID +'" AND F.NAME = "'+ rows[0] +'"'
            curs.execute(sql)
            conn.commit
        except:
           print('error:menuOpenClose')
    
    def menuDelete(self,rows):
        try:
            sql = 'SELECT F.num FROM Food F JOIN Category C ON F.category_num=C.num WHERE C.Store_num = "'+ POSvariable.STORE_ID +'" AND F.NAME ="'+ rows[0] +'" AND C.NAME="'+ rows[1] +'"'
            curs.execute(sql)
            Fnum = curs.fetchone()
            print(str(Fnum[0]))
            conn.commit
            sql2 = "DELETE FROM Menu WHERE Menu.Store_num= '"+ POSvariable.STORE_ID +"' AND Menu.Food_num = '"+ str(Fnum[0]) +"'"
            curs.execute(sql2)
            conn.commit
            sql3 = "DELETE FROM Food WHERE Food.num= '"+ str(Fnum[0]) +"'"
            curs.execute(sql3)
            conn.commit
        except:
            print("error:menuDelete")

    def menuModNoImage(self,Fname,rows):
        try:
            sql='SELECT F.num FROM Food F, Menu M WHERE F.num=M.Food_num AND M.Store_num = "'+ POSvariable.STORE_ID +'" AND F.NAME = "'+Fname+'"'
            curs.execute(sql)
            Fnum=0
            Fnum=curs.fetchone()
            print(rows[3])
            sql2='UPDATE Food F SET F.category_num=(SELECT C.num FROM Category C WHERE C.NAME=\''+rows[3]+'\'AND C.Store_num= "'+ POSvariable.STORE_ID +'"),F.NAME=\''+rows[0]+'\' ,F.price=\''+rows[1]+'\' ,F.description=\''+rows[2]+'\'  WHERE F.num=\''+str(Fnum[0])+'\''
            curs.execute(sql2)
            conn.commit
        except:
            print('error:menuMod')
    
    def menuMod(self,Fname,rows):
        #try:
            print(rows)
            imagename = rows[-1].split('/')[-1]
            url = 'https://untact-order-system-images.s3.ap-northeast-2.amazonaws.com/'+ POSvariable.STORE_ID +'/'+ imagename +''
            Fnum=0
            sql='SELECT F.num FROM Food F, Menu M WHERE F.num=M.Food_num AND M.Store_num = "'+ POSvariable.STORE_ID +'" AND F.NAME = "'+Fname+'"'
            curs.execute(sql)
            Fnum=curs.fetchone()
            print(str(Fnum[0]))
            print(rows[0],rows[1],rows[2],rows[3])
            sql2='UPDATE Food F SET F.category_num=(SELECT C.num FROM Category C WHERE C.NAME=\''+rows[0]+'\'AND C.Store_num= "'+ POSvariable.STORE_ID +'"),F.NAME=\''+rows[1]+'\' ,F.img_src= \''+url+'\',F.price=\''+rows[2]+'\' ,F.description=\''+rows[3]+'\'  WHERE F.num=\''+str(Fnum[0])+'\''
            curs.execute(sql2)
            conn.commit

class Payctrl:
    def total(self,tablenum):
        #try:
            sql = 'SELECT F.price, O.amount, O.pay_code, H.num FROM Food F JOIN OrderDetail O ON F.num=O.Food_num join OrderHistory H ON O.Order_num=H.num WHERE H.pay_state=0 AND H.Store_num = "'+ POSvariable.STORE_ID +'" AND H.table_num = "'+ str(tablenum) +'"'
            curs.execute(sql)
            rows=curs.fetchall()
            total=0
            for i in range(0,len(rows)):
                if int(rows[i][2])!=1:
                    total += (int(rows[i][1])*int(rows[i][0]))
                else:
                    total=total
            return total, str(rows[0][3])

        #except:
        #    print('error:Payctrl total')

    def paidcard(self, ordernum, cardid, payamount):
        #try:
            sql = 'INSERT INTO Payment(Order_num,card_id, pay_code, paid, pay_date) VALUES ("'+ordernum +'","'+cardid +'", \'2\' , "'+  payamount +'",NOW())'
            curs.execute(sql)
            conn.commit()
        #except:
        #    print('error:Payctrl paidcard')
    def paidcash(self,ordernum, payamount):
        #try:
            sql = 'INSERT INTO Payment (Order_num, pay_code, paid, pay_date ) VALUES ("'+ordernum +'",\'3\', "'+  payamount +'",NOW())'
            curs.execute(sql)
            conn.commit()
        #except:
        #    print('error:Payctrl paidcash')
    