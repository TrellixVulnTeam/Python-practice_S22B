#!/user/bin/env python3
# -*- coding: utf-8 -*-

# import base64

# print(base64.b64encode(b'111'))
# print(base64.urlsafe_b64encode(b'111'))

# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64decode(b'abcd--__'))

# ========================================================================================

# 小结
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

# 练习
# 请写一个能处理去掉=的base64解码函数：

# -*- coding: utf-8 -*-
import base64


def safe_base64_decode(s):
    n = 4 - len(s) % 4
    for i in range(n):
        s = s + b'='
    return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
