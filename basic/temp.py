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

# a = 257
# b = 257

# print(a == b)
# print(a is b)

# def my_squer(n):
#     if n < 0:
#         raise Exception('illegal arg lower than zero')
#     if n == 1 or n == 0:
#         print('value: %.7f' % n)
#         return

#     g = n/2
#     different = 1
#     while different > 0.0001:
#         g = (g + n/g)/2
#         different = abs(g*g - n)

#     print('value: %.7f' % g)


# my_squer(121)

# import math
# import time

# log_2 = math.log(2)


# def log2(x):
#     return math.log(x) / math.log(2)


# def log2_second(x):
#     return math.log(x) / log_2


# start_time = time.time()

# for i in range(99999999):
#     log2(9999999999)

# ent_time = time.time()
# spend_time = ent_time - start_time
# print(spend_time)
# start_time = time.time()

# for i in range(99999999):
#     log2_second(9999999999)

# ent_time = time.time()
# spend_time = ent_time - start_time

# print(spend_time)

# import re

# mail = 'someone@gmail.com'
# mail = '<Tom Paris> tom@voyager.org'
# #   re_mail = re.compile(r'^\w+(\.\w+)?\d*@[\w\d]+\.(com|org)$')
# re_mail = re.compile(r'^(<\w+\s+\w+>)\s+(\w+(\.\w+)?\d*@[\w\d]+\.(com|org))$')
# print(re_mail.match(mail))


# (<\w+\s+\w>)\s+


foo = []
for i in range(1, 6):
    # foo.append((lambda j: (lambda: j))(i))
    foo.append(lambda i= i: i)

for f in foo:
    print(f())
