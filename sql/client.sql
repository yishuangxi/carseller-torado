CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

CREATE TABLE IF NOT EXISTS client (
  id INT(10) unsigned not null auto_increment PRIMARY KEY ,
  clientname VARCHAR (20) UNIQUE not NULL ,
  phone CHAR(11) NOT NULL UNIQUE ,
  gender ENUM('男', '女') comment '男， 女',
  car_id INT(11) NOT NULL COMMENT "车型ID",
  level ENUM('A', 'B', 'C', 'D', 'E') COMMENT "A-E由低到高",
  mark_id TINY_INT DEFAULT NULL COMMENT "备注id",
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW()
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

insert into client values(null, 'c1', '18316997339', 'A', now(), now());