#!/user/bin/env python3
# -*- coding: utf-8 -*-

# L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(L)

# f = lambda x : x * x

# print(f(5))

# def build(x, y):
#     return lambda z: x * x + y * y + z

# print(build(2, 3)(5))


# 练习
# 请用匿名函数改造下面的代码：

def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

print(L)

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
