# -*- coding: utf-8 -*-

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        return bar('a')
    except Exception as identifier:
        logging.exception(identifier)


print(main())
print('END')