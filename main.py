import tornado.ioloop
import tornado.web
import router.all
from settings.main_settings import settings
if __name__ == "__main__":
    app = tornado.web.Application(router.all.Router, **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()