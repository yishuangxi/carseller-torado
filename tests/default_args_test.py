#coding=utf8
# import time
# def fn(arg=[]):
#     print arg
#
# fn(arg=[1, 2, 3])
# fn()


###函数默认参数不是惰性求值
# from datetime import datetime
# def test2(t = datetime.today()):
#     print t
# if __name__ == "__main__":
#     print datetime.today()
#     time.sleep(0.5)
#     test2()
#     time.sleep(0.5)
#     test2()


#函数引用类型参数记忆:请注意不要在函数体内修引用类改默认参数
def foo(a1, args = []):
    print "args before = %s" % (args)
    args.insert(0, 10)
    args.insert(0, 99999)
    print "args = %s " % (args)

foo('a')
print
foo('b')
print
foo('c', args=[1,2,3])
print
foo('d')