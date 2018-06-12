# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 字符串效率更高，不读文件。写到内存里，用完以后释放内存，用集合作为内存

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ZhiwangspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhiwangspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        if spider.name == "author_content":
            print( "chrome driver is starting...")
            chrome_options = Options()
            # chrome_options.add_argument('--headless') #关闭窗口
            # chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(chrome_options=chrome_options)

            #  driver = webdriver.Firefox()
            driver.get(request.url)
            nav_keys_xpath=["//dt[@id='lcatalog_AUKEYWORDS']","//dd[@id='lcatalog_Zgby']","//dd[@id='lcatalog_Zgxz']","//dd[@id='lcatalog_1']",
                            "//dd[@id='lcatalog_Wwjd']","//dd[@id='lcatalog_4']","//dd[@id='lcatalog_3']","//dd[@id='lcatalog_2']","//dd[@id='lcatalog_Cckf']",
                            "//dt[@id='lcatalog_AuTUs']","//dt[@id='lcatalog_AuCos']","//dt[@id='lcatalog_AuFunds']","//dt[@id='lcatalog_AuSTs']"]
            for xpath in nav_keys_xpath:# 点击导航栏
                e=driver.find_element_by_xpath(xpath)
                e.click()
                time.sleep(1)

            print("开始定位iframe")
            # 定位每个iframe
            iframe_ids=["frame1","frame2","framecatalog_1","framecatalog_Wwjd","framecatalog_4","framecatalog_3","framecatalog_2",
                          "framecatalog_Cckf","framecatalog_AuTUs","framecatalog_AuCos","framecatalog_AuFunds","framecatalog_AuSTs"]
            iframe_source_contents=""

            for id in iframe_ids:
                # 将滚动条移动到页面的底部
                js = "var q=document.documentElement.scrollTop=100000"
                driver.execute_script(js) #执行js语句
                time.sleep(1)

                element=driver.find_element_by_xpath('//*[@id="%s"]' % id)
                driver.switch_to.frame(element) # 切换到iframe里面
                source_code = driver.find_element_by_xpath('//*').get_attribute("outerHTML") #获得iframe则所有html内容
                iframe_source_contents="%s%s"%(iframe_source_contents,source_code) #添加所有iframe的内容至局部变量，这个函数执行完毕将被自动清除

                # 写文件方式，效率低，直接改用字符串
                # f = open('html_iframes.html', 'a',encoding='utf-8')
                # f.write(source_code)
                # f.close()

                driver.switch_to.default_content() # 回到主页面，这里如果不切换则不能访问其他iframe

            body = driver.page_source + iframe_source_contents # 将iframe内容串到html源码后面
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

        else:
            return


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
