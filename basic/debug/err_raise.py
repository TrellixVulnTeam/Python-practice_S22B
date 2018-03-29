# -*- coding: utf-8 -*-


# class FooError(ValueError):
#     pass


# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10/n


# print(foo('0'))

# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：

# -*- coding: utf-8 -*-

from functools import reduce


def str2num(s):
    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
