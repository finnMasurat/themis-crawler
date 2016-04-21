import scrapy
from themisbot.items import NyTimesItem

class NyTimesSpider(scrapy.Spider):
    name = "nytimesworld"
    allowed_domains = "nytimes.com"

    start_urls = [
        "http://www.nytimes.com/"
    ]

    def parse(self, response):
        item = NyTimesItem()
        item['title'] = response.xpath('//title/text()').extract()[0]
        item['content'] = response.css('div.story-body').xpath('//p/text()').extract()
        item['author'] = "get_author"
        item['date'] = "get_date"
        print item
