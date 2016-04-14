import scrapy 
import items
from scrapy.loader import ItemLoader
from items import expansys_item

class Allforyou(scrapy.Spider):
	name="allforyou"
	allowed_domains=['http//www.allforyou.sg']
	start_urls=['https://allforyou.sg'
	]

	def parse(self,response):
		for href in response.xpath('//div[contains(@class, "treemenu")]//@href').extract():
			scrapy.Request('http://www.allforyou.sg'+href, callback=self.get_item)
			print 'http://www.allforyou.sg'+str(href)
	def get_item(self,response):

		loader = ItemLoader(item=expansys_item(), response=response)
		loader.add_xpath('url', str('http//www.allforyou.sg'+response.url))
		    	
   		loader.add_xpath('title', '//span[contains(@itemprop, "name")]/text()')
   		return loader.load_items()
    			