#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from scrapy.spiders import Spider
from LianJiaSpiderX.items import LianjiaspiderxItem


class ZuFangSpider(Spider):
    name = 'zufang'
    start_urls = ['http://sh.lianjia.com/zufang/beicai/']

    def parse(self, response):
        item = LianjiaspiderxItem()

        houses = response.xpath('//*[@id="house-lst"]/li/div[2]')
        for house in houses:
            item['xiaoqu'] = house.xpath('./div[1]/div[1]/a/span/text()').extract()[0].strip()
            item['layout'] = house.xpath('./div[1]/div[1]/span[1]/span/text()').extract()[0].strip()
            item['size'] = house.xpath('./div[1]/div[1]/span[2]/text()').extract()[0].strip()
            item['orientation'] = house.xpath('./div[1]/div[1]/span[3]/text()').extract()[0].strip()
            item['price'] = house.xpath('./div[2]/div[1]/span/text()').extract()[0].strip()
            yield item

