# -*- coding: utf-8 -*-

import os

# print(os.name)

# os.uname() 方法 windows平台不提供
# print(os.uname())

# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# print(os.path.abspath('/kugou'))

# mypath = os.path.join('./kugou', 'haha')

# os.mkdir(mypath)
# os.rmdir(mypath)

# paths = os.path.split('/Users/michael/testdir/file.txt')
# print(paths)

# print(os.path.abspath('.'))
# print(os.listdir('.'))

# os.rename('1.txt', '2.txt')
# os.remove('2.txt')
# os.rmdir('2.txt')
# 
# os.remove('2.txt')

# L = [x for x in os.listdir('.') if os.path.isfile(x)]
L = [x for x in os.listdir('.')]
print(L)

# a = 'apis.py'
# print(os.path.splitext(a))
# print('apis.py''.py')

# 练习
# 1.利用os模块编写一个能实现dir -l输出的程序。
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


# 1.

# import os
# import time

# # 获取当前目录下的目录结构['aaa', 'dir.py', 'io.py']
# list = os.listdir('.')

# print('%s\t\t\t\t%s\t\t%s\t\t%s' % ('Time', 'Type', 'Size', 'Name'))
# for i in list:
#     fname = i
#     ftime = time.strftime('%Y-%m-%d %H:%M:%S',
#                           time.localtime(os.path.getmtime(fname)))
#     fsize = os.path.getsize(fname)
#     flag = '<\DIR>' if os.path.isdir(fname) else 'file'
#     print('%s\t\t%s\t\t%4s\t\t%s' % (ftime, flag, fsize, fname))


# 2.
# def searchFile(key, path=os.path.abspath('.'), ):
#     fpath = os.listdir(path)
#     for p in fpath:
#         eachPath = os.path.join(path, p)
#         if os.path.isfile(eachPath):
#             if key and key in eachPath:
#                 print(eachPath)
#         elif os.path.isdir(eachPath):
#             searchFile(key, eachPath)


# searchFile('.py')
