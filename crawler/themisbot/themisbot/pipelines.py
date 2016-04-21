# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from porc import Client

host = "https://api.aws-eu-west-1.orchestrate.io/"
client = Client("5d754f98-857a-4aed-8dc6-0e397c8d1816", host)

class ThemisbotPipeline(object):
    def process_item(self, item, spider):
        return item

class CleanUpPipeline(object):
    def process_item(self, item, spider):

        item['content'].remove('Advertisement')

        return item

class OrchestratePipeline(object):
    def process_item(self, item, spider):

        response = client.post('crawled_pages', {
            'title':    item['title'],
            'content':  item['content'],
            'author':   item['author'],
            'date':     item['date']
        })

        print response.raise_for_status()

        return item
