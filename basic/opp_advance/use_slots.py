#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.score = 99 # 绑定属性'score'


class GraduateStudent(Student):
    __slots__ = ('score')


g = GraduateStudent()
g.name = 9999


print(g.name)

print(hasattr(g, 'name'))
print(hasattr(g, 'age'))
print(hasattr(g, 'score'))

setattr(g, 'age', 19) 
print(g.age)
# setattr(g, 'age1', 19) 
# print(g.age1)
