#coding=utf8
import torndb
conn = torndb.Connection('localhost', 'carseller', 'root', '11111111')
users = conn.query('select * from user where created_at=%s', '2016-06-15 23:56:3')
users = conn.query('select * from user where created_at=%s', '2016-06-15 23:56:3')

for user in users:
    print user
