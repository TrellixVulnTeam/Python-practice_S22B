#!/user/bin/env python3
# -*- coding: utf-8 -*-


# def add(x, y, f):
#     return f(x) + f(y)


# print(add(-5, 6, abs))

def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))
