import scrapy
from scrapy.spiders import CrawlSpider, Rule
from themisbot.items import NyTimesItem
from scrapy.linkextractors import LinkExtractor

class NyTimesSpider(CrawlSpider):
    name = 'nytimes'
    allowed_domains = ['nytimes.com']

    start_urls = ['http://www.nytimes.com/']

    rules = (
        Rule(
            LinkExtractor(
                allow=r'http://www\.nytimes\.com/[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]/[a-zA-Z]+/.*'),
                callback='parse_item',
                follow=True
            ),
    )

    def parse_item(self, response):
        item = NyTimesItem()
        item['title'] = response.xpath('//title/text()').extract()[0]
        item['content'] = response.css('div.story-body').xpath('//p/text()').extract()
        item['author'] = response.css("#story-meta-footer span.byline-author::attr('data-byline-name')").extract()
        item['date'] = response.css("#story-meta-footer time.dateline::attr('datetime')").extract()
        print response.url
