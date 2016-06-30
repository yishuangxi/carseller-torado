#coding=utf8
from base import BaseModel
from tornado.gen import coroutine, Return

class CarModel(BaseModel):
    @coroutine
    def find_one_by_id(self, car_id):
        res = yield self.get('select * from car where id=%s', car_id)
        raise Return(res)

    @coroutine
    def find(self, vin='', color='', model='', status='', min_price='', max_price='', created_at='', page=1, page_count=20):
        configs = [
            {'key': 'vin', 'value': vin, 'filter_type': 'like'},
            {'key': 'color', 'value': color, 'filter_type': '='},
            {'key': 'model', 'value': model, 'filter_type': '='},
            {'key': 'status', 'value': status, 'filter_type': '='},
            {'key': 'min_price', 'value': min_price, 'filter_type': '>'},
            {'key': 'max_price', 'value': vin, 'max_price': '<'},
            {'key': 'created_at', 'value': created_at, 'filter_type': '='}
        ]
        # filter_sql_list = []
        # if vin:
        #     filter_sql_list.append('vin like {0}'.format('%' + vin + '%'))
        # if color:
        #     filter_sql_list.append('color={0}'.format(color))
        # if model:
        #     filter_sql_list.append('model={0}'.format(model))
        # if status:
        #     filter_sql_list.append('status={0}'.format(model))
        # if min_price:
        #     filter_sql_list.append('min_price>{0}'.format(min_price))
        # if max_price:
        #     filter_sql_list.append('max_price={0}'.format(max_price))
        # if created_at:
        #     filter_sql_list.append('created_at={0}'.format(created_at))


        filter_sql = self.get_filter_sql(*configs)
        limit_sql = ' limit {0}, {1}'.format(page - 1, page_count)
        sql = filter_sql + limit_sql

        print 'sql: '+ sql
        res = yield self.query(sql)
        raise Return(res)