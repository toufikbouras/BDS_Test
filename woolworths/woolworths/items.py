# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WoolworthsItem(scrapy.Item):
    # define the fields for your item here like:
    Home = scrapy.Field()
    Drinks = scrapy.Field()
    CJIT = scrapy.Field()
    IcedTeas = scrapy.Field()


