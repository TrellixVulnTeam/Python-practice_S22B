# -*- coding: utf-8 -*-


# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'Student object (name: %s)' % self.name

#     __repr__ = __str__


# s = Student('Halh')

# print(s)


# class TestIndex(object):

#     L  = list(range(10))

#     def __getitem__(self, n):

#         if isinstance(n, int):
#             return self.L[n]
#         elif isinstance(n, slice):
#             start = n.start
#             end = n.stop
#             print('start: %s' % start)
#             print('  end: %s' % end)
#             return  self.L[start:end]

# t = TestIndex()

# print(t[5])
# print(t[7])
# print(t[5:7])


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, arg):
        return Chain('%s/:%s' % (self._path, arg))

    __repr__ = __str__


# /users/:user/repos
c = Chain().users('michael').repos
print(c)


# class Student(object):

#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print('My name is %s.' % self.name)

# s = Student('Micheal')
# s()
