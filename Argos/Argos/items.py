import scrapy

class ArgosToysItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    productUrl = scrapy.Field()