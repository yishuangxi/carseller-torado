#coding=utf8

class A(object):

    def __init__(self):
        super(A, self).__init__()
        self.name = 'yisx'

    def getName(self):
        return self.name

class B(A):
    def __init__(self):
        super(B, self).__init__()

b = B()
print b.getName()