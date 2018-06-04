# -*- coding: utf-8 -*-

# Scrapy settings for zhiwangspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from zhiwangspider.transCookies import stringToDict

BOT_NAME = 'zhiwangspider'

SPIDER_MODULES = ['zhiwangspider.spiders']
NEWSPIDER_MODULE = 'zhiwangspider.spiders'

cookies ='Ecp_notFirstLogin=y8LPES; Ecp_ClientId=5180512111401484195; cnkiUserKey=fff06d5a-f3ef-b430-2c06-87f65a20145d; RsPerPage=20; UM_distinctid=1635262bfbe1e9-07df346658c1b2-3961430f-e1000-1635262bfbf69e; CNZZDATA3258975=cnzz_eid%3D2068027915-1526090497-null%26ntime%3D1527070181; _pk_ref=%5B%22%22%2C%22%22%2C1528033371%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id=e96ada05-9ddc-493b-876b-8154ca9c4789.1526095593.29.1528035478.1528033371.; ASP.NET_SessionId=1wkyvyvvfw5ehzyh4105wmg4; LID=WEEvREcwSlJHSldRa1Fhb09jSnZqem53VkQ5b3Zoc3craXZKR3A4KzhMaz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; SID_kns=123124; Ecp_session=1; SID_klogin=125143; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22xn0116%22%2C%22ShowName%22%3A%22%25E7%2594%25B5%25E5%25AD%2590%25E7%25A7%2591%25E6%258A%2580%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22y8LPES%22%7D; c_m_LinID=LinID=WEEvREcwSlJHSldRa1Fhb09jSnZqem53VkQ5b3Zoc3craXZKR3A4KzhMaz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=06/03/2018 23:50:05; c_m_expire=2018-06-03 23:50:05'



dict_cookies = stringToDict(cookies)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhiwangspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
           'Host': 'kns.cnki.net',
           'Referer': 'http://kns.cnki.net/kns/brief/default_result.aspx',
           # 'Referer': 'http://kns.cnki.net/kns/brief/result.aspx?dbprefix=scdb',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            }

#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhiwangspider.middlewares.ZhiwangspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhiwangspider.middlewares.ZhiwangspiderDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhiwangspider.pipelines.ZhiwangspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
