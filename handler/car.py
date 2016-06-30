#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from base import BasePageHandler, BaseApiHandler
from tornado.gen import coroutine, Return
from model.car import CarModel
from service.car import CarService

class BaseCarPageHandler(BasePageHandler):
    pass

class BaseCarApiHandler(BaseApiHandler):
    def __init__(self, *args, **kwargs):
        super(BaseCarApiHandler, self).__init__(*args, **kwargs)

        self.car_model = CarModel()
        self.car_service = CarService()

#page handlers
class CarDetailPageHandler(BaseCarPageHandler):
    @coroutine
    def get(self, car_id):
        self.render('pc/car/detail.html')

class CarListPageHandler(BaseCarPageHandler):
    @coroutine
    def get(self):
        self.render('pc/car/list.html')



#api handlers
class CarDetailApiHandler(BaseCarApiHandler):
    @coroutine
    def get(self, car_id):
        res = yield self.car_model.find_one_by_id(car_id)
        self.res_success(res)

class CarListApiHandler(BaseCarApiHandler):
    @coroutine
    def get(self, car_id):
        res = yield self.car_model.find_one_by_id(car_id)
        self.res_success(res)
