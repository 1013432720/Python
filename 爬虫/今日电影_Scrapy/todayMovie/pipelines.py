# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import codecs
class TodaymoviePipeline(object):
    def process_item(self, item, spider):
        #return item
        today=time.strftime('%Y-%m-%d',time.localtime())
        fileName='武汉汉街万达广场'+today+'.txt'
        with codecs.open(fileName,'a+','utf-8')as fp:
            fp.write('%s %s %s %s \t \n'%(item['movieTitleCn'],item['movieTitleEn'],item['director'],item['runtime']))
