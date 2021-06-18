# -*- coding: utf-8 -*-
#import base64
#from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives.asymmetric import rsa, padding
#from cryptography.hazmat.primitives import serialization, hashes
#
#
#def utf8(s: bytes):
#    return str(s, 'utf-8')
#
#
#private_key = rsa.generate_private_key(
#    public_exponent=65537,
#    key_size=1024,
#    backend=default_backend()
#)
#public_key = private_key.public_key()
#
#
#private_pem = private_key.private_bytes(
#    encoding=serialization.Encoding.PEM,
#    format=serialization.PrivateFormat.PKCS8,
#    encryption_algorithm=serialization.NoEncryption()
#)
#
#with open('C:/Users/seung/.ssh/my_private_rsa_key.pem', 'wb') as f:
#    f.write(private_pem)
#
#public_pem = public_key.public_bytes(
#    encoding=serialization.Encoding.PEM,
#    format=serialization.PublicFormat.SubjectPublicKeyInfo
#)
#with open('C:/Users/seung/.ssh/my_rsa_public.pem', 'wb') as f:
#    f.write(public_pem)
#
#
#with open("C:/Users/seung/.ssh/my_private_rsa_key.pem", "rb") as key_file:
#    private_key = serialization.load_pem_private_key(
#        key_file.read(),
#        password=None,
#        backend=default_backend()
#    )
#
#with open("C:/Users/seung/.ssh/my_rsa_public.pem", "rb") as key_file:
#    public_key = serialization.load_pem_public_key(
#        key_file.read(),
#        backend=default_backend()
#    )
#
#
#
#plaintext = '짜장면'.encode('utf-8') #b'test text'
#
#plaintext1= [('까르보나라치킨스파게티소스'.encode('utf-8'), '1'.encode('utf-8') ), ('탕수육'.encode('utf-8'),'1'.encode('utf-8')), ('짬뽕'.encode('utf-8'),'1'.encode('utf-8'))]
#print(plaintext)
#
#text1= []
#text= []
#for x in range(len(plaintext1)):
#    text2 = []
#    for y in range(len(plaintext1[0])):
#        
#        plaintext = plaintext1[x][y]
#        print(f'plaintext: \033[1;33m{plaintext.decode()}\033[0m')
#        print(public_key)
#        encrypted = base64.b64encode(public_key.encrypt(
#            plaintext,
#            padding.OAEP(
#                mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                algorithm=hashes.SHA256(),
#                label=None
#            )
#        ))
#        print(f'encrypted: \033[1;32m{encrypted}\033[0m')
#        print(len(encrypted))
#
#
#        decrypted = private_key.decrypt(
#            base64.b64decode(encrypted),
#            padding.OAEP(
#                mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                algorithm=hashes.SHA256(),
#                label=None
#            )
#        )
#        text2.insert(y, decrypted.decode() )
#        print(f'decrypted: \033[1;31m{ decrypted.decode() }\033[0m')
#    text1.insert(x,text2)
#print(text1)

#-----------------------------------------------------------------------------------------
#import POSvariable
#import pymysql
#
#conn = pymysql.connect(
# host=POSvariable.loginVariable['host'],
# port=POSvariable.loginVariable['port'],
# user=POSvariable.loginVariable['user'], 
# password=POSvariable.loginVariable['password'], 
# db=POSvariable.loginVariable['db'],
# charset=POSvariable.loginVariable['charset'] )
#curs = conn.cursor()
#STORE_IDd = '7ZmN7L2p67CY7KCQ'
#
#class Menuctrl:
#    def menuLoad():
#        #try:
#            sql = 'SELECT F.NAME,F.price,F.`STATUS` FROM Food F, Menu M WHERE M.Food_num = F.num AND M.Store_num = \'{}\''.format(STORE_IDd)
#            curs.execute(sql)
#            rows = curs.fetchall()
#            conn.commit()
#            print(rows)
#        
#        #except:
#        #    print(STORE_ID)
#        #    print('error: menuLoad')
#
#def menuLoad():
#        try:
#            rows=0
#            print(rows)
#            sql='SELECT F.NAME, F.price,F.category_num FROM Menu M, Food F WHERE M.Food_num = F.num and M.Store_num = "'+STORE_IDd+'"'
#            curs.execute(sql)
#            rows = curs.fetchall()
#            conn.commit()
#            print(rows)
#            print(len(rows))
#            return rows
#        except:
#            print(STORE_IDd)
#            print('error: ')
#
#Menuctrl.menuLoad()
#menuLoad()
#

#mystr = 'http://cdn.ppomppu.co.kr/zboard/data3/2019/0614/m_20190614110634_fntcdafd.jpg'
#if 'http' in mystr:
#    mylist = mystr.split('/')[-1]
#    print(mylist)
#def test():
#    return False
#
#if type(test())==bool and test() == False:
#    print('와!')

#배포전략
#레슨런