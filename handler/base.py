#coding=utf8
from tornado.web import RequestHandler
import json
from datetime import datetime
from datetime import date

from model.car import CarModel
from model.user import UserModel

from service.user import UserService

class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

    def get_current_user(self):
        return self.get_secure_cookie("__token")


class BasePageHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super(BasePageHandler, self).__init__(*args, **kwargs)


class BaseApiHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super(BaseApiHandler, self).__init__(*args, **kwargs)
        self.string     = 'string'
        self.int        = 'int',
        self.float      = 'float'
        self.number     = 'number'

    def res_success(self, data='', msg=''):
        callback = self.get_argument('callback', False)
        if not callback:
            self.write({
                'code': 1,
                'msg': msg,
                'data': self.__json(data)
            })
        else:
            self.write("""

            try{
                %s(%s)
            }catch(err){

            }

            """ % (callback, self.__dumps(data)))

    def res_error(self, msg=''):
        self.write({
            'code': 0,
            'msg': msg
        })

    def __json(self, data):
        return json.loads(self.__dumps(data))

    def __dumps(self, data):
        return json.dumps(data, cls=JsonEncoder)


class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, o)
