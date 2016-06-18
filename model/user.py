#coding=utf8
from base import BaseModel
from tornado.gen import coroutine, Return
class UserModel(BaseModel):

    @coroutine
    def get_user_by_id(self, user_id):
        user = yield self.query('select * from user')
        raise Return(user)