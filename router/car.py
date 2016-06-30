from handler.car import CarDetailPageHandler, CarListPageHandler, \
    CarDetailApiHandler, CarListApiHandler


Router = [
    #handler: car
    (r'/car/detail/(\d+)', CarDetailPageHandler),
    (r'/car/list', CarListPageHandler),
    (r'/api/car/detail/(\d+)', CarDetailApiHandler),
    (r'/api/car/list', CarListApiHandler)
]