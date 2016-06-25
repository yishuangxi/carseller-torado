DROP database if EXISTS carseller;
CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET UTF8 COLLATE UTF8_general_ci;
use carseller;

-- 用戶表
CREATE TABLE `user` (
  `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` VARCHAR(20) NOT NULL COMMENT '用户名',
  `password` VARCHAR(20) NOT NULL,
  `phone` CHAR(11) NOT NULL UNIQUE ,
  `sex` ENUM('男','女', '保密') NOT NULL DEFAULT '保密',
  `status` INT(1) NOT NULL DEFAULT '0' COMMENT '1激活，0为禁用',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`id`)
) ENGINE=innodb  DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1 ;

-- 客戶表
CREATE TABLE `client` (
   `id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '客户ID',
   `clientname` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '客户名',
   `phone` CHAR(11) NOT NULL COMMENT '客户手机号码',
   `sex` ENUM('男','女', '保密') NOT NULL DEFAULT '保密',
   `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
   `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
   PRIMARY KEY (`id`)
  )ENGINE=innodb  DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1;

-- 客户需要记录的历史信息：客户等级变更历史:一对多
CREATE TABLE `client_level`(
  `id` INT(10) NOT NULL AUTO_INCREMENT ,
  `client_id` INT(10) NOT NULL,
  `level` ENUM('A', 'B', 'C', 'D', 'E', 'F') COMMENT '用户等级',
  `mark` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '备注',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
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
  `status` ENUM('已售', '未售', '在途') NOT NULL DEFAULT '在途',
  `price` FLOAT(10, 2) NOT NULL DEFAULT 0 COMMENT '汽车价格',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
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








