CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

-- 车的最基本的信息
CREATE TABLE IF NOT EXISTS car (
  `id` INT(10) unsigned not null auto_increment PRIMARY KEY,
  `vin` VARCHAR(20) NOT NULL UNIQUE COMMENT '车架号，唯一标记',
  `name` VARCHAR(20) DEFAULT NULL COMMENT '车名字',
  `model` VARCHAR(20) NOT NULL COMMENT '车型号',
  `created_at` DATETIME DEFAULT NOW(),
  `updated_at` DATETIME DEFAULT NOW()
) ENGINE=innodb DEFAULT CHARACTER SET=utf8;

insert into car values(1, 'vin-1', 'name-S6幻影', 'model-S6', now(), now());
insert into car values(2, 'vin-2', 'name-S7幻影', 'model-S7', now(), now());
insert into car values(3, 'vin-3', 'name-S8幻影', 'model-S8', now(), now());