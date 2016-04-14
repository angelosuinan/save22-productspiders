import scrapy
import datetime
from items import expansys_item 
class DmozSpider(scrapy.Spider):
    name = "expansys"
    allowed_domains = ["expansys.com.sg"]
    start_urls = [
        'http://www.expansys.com.sg/site-map/'
    ]

    def parse(self, response):      
        for url in response.xpath('//ul[contains(@class, "col")]//@href').extract():
            yield scrapy.Request('http://www.expansys.com.sg'+url, 
                callback=self.get_page_num)
    def get_page_num(self, response,x=0):
        a=response.xpath('//li[contains(@class, "pagination")]//text()').re(r'\d+')              
        if(len(a)!=0):           
            for x in range(1,int(max(a))+1):
                #print response.url+"?page={}#listing".format(x)
                yield scrapy.Request((response.url+"?page={}#listing").format(x),
                     callback=self.get_webpage_item)
        else:
            yield scrapy.Request((response.url+"?page=1#listing"),
                     callback=self.get_webpage_item)       
    def get_webpage_item(self,response):
        for url in response.xpath('//li[contains(@class, "title")]/h3/a/@href').extract():
            yield scrapy.Request('http://www.expansys.com.sg'+url, 
                callback=self.get_data)
    def get_data(self,response):
        now = datetime.datetime.now()
        items=expansys_item()
        items["url"]=response.url
        items["title"]=response.xpath('//*[@id="title"]/h1/text()').extract()
  #      d=response.xpath('//*[@id="price"]/strong/span/sup/text()').extract()
    #    r=response.xpath('//*[@id="price"]/strong/span/text()').extract()
        items["price"]=response.xpath('//*[@id="price"]/strong//text()').extract_first()
        items["currency"]=['Singaporean Dollar']
        items["current_price"]=items["price"]
        items["primary_image_url"]=response.xpath('//*[@id="image"]/a/img/@src').extract()
        items['crawl_time']=now.strftime("%Y-%m-%d %H:%M:%S")
        items["categories"]=response.xpath('//li[contains(@class,"level")]/a/span/text()').extract()
        yield items




