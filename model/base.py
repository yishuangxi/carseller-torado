#coding:utf8

import asynctorndb
from tornado.gen import coroutine, Return

class BaseModel(object):
    def __init__(self):
        super(BaseModel, self).__init__()

    @coroutine
    def __get_connection(self):
        conn = asynctorndb.Connection(host='localhost', database='carseller', user='root', passwd='11111111')
        yield conn.connect()
        raise Return(conn)

    @coroutine
    def query(self, sql, *args, **kwargs):
        conn = yield self.__get_connection()
        res = yield conn.query(sql, *args, **kwargs)
        raise Return(res)

