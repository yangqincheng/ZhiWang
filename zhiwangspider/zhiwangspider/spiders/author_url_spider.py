from scrapy import Spider
from zhiwangspider.items import ZhiwangspiderItem
from scrapy import Request
from scrapy.selector import Selector
import urllib.parse
import time
from zhiwangspider.chrome_simulate import return_link,click_fifty
from zhiwangspider.settings import dict_cookies
from urllib.parse import unquote #解码url

class AuthorUrlSpider(Spider):
    name='au'

    cnki_articles_root_url='http://kns.cnki.net/kns/brief/brief.aspx' #知网的根url
    # cnki_articles_root_url='http://cnki.cn-ki.net/kns/brief/result.aspx' #知网的镜像url


    params =  {
    'PageName': 'ASP.brief_result_aspx',
    'dbPrefix': 'SCDB',
    'dbCatalog': '中国学术文献网络出版总库',
    'ConfigFile': 'SCDB.xml',
    'research': 'off',
    't': '1527494012546',
    'keyValue': '',
    'S': '1'
    }

    def start_requests(self):
        url = self.cnki_articles_root_url+'?'+urllib.parse.urlencode(self.params)

        # 点击50按钮，使每页的文章数增加
        # url50 = click_fifty(url)

        # 为了给Request添加params
        yield Request(url,encoding='utf-8',cookies=dict_cookies,callback=self.parse)


    def parse(self, response):
        if 'vericode.aspx'in response.url: #如果当前页面需要验证码
            url = return_link(response.url) #调用验证码模块，返回正确的链接
            print(url,' !!!!!!!!!!!!!')
            yield Request(url, encoding='utf-8', cookies=dict_cookies, callback=self.parse,dont_filter=True)
            # 这里需要设置不查重url，因为虽然之前curpage=17已经parse过，但没有保存信息
            return -1# 此时应当直接退出parse函数
        sel = Selector(response)

        # time.sleep(1)
        author_names = sel.xpath("//td[@class='author_flag']/a/text()").extract()  # 注意：选取xpath时应该跳过tbody，否则会出错
        author_urls = sel.xpath("//td[@class='author_flag']/a/@href").extract()
        print("______", author_urls, "______")
        if len(author_urls) != len(author_names):
            print('Error: len(author_urls)!=len(author_names)')
        count = 0
        while count < len(author_names):
            item = ZhiwangspiderItem()
            item['author_url'] = author_urls[count]
            item['author_name'] = author_names[count]
            yield item
            count += 1

        try:
            next_page_url=unquote(sel.xpath("(//div[@class='TitleLeftCell']/a)[last()]/@href").extract()[0]) #取页面选取栏中最后一项“下一页”
            print("***",next_page_url)
            # 需注意对url解码，避免=变成乱码影响爬取
            time.sleep(0.7)
            yield Request(self.cnki_articles_root_url+ next_page_url,encoding='utf-8', cookies = dict_cookies,callback=self.parse)

        except:
            print("Error: 爬取下一页面的链接发生异常:")
            print("该页面的源代码如下：")
            print("***",response.text,"***")




