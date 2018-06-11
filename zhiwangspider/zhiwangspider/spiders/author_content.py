# -- coding: utf-8 --
import scrapy
import win_unicode_console
win_unicode_console.enable()
# windows 下解决OSError: raw write() returned invalid length 14 (should have been between 0 and 7)
class authorspider(scrapy.Spider):

    name = "author_content"

    start_urls =['http://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=au&skey=%E6%9D%8E%E5%B0%8F%E7%8E%B2&code=10155907']

    def parse(self, response):
        print("here!!!!!!!!!!!!!!")
        print(response.encoding)
        body_data = response.body.decode('utf-8', 'ignore').replace(u'\xa0', u'')
        # 用utf-8解码就能保证输出的中文不乱码了，不能解码的字符忽略掉
        with open('author_body.html','w',encoding='utf-8') as f:
            f.write(body_data)
        print(body_data)
