#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from base import BasePageHandler, BaseApiHandler
from tornado.gen import coroutine, Return

#page handlers
class CarDetailPageHandler(BasePageHandler):
    @coroutine
    def get(self, car_id):
        self.render('pc/car/detail.html')

class CarListPageHandler(BasePageHandler):
    @coroutine
    def get(self):
        self.render('pc/car/list.html')



#api handlers
class CarDetailApiHandler(BaseApiHandler):
    @coroutine
    def get(self, car_id):
        res = yield self.car_model.find_one_by_id(car_id)
        self.res_success(res)

class CarListApiHandler(BaseApiHandler):
    @coroutine
    def get(self, car_id):
        res = yield self.car_model.find_one_by_id(car_id)
        self.res_success(res)
