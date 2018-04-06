# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderxItem(scrapy.Item):
    # define the fields for your item here like:
    xiaoqu = scrapy.Field()
    layout = scrapy.Field()
    size = scrapy.Field()
    orientation = scrapy.Field()
    price = scrapy.Field()
