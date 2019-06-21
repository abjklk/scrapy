# -*- coding: utf-8 -*-
import scrapy

from ..items import TutItem


class TutspiderSpider(scrapy.Spider):
    name = 'tutspider'
    allowed_domains = ['kletecheresults.contineo.in/']
    start_urls = ['http://kletecheresults.contineo.in/index.php/component/report/?task=getReport&id=procard&usn=01FE17BME069']

    def parse(self, response):
        item = TutItem()
        fil_urls = []
        uri = 'http://kletecheresults.contineo.in/index.php/component/report/?task=getReport&id=procard&usn=01FE17BME000'
        x = 74
        while(x > 0):
            num = uri[-2:]
            num = int(num)
            if(num < 9):
                num += 1
                num = str(num)
                uri = uri[:104]
                uri = uri + num
                fil_urls.append(uri)
            elif(num < 99):
                num += 1
                num = str(num)
                uri = uri[:103]
                uri = uri + num
                fil_urls.append(uri)
            else:
                num += 1
                num = str(num)
                uri = uri[:102]
                uri = uri + num
                fil_urls.append(uri)
            x -= 1
        item["file_urls"] = fil_urls
        return item
