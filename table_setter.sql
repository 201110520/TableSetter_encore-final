#CREATE DATABASE untact_order_db;
USE untact_order_db;

CREATE TABLE Store(
	num VARCHAR(100) NOT NULL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	position VARCHAR(200) NOT null
) DEFAULT CHARSET=UTF8;

CREATE TABLE Store_Admin(
	id VARCHAR(100) NOT NULL PRIMARY KEY,
	Store_num VARCHAR(100) NOT NULL,
	pw VARCHAR(100),
	name VARCHAR(50),
	FOREIGN KEY(Store_num) REFERENCES Store(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE Store_User(
	id VARCHAR(100) NOT NULL PRIMARY KEY,
	pw VARCHAR(100),
	user_description VARCHAR(100),
	Store_num VARCHAR(100) NOT NULL,
	FOREIGN KEY(Store_num) REFERENCES Store(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE QR_image(
	regist_id VARCHAR(100) NOT NULL PRIMARY KEY,
	Store_num VARCHAR(100) NOT NULL,
	tbl_num INT,
	img_src VARCHAR(100) NOT NULL,
	FOREIGN KEY(Store_num) REFERENCES Store(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE Category(
	num INT PRIMARY KEY AUTO_INCREMENT,
	Store_num VARCHAR(100) NOT NULL,
	NAME VARCHAR(50),
	description VARCHAR(200),
	FOREIGN KEY(Store_num) REFERENCES Store(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE Food(
	num INT PRIMARY KEY AUTO_INCREMENT,
	category_num INT,
	NAME VARCHAR(50) NOT NULL,
	img_src VARCHAR(100) NOT NULL,
	price VARCHAR(50) NOT NULL,
	description VARCHAR(200),
	STATUS BOOLEAN DEFAULT 1 NOT NULL,
	FOREIGN KEY(category_num) REFERENCES Category(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE Menu(
	reg_id INT PRIMARY KEY AUTO_INCREMENT,
	Store_num VARCHAR(100) NOT NULL,
	Food_num INT,
	FOREIGN KEY(Store_num) REFERENCES Store(num),
	FOREIGN KEY(Food_num) REFERENCES Food(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE UserInfo(
	num INT AUTO_INCREMENT PRIMARY KEY,
	device_info VARCHAR(200)
) DEFAULT CHARSET=UTF8;

CREATE TABLE OrderHistory(
	num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	Store_num VARCHAR(100) NOT NULL,
	order_date TIMESTAMP NOT NULL,
	table_num INT,
	pay_state BOOLEAN NOT NULL DEFAULT 0,
	request VARCHAR(100),
	User_num INT NOT NULL ,
	FOREIGN KEY(Store_num) REFERENCES Store(num),
	FOREIGN KEY(User_num) REFERENCES UserInfo(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE OrderDetail(
	num INT PRIMARY KEY AUTO_INCREMENT,
	Order_num INT NOT NULL,
	Food_num INT NOT NULL,
	amount INT NOT NULL,
	pay_code INT NOT NULL, #1=??????, 2= ????????????, 3=????????????
	FOREIGN KEY(Food_num) REFERENCES Food(num),
	FOREIGN KEY(Order_num) REFERENCES OrderHistory(num)
) DEFAULT CHARSET=UTF8;

CREATE TABLE Payment(
	num INT  PRIMARY KEY AUTO_INCREMENT,
	Order_num INT NOT NULL,
	card_id INT(20),
	pay_code INT NOT NULL,
	paid VARCHAR(50) NOT NULL,
	pay_date TIMESTAMP,
	FOREIGN KEY(Order_num) REFERENCES OrderHistory(num)
) DEFAULT CHARSET=UTF8;

ALTER TABLE Payment ADD COLUMN card_id INT(20) ;
ALTER TABLE Payment ADD COLUMN  paid VARCHAR(50) NOT NULL;

CREATE TABLE SystemAdmin(
	id VARCHAR(100) PRIMARY KEY,
	pw VARCHAR(100) NOT NULL,
	NAME VARCHAR(100)
) DEFAULT CHARSET=UTF8;

INSERT INTO Store VALUES ( '6rSA66as7J6Q', '?????????', '123.14, 123.214'); 
INSERT INTO Store_Admin VALUES 
('burgerking', '67KE6rGw7YK5',PASSWORD('burgerking'),'?????????'),
('hongkong', '7ZmN7L2p67CY7KCQ',PASSWORD('hongkong'),'????????????'),
('sixtychicken', 'NjDqs4TsuZjtgqg=',PASSWORD('sixtychicken'),'60?????????')
;
INSERT INTO UserInfo (device_info) VALUES 
('awer23'),
('vfeh43');
INSERT INTO OrderHistory (Store_num,table_num, request,User_num ) VALUES
('7ZmN7L2p67CY7KCQ', 3, '????????? ????????????~', 1),
('7ZmN7L2p67CY7KCQ', 3, '????????? ????????????~', 1),
('7ZmN7L2p67CY7KCQ', 2, '???  ????????????~', 2);

INSERT INTO OrderDetail ( Order_num, Food_num, amount) VALUES
(3, 14 ,2),
(3, 16 ,1),
(3, 19 ,1),
(4, 15 ,1),
(4, 16 ,1);

UPDATE OrderHistory SET pay_state = 0 WHERE num=4