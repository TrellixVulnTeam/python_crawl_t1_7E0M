# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#https://viblo.asia/p/crawl-du-lieu-trang-web-voi-scrapy-E375zWr1KGW

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass

    User = scrapy.Field()
    Comment = scrapy.Field()
    Time = scrapy.Field()
