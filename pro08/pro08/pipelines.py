# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Pro08Pipeline(object):
    # 触发pipelines.py首先执行__init__方法
    def __init__(self):
        # 读模式('r')、写模式('w')或追加模式('a')
        self.fh = open("A:/result/42/ts.txt", "a")

    def process_item(self, item, spider):
        self.fh.write(item["title"][0] + "\n" + item["link"][0] + "\n" + item["stu"][0] + "\n" + "-------" + "\n")
        return item

    # 触发pipelines.py最后执行close_spider方法
    def close_spider(self):
        self.fh.closed()
