import tornado.web
import asynctorndb
import torndb
from tornado.gen import coroutine, Return
import json

class UserHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self):
        conn = yield self.get_connection()
        users = yield conn.query('select * from user')
        print users
        self.write(users[0].username)

    @coroutine
    def get_connection(self):
        conn = asynctorndb.Connection(host='127.0.0.1', database='carseller', user='root', passwd='11111111')
        yield conn.connect()
        raise Return(conn)

if __name__ == "__main__":
    app = tornado.web.Application([(r'/', UserHandler),], debug=True, autoreload=True)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()