CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;

-- 静态数据表
CREATE TABLE IF NOT EXISTS mark (
  id INT(10) unsigned not null auto_increment PRIMARY KEY ,
  content VARCHAR(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

insert into mark values(null, '对比竞品再考虑');
insert into mark values(null, '下班再过来一趟');
insert into mark values(null, '两天内买车');
insert into mark values(null, '等老公/老婆一起来看');