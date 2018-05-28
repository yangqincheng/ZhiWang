import requests

payload = {
    'code': '10155907',
    'infotype': '1'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'zh-CN,zh;q=0.9',
     'Connection': 'keep-alive',
    'Cookie': 'Ecp_notFirstLogin=Ib6SJd; Ecp_ClientId=4180307153901907322; cnkiUserKey=8c8827b8-3cea-8012-adbd-889a105abb15; UM_distinctid=1632606a879266-0e05c4f101a6dd-f373567-144000-1632606a87a567; RsPerPage=50; ASP.NET_SessionId=u15p1ladju01lcqzwga4p4pq; SID_kcms=124111; Ecp_session=1; SID_klogin=125142; SID_krsnew=125131; SID_knsdelivery=125123; SID_kns=123110; _pk_ref=%5B%22%22%2C%22%22%2C1527437948%2C%22http%3A%2F%2Fwww.cnki.net%2Fold%2F%22%5D; _pk_id=81120ecb-7da4-4729-a415-42a4ccd3d1ba.1525350576.31.1527437948.1527437948.; LID=WEEvREcwSlJHSldRa1Fhb09jSnZqRXNqRmQ1czRuWFkxSTZPcy9zaE04MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22xn0116%22%2C%22ShowName%22%3A%22%25E7%2594%25B5%25E5%25AD%2590%25E7%25A7%2591%25E6%258A%2580%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22Ib6SJd%22%7D; c_m_LinID=LinID=WEEvREcwSlJHSldRa1Fhb09jSnZqRXNqRmQ1czRuWFkxSTZPcy9zaE04MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=05/28/2018 16:02:17; c_m_expire=2018-05-28 16:02:17',
    'Host': 'kns.cnki.net',
    'Referer': 'http://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=au&skey=%E6%9D%8E%E5%B0%8F%E7%8E%B2&code=10155907',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

url = 'http://kns.cnki.net/kcms/detail/frame/knetlist.aspx'

r = requests.get(url,headers=headers,params=payload)

print(r.text)