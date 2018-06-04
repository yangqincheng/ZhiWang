# -- coding: utf-8 --
import scrapy

class authorspider(scrapy.Spider):

    name = "author_content"

    start_urls =['http://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=au&skey=%E6%9D%8E%E5%B0%8F%E7%8E%B2&code=10155907']

    def parse(self, response):
        print("here!!!!!!!!!!!!!!")
        print(response.encoding)
        print(response.body)