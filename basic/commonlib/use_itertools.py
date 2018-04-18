#!/user/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# ================================================================
# count

# natuals = itertools.count(1,2)
# for n in natuals:
#     print(n)
#     # 测试停止
#     if n > 10:
#         break

# ================================================================
# cycle

# cs = itertools.cycle('ABCD')
# for c in cs:
#     print(c)

# ================================================================
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# ================================================================
# takewhile

# natuals = itertools.count(1, 2)
# ns = itertools.takewhile(lambda x: x <= 11, natuals)
# print(list(ns))

# ================================================================
# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# ================================================================
# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：

# for key, group in itertools.groupby('ABABBBCCAAA'):
#     print(key, list(group))

# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))

# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']


# ========================================================================================
# 练习
# 计算圆周率可以根据公式：

# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

# -*- coding: utf-8 -*-
# import itertools


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    item_list = itertools.count(1, 2)
    print(item_list)
    item_list = itertools.takewhile(lambda n: n < 2*n - 1, item_list)
    ns = list(map(lambda x: 4 / x, item_list))
    item_list = [ns[x] if x % 2 == 1 else -1 * ns[x] for x in range(len(ns))]
    return sum(item_list)


# 测试:
print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert 3.1414 < pi(10000) < 3.1415
# print('ok')
