# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

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
            chrome_options.add_argument('--headless') #关闭窗口
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(chrome_options=chrome_options)

            #  driver = webdriver.Firefox()
            driver.get(request.url)
            nav_keys_xpath=["//dt[@id='lcatalog_AUKEYWORDS']","//dd[@id='lcatalog_Zgby']","//dd[@id='lcatalog_Zgxz']","//dd[@id='lcatalog_1']",
                            "//dd[@id='lcatalog_Wwjd']","//dd[@id='lcatalog_4']","//dd[@id='lcatalog_3']","//dd[@id='lcatalog_2']","//dd[@id='lcatalog_Cckf']",
                            "//dt[@id='lcatalog_AuTUs']","//dt[@id='lcatalog_AuCos']","//dt[@id='lcatalog_AuFunds']","//dt[@id='lcatalog_AuSTs']"]
            # elements = []
            # a = driver.find_element_by_xpath("//dt[@id='lcatalog_AUKEYWORDS']")
            # # 找到需要点击的按钮，这个按钮是作者关注领域
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_Zgby']")
            # elements.append(a)
            # # 最高被引
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_Zgxz']")
            # elements.append(a)
            # # 最高下载
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_1']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_Wwjd']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_4']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_3']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_2']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dd[@id='lcatalog_Cckf']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dt[@id='lcatalog_AuTUs']")
            # elements.append(a)
            #
            # a = driver.find_element_by_xpath("//dt[@id='lcatalog_AuCos']")
            # elements.append(a)
            #
            # # a = driver.find_element_by_xpath("//dt[@id='lcatalog_AuFunds']")
            # # elements.append(a)
            #
            # # a = driver.find_element_by_xpath("//dt[@id='lcatalog_AuSTs']")
            # # elements.append(a)
            #
            # i = 0
            #
            # for element in elements:
            #     element.click()
            #     i =i + 1
            #     print(i)
            #     time.sleep(1)
               # driver.refresh()
               # i = i + 1
               # if i == 3:
               #     time.sleep(2)


               # print("1")
               # driver.refresh()
               #  time.sleep(2)
               #  进行点击操作

            for xpath in nav_keys_xpath:# 点击导航栏
                e=driver.find_element_by_xpath(xpath)
                e.click()
                time.sleep(1)

            print("开始定位iframe")
            # 定位每个iframe
            iframe_names=["frame1","frame2","framecatalog_1","framecatalog_Wwjd","framecatalog_4","framecatalog_3","framecatalog_2",
                          "framecatalog_Cckf","framecatalog_AuTUs","framecatalog_AuCos","framecatalog_AuFunds","framecatalog_AuSTs"]
            # //*[@id="frame1"]

            for name in iframe_names:
                try:
                    # 将滚动条移动到页面的底部
                    js = "var q=document.documentElement.scrollTop=100000"
                    driver.execute_script(js) #执行js语句
                    time.sleep(1)

                    element = WebDriverWait(driver, 10).until(
                        # EC.invisibility_of_element_located("//div[class='wait']")
                        EC.presence_of_element_located((By.XPATH, '//*[@id="%s"]'%name)) #注：iframe不加载时一开始就存在，所以这个等待无意义，但尝试等待iframe其中的标题无果
                    )
                    # driver.switch_to.frame(element)
                    # try:
                    #     h2 = WebDriverWait(driver, 20).until( #尝试等待标题加载
                    #         EC.presence_of_element_located((By.XPATH, '//*[@id="%s"]//h2' % name))
                    #     )
                    # except:
                    #     h3 = WebDriverWait(driver, 20).until(
                    #         EC.presence_of_element_located((By.XPATH, '//*[@id="%s"]//h3' % name))
                    #     )

                    # driver.switch_to.default_content()
                    # print(element,"__________")
                finally:
                    # WebDriverWait(driver, 10).until(
                    #     EC.invisibility_of_element_located("//div[class='wait']")# 尝试等待“正在加载”消失
                    #     # EC.presence_of_element_located((By.XPATH, '//*[@id="%s"]' % name))
                    # )
                # element=driver.find_element_by_xpath('//*[@id="%s"]'%name)
                    driver.switch_to.frame(element) # 切换到iframe里面
                    driver.switch_to.default_content() # 回到主页面，这里如果不切换则不能访问其他iframe


            # iframes = []
            # iframes.append(driver.find_element_by_name("frame1"))
            # # 得到异步加载的iframe，然后执行第一个iframe
            # iframes.append(driver.find_element_by_name("framecatalog_Wwjd"))
            # iframes.append(driver.find_element_by_name("framecatalog_1"))
            # iframes.append(driver.find_element_by_name("frame2"))
            # iframes.append(driver.find_element_by_name("framecatalog_4"))
            # iframes.append(driver.find_element_by_name("framecatalog_3"))
            # iframes.append(driver.find_element_by_name("framecatalog_2"))
            # iframes.append(driver.find_element_by_name("framecatalog_Cckf"))
            # iframes.append(driver.find_element_by_name("framecatalog_AuTUs"))
            # iframes.append(driver.find_element_by_name("framecatalog_AuCos"))
            # # iframes.append(driver.find_element_by_name("framecatalog_AuFunds"))
            # # iframes.append(driver.find_element_by_name("framecatalog_AuSTs"))
            #
            # # for iframe in iframes:
            # #     driver.switch_to.frame(iframe)
            # driver.switch_to.frame(iframes[7])
            # driver.switch_to.frame(iframes[8])
            # driver.switch_to.frame(iframe[2])

            # try:
            #     element = WebDriverWait(driver, 20).until(
            #         EC.presence_of_element_located((By.XPATH, '//*[@id="lcatalog_AuSTs"]'))
            #     )
            # finally:
            #     driver.quit()

            time.sleep(2)
            body = driver.page_source
            print("访问" + request.url)
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
