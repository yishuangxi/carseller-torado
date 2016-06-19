from base import BasePageHandler, BaseApiHandler
from tornado.gen import coroutine, Return


class UserPageHandler(BasePageHandler):
    @coroutine
    def get(self):
        user_id = 1
        user = yield self.user_model.find_one_by_id(user_id)
        # self.write(user[0].username)
        self.render('pc/index.html')


class LoginHandler(BaseApiHandler):
    pass


class RegisterHandler(BaseApiHandler):
    def __init__(self):
        super(RegisterHandler, self).__init__()

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        phone    = self.get_argument('phone')

        # self.user_model.insert()



class UserInfoHandler(BaseApiHandler):
    @coroutine
    def get(self):
        pass


class ResetPasswordHandler(BaseApiHandler):
    pass


class UserNameApiHandler(BaseApiHandler):
    pass


class UserPhoneApiHandler(BaseApiHandler):
    pass



