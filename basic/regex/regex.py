#!/user/bin/env python3
# -*- coding: utf-8 -*-


# import re

# re_telphone = re.compile(r'^(\d{3})-(\d{3,8})$')

# result = re_telphone.match('010-123456').groups()

# print(result)


# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

# someone@gmail.com
# bill.gates@microsoft.com

# -*- coding: utf-8 -*-
# import re


# def is_valid_email(addr):
#     re_mail = re.compile(r'[\w\.]+@\w+.com')
#     return re_mail.match(addr)


# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')


# 版本二可以提取出带名字的Email地址：

# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
# -*- coding: utf-8 -*-
import re


def name_of_email(addr):
    re_mail = re.compile(r'(<(\w+\s+\w+)>)?\s*([\w\.]+)@\w+.\w+')
    first = re_mail.match(addr).group(2)
    two = re_mail.match(addr).group(3)
    if first:
        print('first test name: ' + first)
        return first
    else:
        print('two test name: ' + two)
        return two


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
