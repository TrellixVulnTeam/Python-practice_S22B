#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' make a m3u play list '

__author__ = 'huizhe.ju'

import os


def make_m3u():
    L = [x for x in os.listdir('.') if (os.path.isfile(x) and (x != "m3u.py"))]
    with open('./诺.m3u', 'w', encoding='utf8') as f:
        f.write('#EXTM3U\n')
        for x in L:
            f.write('#EXTINF:,\n诺/')
            f.write(x)



if __name__ == '__main__':
    make_m3u()

