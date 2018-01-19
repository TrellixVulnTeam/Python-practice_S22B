'''call func'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(abs(-1))
# print(abs(100))
# print(abs(12.34))

# print(max(1, 2, 3, 4, 5, 6))
# print(max([1, 2, 3, 4, 5]))

# print(int('123'))
# print(int(12.34))
# print(float('12.34'))
# print(str(1.23))
# print(bool(1.23))

# a = abs
# print(a(-1))

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(oct(n1))
# print(hex(n2))


# def my_abs(x_x):
#     '''func docstring'''
#     if not isinstance(x_x, (int, float)):
#         raise TypeError('bad operand type')
#     if x_x >= 0:
#         return x_x
#     else:
#         return -x_x


# print(my_abs(-1))
# print(my_abs(100))
# print(my_abs(12.34))

# help(my_abs)


# def nop():
#     ''' empty func'''
#     pass

import math


# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny


# x, y = move(1, 2, 3)
# print(x, y)
# r = move(1, 2, 3)
# print(r)

# ax*x + bx + c = 0 求解
def quadratic(a, b, c):
    if a == 0:
        return -c / b, -c / b
    else:
        return (-b + math.sqrt(b*b-4*a*c)) / (2 * a), (-b - math.sqrt(b*b-4*a*c)) / (2 * a)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')