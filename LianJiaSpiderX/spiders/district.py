#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import re
from scrapy import Request
from scrapy.spiders import Spider
from LianJiaSpiderX.libs.city import *


class DistrictSpider(Spider):
    allowed_domains = ["lianjia.com"]
    name = 'district'
    start_urls = []
    city = ''

    def __init__(self):
        prompt = create_prompt_text()
        self.city = input(prompt)

        self.start_urls = [
            'http://{0}.lianjia.com/zufang'.format(self.city)
        ]
        with open('district.txt', 'w') as f:
            pass

    def parse(self, response):
        districts = response.xpath('//*[@id="filter-options"]/dl[1]/dd/div[1]/a/@href').extract()
        for district in districts[1:]:  # 跳过"不限"
            url = 'http://{0}.lianjia.com{1}'.format(self.city, district)
            with open('district.txt', 'a') as f:
                f.write(url+'\n')
            yield



