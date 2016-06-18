#coding=utf8
import functools

#partial函数的python实现
def partial(func, *args, **kwargs):
    def new_func(*fargs, **fkwargs):
        new_args = args + fargs
        new_kwargs = kwargs.copy()
        new_kwargs.update(fkwargs)
        return func(*new_args, **new_kwargs)

    new_func.func = func
    new_func.args = args
    new_func.kwargs = kwargs

    return new_func


def add(a, b):
    return a+b

add3 = functools.partial(add, 3)

print add3(4)
print add3(5)

def show_user(name, age):
    print 'name: ' + str(name) + ' age: ' + str(age)

show_yisx = partial(show_user, name='yisx')

show_yisx(age=25)
show_yisx(age=22)
