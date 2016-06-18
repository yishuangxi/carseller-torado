CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

CREATE TABLE IF NOT EXISTS user (
  id INT(10) unsigned not null auto_increment PRIMARY KEY ,
  username VARCHAR (20)UNIQUE not NULL ,
  password VARCHAR(20) NOT NULL ,
  phone CHAR(11) NOT NULL UNIQUE ,
  status INT(1) DEFAULT 1 COMMENT "1激活状态，0是禁用状态",
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW()
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

insert into user values(null, 'a', '111', '11111111111', 1, now(), now());