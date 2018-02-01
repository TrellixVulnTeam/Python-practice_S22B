#!/user/bin/env python3
# -*- coding: utf-8 -*-


# def calc_sum(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n
#     return sum


# print(calc_sum(*[1, 2, 3, 4, 5, 6, 7, 8, 9]))


# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum


# f = lazy_sum(*[1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(f())

# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f1 == f2)

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs


# f1, f2, f3 = count()

# print(f1())
# print(f2())
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# f1, f2, f3 = count()

# print(f1())
# print(f2())
# print(f3())

# ===================================================================================
# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：


def createCounter():
    n = 0

    def counter():
        n = 1 + n
        return n
    print('n = ' + str(n))
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
