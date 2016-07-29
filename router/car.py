from handler.car import CarDetailPageHandler, CarListPageHandler, \
    CarDetailApiHandler, CarListApiHandler


Router = [
    #handler: car
    (r'/car/(\d+)', CarDetailPageHandler),
    (r'/car', CarListPageHandler),
    (r'/api/car/(\d+)', CarDetailApiHandler),
    (r'/api/car/list', CarListApiHandler)
]