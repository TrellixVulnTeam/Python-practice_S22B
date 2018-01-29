#!/user/bin/env python3
# -*- coding: utf-8 -*-


# def is_odd(n):
#     return n % 2 == 0

# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# def not_empty(s):
#     return s and s.strip()

# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# # 结果: ['A', 'B', 'C']


# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]


# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


# ===================================================================================================
#  SORTED

# L = sorted([36, 5, -12, 9, -21])
# print(L)

# L = sorted([36, 5, -12, 9, -21], key=abs)
# print(L)

# L = sorted(['bob', 'about', 'Zoo', 'Credit'])
# print(L)

# L = sorted(['bob', 'about', 'Zoo', 'Credit'], reverse=True)
# print(L)

# L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# print(L)

# # 练习
# # 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # 请用sorted()对上述列表分别按名字排序：


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# def by_name(t):
#     return t[0]


# L2 = sorted(L, key=by_name)
# print(L2)

# 再按成绩从高到低排序：


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# def by_score(t):
#     return t[1]


# L2 = sorted(L, key=by_score, reverse=True)
# print(L2)


# =====================================================================

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for p in primes():
    if p < 1000:
        print(p)
