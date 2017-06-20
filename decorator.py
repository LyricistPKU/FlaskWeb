# -*- encoding=UTF-8 -*-
# 装饰器，Java当中的注解


def log(level):  # 传入函数指针
    def inner(func):
        def wrapper(*args, **kvargs):  # 一个*表示无名字的参数，相当于一个tuple，两个表示有名字的，相当于一个dict
            print 'before calling', func.__name__
            print level, 'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print 'end calling', func.__name__
        return wrapper
    return inner


@log(level='INFO')  # log level
def hello(name, age):    # 把hello()传入log函数
    print 'hello', name, age


if __name__ == '__main__':
    # hello(name='Calvin', age=23)  # log(hello())
    hello('Calvin', 23)  # log(hello())
