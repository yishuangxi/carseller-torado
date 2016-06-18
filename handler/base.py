#coding=utf8
from tornado.web import RequestHandler
from model.user import UserModel
from service.user import UserService

class BaseHandler(RequestHandler):
    user_model = UserModel()
    user_srv = UserService
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)


class BasePageHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)


class BaseApiHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super(object, self).__init__(*args, **kwargs)
        self.string = 'string'
        self.int = 'int',
        self.float = 'float'
        self.number = 'number'

