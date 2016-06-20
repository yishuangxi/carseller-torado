CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

CREATE TABLE IF NOT EXISTS car (
  id INT(10) unsigned not null auto_increment PRIMARY KEY ,
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW()
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

insert into car values(null, 'car1', '18316997339', 'A', now(), now());