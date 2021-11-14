# TableSetter_encore-final

## 개요
```
언택트(Untact)비지니스를 위한 멀티 클라우드 아키텍트 양성 과정에서 진행한 
최종 프로젝트 테이블세터 중 포스 및 매장관리 프론트엔드 부분.
```


#### QR생성 부분 때문에 아래 부분 필요
- CMD에서 실행해주세요
```
pip3 install qrcode

pip3 install Pillow

pip3 install pycryptodome

pip3 install boto3
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

## 기능 상세

* 관리
    + 매출관리
        -기간별 매출 확인 및 저장
    + 재고관리
    + QR코드 생성
    + 메뉴 등록
* 포스 시스템
    + 주문
    + 테이블관리
    + 결제
