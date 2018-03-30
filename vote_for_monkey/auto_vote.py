# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib


def auto_vote():

    pre_url = 'http://promo.unitechance.com/picc2018contest/detial/40?from=groupmessage&isappinstalled=0'
    url = 'http://promo.unitechance.com/api/picc2018contest/vote?id=40'

    req = urllib2.Request(pre_url)
    # 将cookie与opener绑定，原因是让两次请求用相同cookie
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # 第一次请求
    response = opener.open(req)

    # 第二次请求
    req = urllib2.Request(url)
    response = opener.open(req)
    html = response.read().decode('utf-8')
    # 输出页面
    print(html)
