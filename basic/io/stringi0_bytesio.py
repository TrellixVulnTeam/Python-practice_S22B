# -*- coding: utf-8 -*-

# from io import StringIO

# f = StringIO()

# print(f.write('Hello'))
# print(f.write(' '))
# print(f.write('VlzZ'))

# print(f.getvalue())


# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

from io import BytesIO

# f = BytesIO()
# print(f.write('中文'.encode('utf-8')))

# print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())