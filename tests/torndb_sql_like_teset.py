import torndb

conn = torndb.Connection('localhost', 'carseller', 'root', '11111111')

user = 'user1'
password = '111'
res = conn.query('select * from user where username=%s and password=%s', user, password)

print res