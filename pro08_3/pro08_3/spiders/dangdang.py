# -*- coding: utf-8 -*-
import scrapy
from pro08_3.items import Pro083Item
from scrapy.http import Request


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # 第1页的数据丢失
    start_urls = ['http://www.dangdang.com/']

    def parse(self, response):
        item = Pro083Item()
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comment"] = response.xpath("//a[@class='search_comment_num']/text()").extract()
        yield item
        # 从第0页到第20页用for循环去爬
        for i in range(0, 21):
            # 构造url
            url = "http://category.dangdang.com/pg" + str(i) + "-cp01.54.06.00.00.00.html"
            yield Request(url, callback=self.parse)

