#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self._score = score

#     def print_name(self):
#         print('name = %s' % self.__name)

#     def print_score(self):
#         print('score = %s' % self._score)


# bart = Student('Bart Simpson', 59)
# bart.print_name()
# bart.print_score()
# print(bart._score)
# print(bart.__name)

# 需要注意的是，
# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。


# =====================================================================================================
# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender



# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
