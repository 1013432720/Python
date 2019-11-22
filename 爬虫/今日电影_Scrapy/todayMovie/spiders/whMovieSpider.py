# -*- coding: utf-8 -*-
import scrapy
import re
from todayMovie.items import TodaymovieItem

class WhmoviespiderSpider(scrapy.Spider):
    name = 'whMovieSpider'
    allowed_domains = ['mtime.com']
    start_urls = ['http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/']

    def parse(self, response):
        #pass
        selector=response.xpath('/html/body/script[3]/text()')[0].extract()
        movieStr=re.search('"movies":\[.*?\]',selector).group()
        movieList=re.findall('{.*?}',movieStr)
        items=[]
        for movie in movieList:
            mDic=eval(movie)
            item=TodaymovieItem()
            item['movieTitleCn']=mDic.get('movieTitleCn')
            item['movieTitleEn']=mDic.get('movieTitleEn')
            item['director']=mDic.get('director')
            item['runtime']=mDic.get('runtime')
            items.append(item)
        return items
