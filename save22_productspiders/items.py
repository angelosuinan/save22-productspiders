# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class expansys_item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    crawl_time = scrapy.Field()
    current_price = scrapy.Field()
    primary_image_url = scrapy. Field()
    categories = scrapy.Field()

    instock = scrapy.Field
    
