DROP database if EXISTS carseller;

CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

-- 用戶表
CREATE TABLE `user` (
  `id` INT(11) NOT NULL auto_increment COMMENT '用户ID',
  `username` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '用户名',
  `password` VARCHAR(20) NOT NULL,
  `phone` CHAR(11) DEFAULT NULL ,
  `sex` enum('男','女') DEFAULT NULL ,
  `status` INT(1) NOT NULL DEFAULT '0' COMMENT '1激活，0为禁用',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp comment '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp comment '创建时间',
  PRIMARY KEY  (`id`)
) ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 客戶表
CREATE TABLE `client` (
   `id` INT(11) NOT NULL auto_increment comment '客户ID',
   `clientname` VARCHAR(50) NOT NULL DEFAULT '' comment '客户名',
   `phone` INT(11) NOT NULL DEFAULT '0' comment '客户手机号码',
   `sex` enum('男','女') DEFAULT NULL ,
   `created_at` timestamp NOT NULL DEFAULT current_timestamp comment '创建时间',
   `updated_at` timestamp NOT NULL DEFAULT current_timestamp comment '创建时间',
   PRIMARY KEY (`id`)
  )ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

-- 用户-客户关系表：一个客户对应一个用户，一个用户对应多个客户
CREATE TABLE r_user_client(
  `id` INT(11) NOT NULL auto_increment comment '关系表id',
  `user_id` INT(11) NOT NULL ,
  `client_id` INT(11) NOT NULL UNIQUE ,
  PRIMARY KEY (`id`),
  FOREIGN KEY f_key_1 (user_id) REFERENCES user(id),
  FOREIGN KEY f_key_2 (client_id) REFERENCES client(id)
) ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

-- 汽车表
CREATE TABLE IF NOT EXISTS car (
  `id` INT(10) unsigned not null auto_increment PRIMARY KEY,
  `vin` VARCHAR(20) NOT NULL UNIQUE COMMENT '车架号，唯一标记',
  `name` VARCHAR(20) DEFAULT NULL COMMENT '车名字',
  `color` INT(1) COMMENT '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10',
  `model` VARCHAR(20) NOT NULL COMMENT '车型号',
  `created_at` DATETIME DEFAULT NOW(),
  `updated_at` DATETIME DEFAULT NOW()
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;