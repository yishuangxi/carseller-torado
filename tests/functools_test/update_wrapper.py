import functools

#update_wrapper把后一个函数的__doc__和__name__拷贝到前一个函数。。。
# 常用于装饰器内部，避免因装饰器而修改原函数的__doc__和__name__属性
def dec1(func):
    def inner_func(*args, **kwargs):
        """inner_func doc str"""
        print 'inner_func before func '
        func(*args, **kwargs)

    return inner_func

@dec1
def func1():
    """func1 doc str"""
    print 'func1 ...'

def dec2(func):
    def inner_func(*args, **kwargs):
        """inner_func doc str"""
        print 'inner_func before func '
        func(*args, **kwargs)

    return functools.update_wrapper(inner_func, func)

@dec2
def func2():
    """func2 doc str"""
    print 'func1 ...'

print func1.__doc__
print func1.__name__

print

print func2.__doc__
print func2.__name__
