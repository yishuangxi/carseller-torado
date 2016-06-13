import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado import gen

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        data = yield self.fetch_json('http://www.jd.com')
        self.write(data)

    @gen.coroutine
    def fetch_json(self, url):
        response = yield tornado.httpclient.AsyncHTTPClient().fetch(url)
        raise gen.Return(response.body)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()




