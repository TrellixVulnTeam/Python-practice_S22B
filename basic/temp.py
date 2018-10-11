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


# foo = []
# for i in range(1, 6):
#     # foo.append((lambda j: (lambda: j))(i))
#     foo.append(lambda i= i: i)

# for f in foo:
#     print(f())

# import socket
# import time


# def get_host_ip():
#     sock = socket.create_connection(('ns1.dnspod.net', 6666))
#     sock.settimeout(10)
#     ip = sock.recv(16)
#     sock.close()
#     return ip


# def local_log(file_name, text):
#     fo = open(file_name, "a")
#     strTime = time.asctime(time.localtime(time.time()))
#     # print strTime
#     fo.write(strTime+" ip:"+text)
#     fo.close()


# print(get_host_ip())
# domain_ip = socket.gethostbyname("vlzz.xyz")
# print(domain_ip)

# ip = b'27.184.48.50';
# print(str(ip))
# print(str(ip) == domain_ip)

# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     d = {}
#     # for i in range(len(nums)):
#     #     d[nums[i]] = i
#     # for i in range(len(nums)):
#     #     last_num = target - nums[i]
#     #     if last_num in d and d[last_num] != i:
#     #         return [i, last_num]
#     for i in  range(len(nums)):
#         other_num = target - nums[i]
#         if other_num in d:
#             return [d[other_num]+1, i+1]
#         d[nums[i]] = i

# nums = [2, 7, 11, 15]
# target = 9

# print(twoSum(nums, target))

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# def by_start(interval):
#     return interval.start


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x.start)
    L = []
    last_end = 0
    for i in range(len(intervals)):
        if i == 0:
            L.append([intervals[0].start, intervals[0].end])
        elif intervals[i].start <= last_end:
            if intervals[i].end > last_end:
                L[-1][-1] = intervals[i].end
        else:
            L.append([intervals[i].start, intervals[i].end])
        last_end = L[-1][-1]
    return L


# intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
intervals = [Interval(0, 2), Interval(1, 4), Interval(3, 5)]
print(merge(intervals))
