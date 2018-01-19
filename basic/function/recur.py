#!/user/bin/env python3
# -*- coding: utf-8 -*-


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)


# print(fact(1))
# print(fact(5))
# print(fact(100))

# ============================================================================
# 尾递归

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了
# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，
# num - 1和num * product在函数调用前就会被计算，不影响函数调用。
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# def fact(n):
#     return fact_iter(n, 1)


# def fact_iter(sum, product):
#     if sum == 1:
#         return product
#     else:
#         return fact_iter(sum - 1, sum * product)


# ============================================================================
# 练习
# 汉诺塔的移动可以用递归函数非常简单地实现。

# 请编写move(n, a, b, c)函数，
# 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
