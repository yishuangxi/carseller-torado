#coding=utf8
from base import BaseModel
from tornado.gen import coroutine, Return

class UserModel(BaseModel):
    @coroutine
    def find_one_by_id(self, user_id):
        user = yield self.get('select * from user where id=%s', user_id)
        raise Return(user)

    @coroutine
    def create(self, username, password, phone):
        sql = '''insert into user (id, username, password, phone, status, created_at, updated_at)
                             values(null, %s, %s, %s, %s, %s, %s)'''
        status, now = 0, self.now()
        res = yield self.insert(sql, username, password, phone, status, now, now)

        raise Return(res)

    @coroutine
    def find_one_by_username_password(self, username, password):
        sql = '''select * from user where username=%s and password=%s'''
        user = yield self.get(sql, username, password)
        raise Return(user)