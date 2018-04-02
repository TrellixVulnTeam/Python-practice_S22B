# -*- coding: utf-8 -*-

import http
import time
import urllib
from http import cookiejar
from urllib import request


def vote():
    pre_url = r'http://promo.unitechance.com/picc2018contest/detial/40?from=groupmessage&isappinstalled=0'
    url = r'http://promo.unitechance.com/api/picc2018contest/vote?id=40'

    cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)  # 通过handler来构建opener

    response = opener.open(pre_url)  # 此处的open方法同urllib2的urlopen方法，也可以传入request
    time.sleep(2)
    response = opener.open(url)
    print(response.read().decode())


def auto_vote():
    n = 1000
    while n >= 0:
        print('index = %s start ...' % n)
        vote()
        print('index = %s   end ...' % n)
        n = n - 1
        time.sleep(1)


auto_vote()
