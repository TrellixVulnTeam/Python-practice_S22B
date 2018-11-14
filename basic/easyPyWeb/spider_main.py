#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crew(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url() and count <= 1000:
            try:
                new_url = self.urls.get_new_url()
                print('crew %d : %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
            except Exception as e:
                print('crew failed')
                print(e)
        self.outputer.outputer_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.crew(root_url)
