#!/user/bin/env python3
# -*- coding: utf-8 -*-


# def test():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6


# g = test()

# print(list(filter(lambda x: x < 100, test())))


# def _not_divisible(n):
#     return lambda x: x % n > 0


# print(filter(_not_divisible(3), [1, 2 ,3 ,4 ,5 ,6 ,7]))


# print([x for x in test() if x % 3 > 0])

# import functools

# def f1(x, y=2):
#     print('x = ' + str(x) + ' , y = ' + str(y))


# # kw = {'x': 4, 'y': 5}

# # f1(**kw)

# f2 = functools.partial(f1, **{'x': 4, 'y': 5})
# f2()

# def _not_divisible(n):
#     return lambda x: x % n > 0


# def _do_itec():
#     n = 3
#     while True:
#         yield n
#         n += 2


# def primes():
#     yield 2
#     it = _do_itec()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)


# for i in primes():
#     if i < 100:
#         print(i)
#     else:
#         break


# import os

# L = [d for d in os.listdir('.')]
# print(L)

# a = 'A81110101_昗弨巇條_僕儑僀儞僩嵽僞僀僾抐柺.dwg'.encode('ansi')
# print(a.decode('Shift_JIS'))

a = 257
b = 257

print(a == b)
print(a is b)