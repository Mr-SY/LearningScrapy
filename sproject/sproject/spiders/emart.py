import scrapy

class QuotesSpider(scrapy.Spider):
    name = "emart"

    def start_requests(self):
        start_url = ["http://emart.ssg.com/best/main.ssg?Egnb=best"]

    def parse(self, response):
        for sel in response.xpath('//*[@id="best5"]/li'):
            yeild {
            'title' : sel.xpath('/div/a/text()').extract(),
            #'link' : sel.xpath('/div/a/@href').extract(),
            #'number' : sel.xpath('/strong/text()').extract(),
            }
            
            
