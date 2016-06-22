CREATE TABLE `user` (
 `id` int(11) NOT NULL auto_increment COMMENT '用户ID',  
 `name` varchar(50) NOT NULL default '' COMMENT '名称',  
 `sex` int(1) NOT NULL default '0' COMMENT '0为男，1为女',  
 PRIMARY KEY  (`id`)  
) ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

insert into user (name,sex)values("tank",1),("zhang",2);



create table `order` (
   `order_id` int(11) not null auto_increment comment '订单ID',  
   `u_id` int(11) not null default '0' comment '用户ID',  
   `username` varchar(50) not null default '' comment '用户名',  
   `money` int(11) not null default '0' comment '钱数',  
   `datetime` timestamp not null default current_timestamp comment '生成时间',
   primary key(`order_id`),  
   index (`u_id`),  
   FOREIGN KEY order_f_key (u_id) REFERENCES user(id)
  )ENGINE=innodb  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

  INSERT INTO `order` (`u_id`, `username`, `money`, `datetime`) VALUES ('1', 'tank','2222', CURRENT_TIMESTAMP);

  SELECT * FROM `order`