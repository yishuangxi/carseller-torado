DROP database if EXISTS carseller;

CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use carseller;


CREATE TABLE `user` (
 `id` int(11) NOT NULL auto_increment COMMENT '用户ID',  
 `name` varchar(50) NOT NULL default '' COMMENT '名称',  
 `sex` int(1) NOT NULL default '0' COMMENT '0为男，1为女',
 PRIMARY KEY  (`id`)  
) ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


create table `client` (
   `id` int(11) not null auto_increment comment '订单ID',  
   `username` varchar(50) not null default '' comment '用户名',
   `money` int(11) not null default '0' comment '钱数',  
   `datetime` timestamp not null default current_timestamp comment '生成时间',
   primary key(`id`)
  )ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

create table r_user_client(
  `id` int(11) not null auto_increment comment '关系表id',
  `user_id` INT(11) NOT NULL ,
  `client_id` INT(11) NOT NULL UNIQUE ,
  PRIMARY KEY (`id`),
  FOREIGN KEY f_key_1 (user_id) REFERENCES user(id),
  FOREIGN KEY f_key_2 (client_id) REFERENCES client(id)
) ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;