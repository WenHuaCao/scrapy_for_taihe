# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['music.taihe.com']
    start_urls = ['http://music.taihe.com/']

    def parse(self, response):
        pass
