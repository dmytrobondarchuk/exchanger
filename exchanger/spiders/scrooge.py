# -*- coding: utf-8 -*-
import scrapy
from exchanger.items import ExchangerItem
import datetime
import hidden_information


class ScroogeSpider(scrapy.Spider):
    name = "scrooge"
    allowed_domains = hidden_information.allowed_domains
    start_urls = hidden_information.start_urls

    def parse(self, response):
        item = ExchangerItem()

        usd = response.xpath("//*[@class='line usd white']")
        eur = response.xpath("//*[@class='line euro']")

        date = datetime.date.today()

        item["year"] = str(date.year)
        item["month"] = str(date.month)
        item["day"] = str(date.day)

        item["usd_buy"] = usd.xpath(
            ".//span[@class='sell']/text()").extract()

        item["usd_sell"] = usd.xpath(
            ".//span[@class='sell']/text()").extract()

        item["eur_buy"] = eur.xpath(
            ".//span[@class='sell']/text()").extract()

        item["eur_sell"] = eur.xpath(
            ".//span[@class='sell']/text()").extract()

        return item
