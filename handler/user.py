#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
        username = self.get_argument('username')
        password = self.get_argument('password')
        phone    = self.get_argument('phone')
        sex = self.get_argument('sex', 'secret')

        print username, password, phone, sex
        res = yield self.user_model.create(username, password, phone, sex)
        self.write(str(res))

class PasswordApiHandler(BaseApiHandler):
    pass

class LoginApiHandler(BaseApiHandler):
    @coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        res = yield self.user_model.find_one_by_username_and_password(username, password)

        if res:
            self.res_success(res)
        else:
            self.res_error('用户名或密码错误')

class UserApiHandler(BaseApiHandler):
    @coroutine
    def get(self):
        pass
