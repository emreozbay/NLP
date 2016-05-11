# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json, os
from scrapy.http import Request
from scrapy.exporters import JsonItemExporter, ScrapyJSONEncoder
from scrapy import signals
from scrapy.exporters import XmlItemExporter


# Pipeline for movies' data
class MoviesPipeline(object):

    def process_item(self, item, spider):
        return item