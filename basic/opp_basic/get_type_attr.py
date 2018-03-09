#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types

# print(type(123))
# print(type('132'))
# print(type(None))
# print(type(abs))


# def fn():
#     pass

# print(type(fn) == types.FunctionType)
# print(type(fn))
# print(type(lambda x: x) == types.FunctionType)
# print(type(lambda x: x) == types.LambdaType)
# print(type(lambda x: x) == types.LambdaType)

# class Animal(object):
#     def run(self):
#         print('Animal is running...')


# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')


# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')


# dog = Dog()

# print(isinstance(dog, (Dog, Cat)))
# print(type(dog) == Animal)

# print(dir('abc'))

# abc_str = 'abc'
# print(len(abc_str))
# print(abc_str.__len__())

# class Student(object):
#     name = 'Student'

# print(Student.name)


# s = Student()
# print(s.name)

# s.name = 'Jack'
# print(s.name)

# # del s.name
# # print(s.name)
# del Student.name

# print(s.name)
# print(Student.name)


# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

