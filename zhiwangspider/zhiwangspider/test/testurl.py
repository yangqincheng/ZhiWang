import requests

# r = requests.get('http://kns.cnki.net/kns/brief/brief.aspx')
#
# print(r.status_code)
#http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&dbPrefix=SCDB&dbCatalog=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%96%87%E7%8C%AE%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93&ConfigFile=SCDBINDEX.xml&research=off&t=1527021832141&keyValue=&S=1
# payload = {'pagename': 'ASP.brief_default_result_aspx',
#            'dbPrefix': 'SCDB',
#             'dbCatalog': '%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%96%87%E7%8C%AE%E7%BD%91%E7%BB%9C%E5%87%BA%E7%89%88%E6%80%BB%E5%BA%93',
#            'ConfigFile':'SCDBINDEX.xml',
#            'research':'off',
#            't':'1527021832141',
#            'keyValue': '',
#            'S': '1'
#            }

# payload ={ 'dbPrefix': 'SCDB'}
# 'action':'',
#         'NaviCode': 'J',
#         'ua': '1.25',
# 1527073187623
# 1527073334297
# 1527073274508
# 1527073391279
# 1527073772574
# 1527149333171
# 对比信息科技下t的变化
# 1527149333171
# 1527149641181
# 1527149671599
# 1527150465953
# 对比经济与管理科学下的t的变化
# 1527150552356
# 1527150590800
# 1527150706199
payload ={
         'PageName': 'ASP.brief_result_aspx',
         'dbPrefix': 'SCDB',
         'dbCatalog': '中国学术文献网络出版总库',
         'ConfigFile': 'SCDB.xml',
        # 'db_opt': 'CJFQ,CJRF,CDFD,CMFD,CPFD,IPFD,CCND,CCJD',
          'research':'off',
          't': '1527071672314',
          'keyValue':'',
          'S': '1'
          }

headers = { 'Host': 'kns.cnki.net',
            'Referer': 'http://kns.cnki.net/kns/brief/default_result.aspx',
            # 'Referer': 'http://kns.cnki.net/kns/brief/result.aspx?dbprefix=scdb',
            'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'cookie': 'Ecp_notFirstLogin=Ib6SJd; Ecp_ClientId=4180307153901907322; cnkiUserKey=8c8827b8-3cea-8012-adbd-889a105abb15; UM_distinctid=1632606a879266-0e05c4f101a6dd-f373567-144000-1632606a87a567; RsPerPage=50; ASP.NET_SessionId=u15p1ladju01lcqzwga4p4pq; SID_kcms=124111; Ecp_session=1; SID_klogin=125142; SID_krsnew=125131; SID_knsdelivery=125123; SID_kns=123110; _pk_ref=%5B%22%22%2C%22%22%2C1527437948%2C%22http%3A%2F%[图片]2Fwww.cnki.net%2Fold%2F%22%5D; _pk_id=81120ecb-7da4-4729-a415-42a4ccd3d1ba.1525350576.31.1527437948.1527437948.; LID=WEEvREcwSlJHSldRa1Fhb09jSnZqRXNqRmQ1czRuWFkxSTZPcy9zaE04MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22xn0116%22%2C%22ShowName%22%3A%22%25E7%2594%25B5%25E5%25AD%2590%25E7%25A7%2591%25E6%258A%2580%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22Ib6SJd%22%7D; c_m_LinID=LinID=WEEvREcwSlJHSldRa1Fhb09jSnZqRXNqRmQ1czRuWFkxSTZPcy9zaE04MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=05/28/2018 15:53:29; c_m_expire=2018-05-28 15:53:29'
            }



url ='http://kns.cnki.net/kns/brief/brief.aspx'

r = requests.get(url, headers=headers, params=payload)

print(r.text)