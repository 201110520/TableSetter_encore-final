# TableSetter_encore-final Frontend POS

## 개요
```
언택트(Untact)비지니스를 위한 멀티 클라우드 아키텍트 양성 과정에서 진행한 
최종 프로젝트 테이블세터 중 포스 및 매장관리 프론트엔드 부분.

개발 언어 : Python 3, PyQt5
개발 환경 : VS code
개발 기간 : 2021. 05. 24 ~ 2021. 06. 21
패키징 : pyinstaller


```
![디비](img/디비.png)

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

![포스 기능]{img/포스 기능.png}
## 기능 상세


 + 점포 등록 
+ >본사 관리자 mode
+ 정포 조회
+ >본사 관리자 mode

* 로그인
* >점포별 계정이 존제
* 관리
    + 매출관리
    * > 기간별 매출 확인 및 저장
    + 재고관리
    + QR코드 생성
    + 메뉴 등록
* 포스 시스템
    + 주문
    + 테이블관리
    + 결제


![포스기1](img/포스기1.jpg)

### 발전 방향

![발전방향](img/발전방향.png)
