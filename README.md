# TableSetter_encore-final


#### QR생성 부분 때문에 아래 부분 필요
- CMD에서 실행해주세요
```
pip3 install qrcode

pip3 install Pillow

pip3 install pycryptodome
```

### 필요 변수 파일
- POSvariable.py
```
loginVariable = {
    'host': 'YOUER_DBSERVER_IP' ,
    'user':  'YOUER_DBSERVER_USER',
    'password' : 'YOUER_DBSERVER_USER_PW',
    'db' : 'YOUER_DB_NAME',
    'charset' : 'utf8'#한국어 사용시 넣어줘야함.
}
s3Variable = {
'ACCESS_KEY_ID' : 'YOUR_ACCESS_KEY_ID',
'ACCESS_SECRT_KEY' : 'YOUR_ACCESS_SECRT_KEY',
'BUCKET_NAME' : 'YOUR_BUCKET_NAME',
'region': 'used_region'
}

global STORE_ID #로그인시 받아둔 매장번호
global POS_ID   #로그인시 받아둔 ID
global TABLE_NUM #테이블 개수

TABLE_NUM = 10

```
작성후 실행하세요!