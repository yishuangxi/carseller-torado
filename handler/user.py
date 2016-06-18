from base import BaseHandler
from tornado.gen import coroutine, Return
from model.user import UserModel
class UserHandler(BaseHandler):
    user_model = UserModel()
    @coroutine
    def get(self):
        user_id = 1
        user = yield self.user_model.get_user_by_id(user_id)
        print user
        self.write(user[0].username)