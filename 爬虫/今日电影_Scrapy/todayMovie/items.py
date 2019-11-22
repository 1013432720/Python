# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TodaymovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    movieTitleCn=scrapy.Field()
    movieTitleEn=scrapy.Field()
    director=scrapy.Field()
    runtime=scrapy.Field()
