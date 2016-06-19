#coding=utf8
from tornado.web import RequestHandler
from model.user import UserModel
from service.user import UserService
import json
from datetime import datetime
from datetime import date

class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.user_model = UserModel()
        self.user_srv = UserService()


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

    def json(self, data):
        return json.loads(self.dumps(data))

    def dumps(self, data):
        return json.dumps(data, cls=JsonEncoder)

    def res_success(self, data='', msg=''):
        callback = self.get_argument('callback', False)
        if callback:
            self.write({
                'code': 0,
                'msg': msg,
                'data': self.json(data)
            })
        else:
            self.write("""

            try{
                %s(%s)
            }catch(err){

            }

            """ % (callback, self.dumps(data)))

    def res_error(self):
        pass

    def __json(self, data, code=0, msg=''):
        self.write({
            'code': code,
            'msg': msg,
            'data': data
        })

    def __jsonp(self):
        pass

class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, o)
