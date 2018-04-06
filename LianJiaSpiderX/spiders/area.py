#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import re
from scrapy import Request
from scrapy.spiders import Spider
from LianJiaSpiderX.libs.city import *


class AreaSpider(Spider):
    allowed_domains = ["lianjia.com"]
    name = 'area'
    start_urls = []
    city = ''

    def __init__(self):
        with open('district.txt', 'r') as f:
            self.start_urls = f.readlines()
            self.city = self.start_urls[0][7:9]
        with open('area.txt', 'w') as f:
            pass

    def parse(self, response):
        areas = response.xpath('//*[@id="filter-options"]/dl[1]/dd/div[2]/a/@href').extract()
        for area in areas[1:]:  # 跳过"不限"
            url = 'http://{0}.lianjia.com{1}'.format(self.city, area)
            with open('area.txt', 'a') as f:
                f.write(url+'\n')
            yield



