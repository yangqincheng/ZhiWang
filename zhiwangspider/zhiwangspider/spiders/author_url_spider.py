from scrapy import Spider
from zhiwangspider.items import ZhiwangspiderItem
from scrapy import Request
from scrapy.selector import Selector
from zhiwangspider.transCookies import stringToDict
import urllib.parse
import time

from urllib.parse import unquote #解码url

class AuthorUrlSpider(Spider):
    name='au'

    cnki_articles_root_url='http://kns.cnki.net/kns/brief/brief.aspx' #知网的根url

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

    cookies="Ecp_notFirstLogin=AjlAZ1; Ecp_ClientId=5180512111401484195; cnkiUserKey=fff06d5a-f3ef-b430-2c06-87f65a20145d; RsPerPage=20; UM_distinctid=1635262bfbe1e9-07df346658c1b2-3961430f-e1000-1635262bfbf69e; CNZZDATA3258975=cnzz_eid%3D2068027915-1526090497-null%26ntime%3D1527070181; _pk_ref=%5B%22%22%2C%22%22%2C1527590884%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id=e96ada05-9ddc-493b-876b-8154ca9c4789.1526095593.22.1527595071.1527590884.; ASP.NET_SessionId=vvyodmv0n0dpdf2thwk04q4g; LID=WEEvREcwSlJHSldRa1FhdXNXa0hIb2hqMDBJY2twTmFQanJDTk9qYW40MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; SID_kns=123111; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhdXNXa0hIb2hqMDBJY2twTmFQanJDTk9qYW40MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=05/30/2018 00:08:53; c_m_expire=2018-05-30 00:08:53; SID_klogin=125144; Ecp_session=1; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22xn0116%22%2C%22ShowName%22%3A%22%25E7%2594%25B5%25E5%25AD%2590%25E7%25A7%2591%25E6%258A%2580%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22AjlAZ1%22%7D"

    def start_requests(self):
        url = 'http://kns.cnki.net/kns/brief/brief.aspx?'+urllib.parse.urlencode(self.params)
        # 为了给Request添加params
        yield Request(url,encoding='utf-8',cookies=stringToDict(self.cookies),callback=self.parse)


    def parse(self, response):
        sel = Selector(response)
        time.sleep(1)
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
            yield Request(self.cnki_articles_root_url+ next_page_url,encoding='utf-8', cookies = stringToDict(self.cookies),callback=self.parse)

        except:
            print("Error: 爬取下一页面的链接发生异常:")
            print("该页面的源代码如下：")
            print(response.text)




