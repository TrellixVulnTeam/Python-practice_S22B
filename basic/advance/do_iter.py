#!/user/bin/env python3
# -*- coding: utf-8 -*-

# d = {'a': 1, 'b': 2, 'c': 3}

# for key in d:
#     print("%s haha %s" % (key, d[key]))

# for key in d.keys():
#     print("%s haha %s" % (key, d[key]))

# print(d.keys())
# print(d.values())
# print(d.items())

# for ch in 'ABC':
#     print(ch)

# from collections import Iterable


# print(isinstance('abc', Iterable))  # str是否可迭代
# print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
# print(isinstance(123, Iterable))  # 整数是否可迭代
# print(isinstance({}, Iterable))

# L = ['A', 'B', 'C']
# for value in L:
#     print(value)

# for i in range(len(L)):
#     print(i)

# print(list(enumerate(L)))

# for i, value in enumerate(L):
#     print(i, value, L[i])

# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

# def findMinAndMax(L):
#     min = None
#     max = None
#     for item in L:
#         if min == None or min > item:
#             min = item
#         if max == None or max < item:
#             max = item
#     return (min, max)


# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')


from collections import Iterator
from collections import Iterable

# print(isinstance((x for x in range(10)), Iterator))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance([x for x in range(10)], Iterator))
# print(isinstance([x for x in range(10)], Iterable))

# print(isinstance('abc', Iterator))
# print(isinstance(iter('abc'), Iterator))

# print(iter('abc'))

# g = iter('abc')
# print(next(g))
# print(next(g))
# print(next(g))

for x in [1, 2, 3, 4, 5]:
    pass
# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
