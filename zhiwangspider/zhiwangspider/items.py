# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiwangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_url=scrapy.Field()
    author_name=scrapy.Field()
    article_name=scrapy.Field()
    pass
