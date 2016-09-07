# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExchangerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()

    usd_buy = scrapy.Field()
    usd_sell = scrapy.Field()
    eur_buy = scrapy.Field()
    eur_sell = scrapy.Field()
