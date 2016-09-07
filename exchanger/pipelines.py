# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import os


class ExchangerPipeline(object):

    def __init__(self):
        if not os.path.isfile('scrapped_data.db'):
            self.conn = sqlite3.connect('scrapped_data.db')
            c = self.conn.cursor()
            c.execute('''CREATE TABLE exchange
                 (year text,
                 month text,
                 day text,
                 usd_buy text,
                 usd_sell text,
                 eur_buy text,
                 eur_sell text)''')
        else:
            self.conn = sqlite3.connect('scrapped_data.db')

    def process_item(self, item, spider):
        c = self.conn.cursor()
        year = str(item["year"])
        print "year: ", year
        month = str(item["month"])
        print "month: ", month
        day = str(item["day"])
        print "day: ", day
        usd_buy = str(item["usd_buy"][0])
        print "usd_buy: ", usd_buy
        usd_sell = str(item["usd_sell"][0])
        print "usd_sel: ", usd_sell
        eur_buy = str(item["eur_buy"][0])
        print "eur_by: ", eur_buy
        eur_sell = str(item["eur_sell"][0])
        print "eur_sell: ", eur_sell

        c.execute('''INSERT INTO exchange VALUES
            ("%s", "%s", "%s", "%s", "%s", "%s", "%s")
            ''' % (year, month, day, usd_buy, usd_sell, eur_buy, eur_sell))
        self.conn.commit()
        self.conn.close()
