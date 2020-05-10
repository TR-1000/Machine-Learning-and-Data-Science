# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2 as pg2



class WikispiderPipeline(object):

    #THIS CODE IS FOR GETTING DB SETTINGS from settings.py
    def __init__(self,db,user):
        self.db = db
        self.user = user

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")
        db = db_settings['DATABASE']
        user = db_settings['USER']
        return cls(db,user)

        print(db_settings)

    def open_spider(self, spider):
        self.conn = pg2.connect(database=self.db, user=self.user)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO test (url, title) VALUES (%s, %s)"
        self.cur.execute(sql,(
                            item["url"][0],
                            item["title"][0],
                        )
                    )
        self.conn.commit()
        print(f'inserted {item["url"]}, {item["title"]} into database')
        


    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
