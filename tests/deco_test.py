#coding=utf8
#可执行装饰器
def outerDec():
    print 'outer deco start'
    def innerDec(func):
        def dec(*args, **kwargs):
            print 'before func'
            func(*args, **kwargs)
            print 'after func'

        return dec
    return innerDec

@outerDec()
def func(name):
    print 'func is executing ' + name

func('aaa')
func('bbb')

#一层装饰器
# def dec(func):
#     def fn(*args, **kwargs):
#         print 'before func'
#         func(*args, **kwargs)
#         print 'after func'
#
#     return fn
#
# @dec
# def func1(name):
#     print 'func is executing ' + name
#
# func1('aaa')
# func1('bbb')
# func1('ccc')

