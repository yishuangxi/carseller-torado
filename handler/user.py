from base import BaseHandler

class UserHandler(BaseHandler):
    def get(self):
        self.write('hello')