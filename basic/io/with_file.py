# -*- coding: utf-8 -*-

path = 'C:/users/Administrator/1.txt'
# f = open('1.txt', 'r')
# try:
#     f = open('C:/Users/Administrator/1.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('C:/users/Administrator/1.txt', 'r', encoding='utf-8', errors='ignore') as f:
#     print(f.read())


# f = open(path, 'w')
# f.white('Hello world again')
# f.close

with open(path, 'a') as f:
    f.write('with ...')

#     练习
# 请将本地一个文本文件读为一个str并打印出来：

# -*- coding: utf-8 -*-

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

# 运行代码观察结果