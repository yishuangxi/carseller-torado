DROP database if EXISTS carseller;
CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET UTF8 COLLATE UTF8_general_ci;
use carseller;

-- 用戶表
CREATE TABLE `user` (
  `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` VARCHAR(20) NOT NULL COMMENT '用户名',
  `password` VARCHAR(20) NOT NULL,
  `phone` CHAR(11) NOT NULL UNIQUE ,
  `sex` ENUM('male','female', 'secret') NOT NULL DEFAULT 'secret',
  `status` ENUM('disabled', 'enabled') NOT NULL DEFAULT 'enabled',
  `created_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '创建时间',
  `updated_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '更新时间',
  PRIMARY KEY  (`id`)
) ENGINE=innodb  DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1 ;

-- 客戶表
CREATE TABLE `client` (
   `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '客户ID',
   `clientname` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '客户名',
   `phone` CHAR(11) NOT NULL COMMENT '客户手机号码',
   `sex` ENUM('male','female', 'secret') NOT NULL DEFAULT 'secret',
   `created_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '创建时间',
   `updated_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '更新时间',
   PRIMARY KEY (`id`)
  )ENGINE=innodb  DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1;

-- 客户需要记录的历史信息：客户等级变更历史:一对多
CREATE TABLE `r_client_level`(
  `id` INT(10) NOT NULL AUTO_INCREMENT ,
  `client_id` INT(10) NOT NULL,
  `level` ENUM('A', 'B', 'C', 'D', 'E', 'F') COMMENT '用户等级',
  `mark` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '备注',
  `created_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '创建时间',
  `updated_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '更新时间',
  PRIMARY KEY(`id`),
  FOREIGN KEY f_key_1 (`client_id`) REFERENCES `client`(`id`)
) ENGINE=innodb DEFAULT CHARACTER SET=UTF8 AUTO_INCREMENT=1;

-- 用户-客户关系表：一个客户对应一个用户，一个用户对应多个客户
CREATE TABLE `r_user_client`(
  `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '关系表id',
  `user_id` INT(10) NOT NULL COMMENT '用户id无需唯一',
  `client_id` INT(10) NOT NULL UNIQUE COMMENT '客户id要唯一',
  PRIMARY KEY (`id`),
  FOREIGN KEY f_key_1 (`user_id`) REFERENCES `user`(`id`),
  FOREIGN KEY f_key_2 (`client_id`) REFERENCES `client`(`id`)
) ENGINE=innodb  DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1;

-- 汽车表
CREATE TABLE `car` (
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `vin` VARCHAR(20) NOT NULL UNIQUE COMMENT '车架号，唯一标记',
  `color` VARCHAR(20) NOT NULL DEFAULT '',
  `model` VARCHAR(20) NOT NULL COMMENT '车型号',
  `status` ENUM('sold', 'selling', 'onway') NOT NULL DEFAULT 'onway',
  `price` FLOAT(10, 2) NOT NULL DEFAULT 0 COMMENT '汽车价格',
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`)
) ENGINE=innodb DEFAULT CHARACTER SET=UTF8 AUTO_INCREMENT=1 ;

-- -- 订单表
CREATE TABLE `order`(
  `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '关系表id',
  `payment` FLOAT(10, 2) NOT NULL DEFAULT 0 COMMENT '实付款',
  `car_id` INT(10) NOT NULL COMMENT '用户id无需唯一',
  `client_id` INT(10) NOT NULL UNIQUE COMMENT '客户id要唯一',
  PRIMARY KEY (`id`),
  FOREIGN KEY f_key_1 (`car_id`) REFERENCES `car`(`id`),
  FOREIGN KEY f_key_2 (`client_id`) REFERENCES `client`(`id`)
) ENGINE=innodb DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1;


-- 插入用户数据
insert into user VALUES(NULL, 'user1', '111', '16666666661', 'male', 'enabled', NOW(), NOW());
insert into user VALUES(NULL, 'user2', '111', '16666666662', 'female', 'enabled', NOW(), NOW());
insert into user VALUES(NULL, 'user3', '111', '16666666663', 'secret', 'disabled', NOW(), NOW());


-- 插入客户数据
insert into client VALUES (1, 'clientname1', '18888888881', 'male', NOW(), NOW());
insert into client VALUES (2, 'clientname2', '18888888882', 'female', NOW(), NOW());
insert into client VALUES (3, 'clientname3', '18888888883', 'secret', NOW(), NOW());

-- 插入client的level变更数据
insert into r_client_level VALUES(NULL, 1, 'A', '备注1', NOW(), NOW());
insert into r_client_level VALUES(NULL, 1, 'B', '备注2', NOW(), NOW());
insert into r_client_level VALUES(NULL, 1, 'F', '备注3', NOW(), NOW());
insert into r_client_level VALUES(NULL, 2, 'A', '备注1', NOW(), NOW());
insert into r_client_level VALUES(NULL, 2, 'C', '备注2', NOW(), NOW());
insert into r_client_level VALUES(NULL, 3, 'F', '备注1', NOW(), NOW());

-- 插入用户和客户关系数据
insert into r_user_client VALUES (NULL, 1, 1);
insert into r_user_client VALUES (NULL, 2, 2);
insert into r_user_client VALUES (NULL, 3, 3);

-- 插入汽车数据
insert into car values (NULL, 'vin1', 'color1', 'model1', 'sold', 188881.69, NOW(), NOW());
insert into car values (NULL, 'vin2', 'color2', 'model2', 'selling', 188882.69, NOW(), NOW());
insert into car values (NULL, 'vin3', 'color3', 'model3', 'onway', 188883.69, NOW(), NOW());
















