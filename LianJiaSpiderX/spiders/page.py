#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import re
from scrapy import Request
from scrapy.spiders import Spider
from LianJiaSpiderX.items import LianjiaspiderxItem


class ZuFangSpider(Spider):
    allowed_domains = ["lianjia.com"]
    name = 'page'
    city = ''
    href = ''
    page = 1    # 总是从第一页开始
    total_page = 0  # 起始没有获得总页数
    start_urls = []

    def __init__(self):
        with open('area.txt', 'r') as f:
            self.start_urls = f.readlines()
            self.city = self.start_urls[0][7:9]
        with open('page.txt', 'w') as f:
            pass

    def parse(self, response):
        try:
            page_box = response.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]').extract()[0]
            matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
            self.total_page = int(matches.group(1))
            print('++++++++++++++++++++')
            print(self.total_page)
            print(page_box)
            matches = re.search('.*page-url="(.+)pg{page}/".*', str(page_box))
            self.href = matches.group(1)
            print(self.href)
            print('++++++++++++++++++++')
        except Exception as e:
            self.total_page = 1

        with open('page.txt', 'a') as f:
            for i in range(self.total_page+1)[1:]:
                url = 'http://{0}.lianjia.com{1}pg{2}'.format(self.city, self.href, i)
                f.write(url+'\n')
        return


