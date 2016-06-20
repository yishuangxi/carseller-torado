#coding=utf8
from base import BaseModel
from tornado.gen import coroutine, Return
from model.user import UserModel
from service.user import UserService

class UserModel(BaseModel):
    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)
        self.user_model = UserModel()
        self.user_srv = UserService()
    @coroutine
    def find_one_by_id(self, user_id):
        user = yield self.query('select * from user')
        raise Return(user)

    @coroutine
    def create(self, username, password, phone):
        sql = '''insert into user (id, username, password, phone, status, created_at, updated_at)
                             values(null, %s, %s, %s, %s, %s, %s)'''
        status, now = 0, self.now()
        res = yield self.insert(sql, username, password, phone, status, now, now)

        raise Return(res)