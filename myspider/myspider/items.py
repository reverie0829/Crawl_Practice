# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    
    name = scrapy.Field()  #講師名字
    title = scrapy.Field()  #講師職稱
    desc = scrapy.Field()  #講師介紹
    
