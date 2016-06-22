CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

-- 客户基本信息
CREATE TABLE IF NOT EXISTS client (
  `id` INT(10) unsigned not null auto_increment PRIMARY KEY ,
  `name` VARCHAR (20) not NULL ,
  `phone` CHAR(11) NOT NULL ,
  `gender` int(1) COMMENT '1: 男，0: 女',
  `created_at` DATETIME DEFAULT NOW(),
  `updated_at` DATETIME DEFAULT NOW()
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;

insert into client values (1, 'client_1', '18888888881', 0, now(), now());
insert into client values (2, 'client_2', '18888888882', 1, now(), now());
insert into client values (3, 'client_3', '18888888883', 1, now(), now());

-- 客户需求信息
CREATE TABLE IF NOT EXISTS client_demand(
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `client_id` INT(10) NOT NULL,
  `car_id` INT(10) NOT NULL COMMENT "车型ID",
  `mark` VARCHAR(200) DEFAULT NULL COMMENT "备注",
  `created_at` DATETIME DEFAULT NOW(),
  `updated_at` DATETIME DEFAULT NOW(),
  FOREIGN KEY f_key1 (`car_id`) REFERENCES `car`(`id`),
  FOREIGN KEY f_key2 (`client_id`) REFERENCES `client`(`id`)
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;
insert into client_demand values (1, 1, 1, '备注1', now(), now()),
                                 (2, 2, 2, '备注2', now(), now()),
                                 (3, 3, 3, '备注3', now(), now());


-- 客户需要记录的历史信息：客户等级变更历史:一对多
CREATE TABLE IF NOT EXISTS client_level(
  `id` INT(10) unsigned not null auto_increment PRIMARY KEY ,
  `client_id` INT(10) NOT NULL,
  `level` CHAR(1) comment 'A, B, C, D, E, F',
  `created_at` DATETIME DEFAULT NOW(),
  index(`client_id`),
  FOREIGN KEY client_level_f_key (`client_id`) REFERENCES `client` (`id`)
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;

insert into client_level values (1, 1, 'A', now());
insert into client_level values (2, 1, 'B', now());
insert into client_level values (3, 2, 'C', now());
insert into client_level values (4, 2, 'D', now());

-- 客户和销售人员关系表：1个client只能有1个user，1个user可以多个client
CREATE TABLE rs_user_client(
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `user_id` INT(10) NOT NULL,
  `client_id` INT(10) NOT NULL UNIQUE COMMENT "这个关系表里面，客户id必须唯一",
  FOREIGN KEY f_key1 (`user_id`) REFERENCES user(`id`) ,
  FOREIGN KEY f_key2 (`client_id`) REFERENCES client(`id`)
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;

insert into rs_user_client values (1, 1, 1), (2, 2, 2), (3, 3, 3);