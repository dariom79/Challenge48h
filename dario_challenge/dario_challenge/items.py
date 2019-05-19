# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DarioChallengeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class TreeItem(scrapy.Item):
    parent = scrapy.Field()
    element = scrapy.Field()