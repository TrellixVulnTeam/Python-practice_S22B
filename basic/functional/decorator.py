#!/user/bin/env python3
# -*- coding: utf-8 -*-


# def now():
#     print('2015-3-25')


# f = now

# print(now.__name__)
# print(f.__name__)


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s' % func.__name__)
#         return func(*args, ** kw)
#     return wrapper


# @log
# def now():
#     print('2015-3-25')


# now()

# print(now.__name__)


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log('execute')
# def now():
#     print('2015-3-25')

# now()

# print(now.__name__)

# import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# def now():
#     print('2015-3-25')


# now()
# print(now.__name__)

# now = log('execute')(now)

# now()
# print(now.__name__)

# ===========================================================================================
# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

# import time
# import functools


# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start_time = time.time()
#         result = fn(*args, **kw)
#         print('%s executed in %s ms' % (fn.__name__, time.time() - start_time))
#         return result
#     return wrapper

# # 测试


# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y


# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z


# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# ===========================================================================================
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

# 再思考一下能否写出一个@log的decorator，使它既支持：

# @log
# def f():
#     pass
# 又支持：

# @log('execute')
# def f():
#     pass


def log(text=None):
    def decorator(func):
        def wrapper(*args, **kw):
            print('begin call')
            result = func(*args, **kw)
            print('end call')
            return result
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


@log()
def again():
    print('2015-3-26')


now()
again()
