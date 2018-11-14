#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from urllib import request
import http.cookiejar

url = "http://www.baidu.com"

print("第一种方式")
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第一种方式")
request2 = request.Request(url)
request2.add_header("user-agent", "Mozilla/5.0")
response2 = request.urlopen(request2)
print(response2.getcode())
print(len(response2.read()))

print("第三种方式")
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(len(response3.read()))
