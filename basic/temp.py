#!/user/bin/env python3
# -*- coding: utf-8 -*-


def test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


g = test()

print(list(filter(lambda x: x < 100, test())))


# def _not_divisible(n):
#     return lambda x: x % n > 0


# print(filter(_not_divisible(3), [1, 2 ,3 ,4 ,5 ,6 ,7]))


print([x for x in test() if x % 3 > 0])
