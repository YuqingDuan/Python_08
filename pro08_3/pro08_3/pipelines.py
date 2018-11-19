# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import logging as log


class Pro083Pipeline(object):
    def __init__(self):
        # 链接数据库
        self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Devilhunter9527", db="dangdang",
                               charset="utf8", use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.conn.cursor();

    def process_item(self, item, spider):
        try:
            # 遍历每页的len(item["title"]本图书
            for i in range(0, len(item["title"])):
                title = item["title"][i]
                link = item["link"][i]
                comment = item["comment"][i]
                sql = "insert into books(title,link,comment) values('" + title + "','" + link + "','" + comment + "')"
                # 插入数据
                self.cursor.execute(sql)
                # 提交sql语句
                self.conn.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item
