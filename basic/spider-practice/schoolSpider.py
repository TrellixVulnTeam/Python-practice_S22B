#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import bs4


def get_one_page(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print('产生异常')
        return ''


def parse_one_page(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string,
                          tds[2].string, tds[3].string])


def print_one_page(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "学校地址", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = get_one_page(url)
    parse_one_page(uinfo, html)
    print_one_page(uinfo, 30)


if __name__ == "__main__":
    main()
