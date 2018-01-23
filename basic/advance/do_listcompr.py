#!/user/bin/env python3
# -*- coding: utf-8 -*-

# print(list(range(10)))
# print(list(range(1, 11)))

# L = []
# for i in range(1, 11):
#     L.append(i * i)

# print(L)


# L = [x * x for x in range(1, 11) if x % 2 == 0]
# print(L)

# L = [m + n for m in 'ABC' for n in 'XYZ']
# print(L)

# import os
# L = [d for d in os.listdir()]
# print(L)

# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# L = [k + '=' + v for k, v in d.items()]
# print(L)

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])


# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
