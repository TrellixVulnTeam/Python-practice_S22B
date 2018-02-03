#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{}: {}'.format(self.name, self.score))


s = Student('L', 11)

print(s)
print(Student)
s.print_score()
