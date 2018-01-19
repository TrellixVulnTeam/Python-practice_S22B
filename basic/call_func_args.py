''' the_list_tuple '''
#!/user/bin/env python3
# -*- coding: utf-8 -*-

# =========================================================================
# 默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s


# print(power(5, 2))
# print(power(15))
# print(power(15, 3))


# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('Sarah', 'F')
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin')


#  定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=[]):
#     L.append('END')
#     return L


# print(add_end())
# print(add_end())
# print(add_end())

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L


# print(add_end())
# print(add_end())
# print(add_end())

# 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum


# print(calc(1, 2, 3, 4))

# L = [1, 2, 3, 4]
# print(calc(*[1, 2, 3, 4]))
# print(calc(*L))

# print(L)
# print(*L)


# =========================================================================
# 关键字参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)


# person('Michael', 30)
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')

# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
# person('Jack', 24, **extra)

# =========================================================================
# 命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)


# person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person(name, age, *args, city='Beijing', job):
#     print(name, age, args, city, job)


# person('Jack', 24, job='Engineer')


# =========================================================================

# 参数组合 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

# >>> f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
# >>> f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
# >>> f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# >>> f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# >>> f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

# >>> args = (1, 2, 3, 4)
# >>> kw = {'d': 99, 'x': '#'}
# >>> f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
# >>> args = (1, 2, 3)
# >>> kw = {'d': 88, 'x': '#'}
# >>> f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# ===============================================================================
# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

# -*- coding: utf-8 -*-


def product(*args):
    if not args:
        raise TypeError('bad operand type')
    s = 1
    for n in args:
        s = s * n
    return s


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
