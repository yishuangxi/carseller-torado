import tornado.web

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')