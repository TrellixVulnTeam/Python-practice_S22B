#!/user/bin/env python3
# -*- coding: utf-8 -*-

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
# print(L[:3])
# print(L[1:3])
# print(L[-1])
# print(L[-2:])
# print(L[:-2])

# L = list(range(100))
# print(L[:10])
# print(L[-10:])
# print(L[10:20])
# print(L[:10:2])

# print(L[::5])
# print(L[:])

# print((0, 1, 2, 3, 4, 5)[:3])
# print('ABCDEFG'[:3])
# print('ABCDEFG'[::2])

# ==================================================================================
# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    if s.isspace() or not s:
        return ''
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
