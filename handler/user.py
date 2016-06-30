#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from base import BasePageHandler, BaseApiHandler
from tornado.gen import coroutine, Return
from model.user import UserModel
from service.user import UserService

class BaseUserPageHandler(BasePageHandler):
    pass

class BaseUserApiHandler(BaseApiHandler):
    def __init__(self, *args, **kwargs):
        super(BaseApiHandler, self).__init__(*args, **kwargs)
        self.user_model = UserModel()
        self.user_service = UserService()

#page handlers
class RegisterPageHandler(BaseUserPageHandler):
    @coroutine
    def get(self):
        self.render('pc/user/register.html')

class LoginPageHandler(BaseUserPageHandler):
    @coroutine
    def get(self):
        self.render('pc/user/login.html')

class UserPageHandler(BaseUserPageHandler):
    @coroutine
    def get(self):
        user_id = 1
        user = yield self.user_model.find_one_by_id(user_id)
        self.render('pc/user/user.html')


#api handlers
class RegisterApiHandler(BaseUserApiHandler):
    @coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        phone    = self.get_argument('phone')
        sex = self.get_argument('sex', 'secret')

        print username, password, phone, sex
        res = yield self.user_model.create(username, password, phone, sex)
        self.write(str(res))

class PasswordApiHandler(BaseUserApiHandler):
    pass

class LoginApiHandler(BaseUserApiHandler):
    @coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        res = yield self.user_model.find_one_by_username_and_password(username, password)

        if res:
            self.res_success(res)
        else:
            self.res_error('用户名或密码错误')

class UserApiHandler(BaseUserApiHandler):
    @coroutine
    def get(self, user_id):
        res = yield self.user_model.find_one_by_id(user_id)
        self.res_success(res)
