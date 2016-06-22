CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

CREATE TABLE IF NOT EXISTS user (
  `id` INT(10) unsigned not null auto_increment PRIMARY KEY ,
  `name` VARCHAR (20) UNIQUE not NULL ,
  `password` VARCHAR(20) NOT NULL ,
  `phone` CHAR(11) NOT NULL UNIQUE ,
  `status` INT(1) DEFAULT 1 COMMENT "1激活状态，0是禁用状态",
  `created_at` DATETIME DEFAULT NOW(),
  `updated_at` DATETIME DEFAULT NOW()
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;

insert into user values(1, 'user1', '111', '16666666661', 1, now(), now());
insert into user values(2, 'user2', '111', '16666666662', 1, now(), now());
insert into user values(3, 'user3', '111', '16666666663', 1, now(), now());