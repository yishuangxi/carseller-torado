import tornado.ioloop
import tornado.web
from handler.user import UserHandler
import router.all
if __name__ == "__main__":
    app = tornado.web.Application(router.all.Router, debug=True, autoreload=True)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()