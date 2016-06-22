DROP DATABASE IF EXISTS carseller;
CREATE DATABASE IF NOT EXISTS carseller DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use carseller;

create table `user`(
  `id` int(11) not null auto_increment,
  `username` varchar(20) not null comment '用户名',
  `password` varchar(20) not null,
  `phone` char(11) not null,
  `created_at` datetime not null DEFAULT now(),
  `updated_at` datetime not null DEFAULT now(),
  PRIMARY KEY (`id`)
) ENGINE=innodb DEFAULT charset=utf8 auto_increment=1;

create table `client`(
  `id` int(11) not null auto_increment,
  `user_id` int(11) not null,
  PRIMARY KEY (`id`),
  FOREIGN KEY client_f_key (`user_id`) REFERENCES `user`(`id`)
) ENGINE=innodb DEFAULT charset=utf8 auto_increment=1;

