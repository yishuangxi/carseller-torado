from base import BasePageHandler, BaseApiHandler
from tornado.gen import coroutine, Return

#page handlers
class RegisterPageHandler(BasePageHandler):
    @coroutine
    def get(self):
        self.render('pc/user/register.html')

class LoginPageHandler(BasePageHandler):
    @coroutine
    def get(self):
        self.render('pc/user/login.html')

class UserPageHandler(BasePageHandler):
    @coroutine
    def get(self):
        user_id = 1
        user = yield self.user_model.find_one_by_id(user_id)
        self.render('pc/user/user.html')


#api handlers
class RegisterApiHandler(BaseApiHandler):
    @coroutine
    def post(self):
        print 'register api handler ...'
        username = self.get_argument('username')
        password = self.get_argument('password')
        phone    = self.get_argument('phone')

        res = yield self.user_model.create(username, password, phone)
        self.write(str(res))

class PasswordApiHandler(BaseApiHandler):
    pass

class LoginApiHandler(BaseApiHandler):
    @coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        res = yield self.user_model.find_one_by_username_password(username, password)
        self.res_success(res)

class UserApiHandler(BaseApiHandler):
    @coroutine
    def get(self):
        pass
