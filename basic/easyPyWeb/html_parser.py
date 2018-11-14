#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):

    def parser(self, url, content):
        if url is None or content is None:
            return

        soup = BeautifulSoup(content, 'lxml', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = []
        # <a target="_blank" href="/item/%E6%8E%92%E8%A1%8C%E6%A6%9C/4895" data-lemmaid="4895">排行榜</a>
        links = soup.find_all('a', href=re.compile(r'/item/\w+/\d+'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.append(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_data = {}

        res_data['url'] = url
        title_node = soup.find(
            'dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data
