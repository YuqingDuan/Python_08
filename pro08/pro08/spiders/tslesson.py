# -*- coding: utf-8 -*-
import scrapy
from pro08.items import Pro08Item
from scrapy.http import Request


class TslessonSpider(scrapy.Spider):
    name = 'tslesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        item = Pro08Item()
        item["title"] = response.xpath("//ol[@class='breadcrumb']/li[@class='active']/text()").extract()
        item["link"] = response.xpath("//ul[@class='nav nav-tabs']/li[@class='active']/a/@href").extract()
        item["stu"] = response.xpath("//span[@class='course-view']/text()").extract()
        yield item
        for i in range(1, 302):
            url = "https://edu.hellobi.com/course/" + str(i)
            yield Request(url, callback=self.parse)



