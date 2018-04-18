#!/user/bin/env python3
# -*- coding: utf-8 -*-

# namedtuple
# 一个点的二维坐标就可以表示成：

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)

# print(p.x)
# print(p.y)
# print(isinstance(p, Point))
# print(isinstance(p, tuple))
# # namedtuple('名称', [属性list]):
# Circle = namedtuple('Circle', ['x', 'y', 'r'])

# =================================================================

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

# =================================================================

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1']  # key1存在
# 'abc'
dd['key2']  # key2不存在，返回默认值
# 'N/A'
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。


# =================================================================


# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：

# from collections import Counter

# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1


# print(c)
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。

# 补充几个地方：

# 1. Counter 类可以直接调用其构造方法，传入要统计的字符串：

# >>> Counter('programming')
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

# >>> dict(Counter('programming'))
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
