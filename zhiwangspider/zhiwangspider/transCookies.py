# -*- coding: utf-8 -*-


def stringToDict(cookie):
    '''
    将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
    :return:
    '''
    itemDict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
    return itemDict

if __name__ == "__main__":
    cookie = "Ecp_notFirstLogin=Y3E2UL; Ecp_ClientId=5180512111401484195; cnkiUserKey=fff06d5a-f3ef-b430-2c06-87f65a20145d; RsPerPage=20; UM_distinctid=1635262bfbe1e9-07df346658c1b2-3961430f-e1000-1635262bfbf69e; CNZZDATA3258975=cnzz_eid%3D2068027915-1526090497-null%26ntime%3D1527070181; ASP.NET_SessionId=1c5bttzhp2asndykw211libv; SID_kns=123112; Ecp_session=1; SID_klogin=125141; SID_krsnew=125133; LID=WEEvREcwSlJHSldRa1FhcTdWajFtaXRldVdhWVAvOUZYcVdPYklIdm95OD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; _pk_ref=%5B%22%22%2C%22%22%2C1527508660%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses=*; Ecp_LoginStuts=%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22xn0116%22%2C%22ShowName%22%3A%22%25E7%2594%25B5%25E5%25AD%2590%25E7%25A7%2591%25E6%258A%2580%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22Y3E2UL%22%7D; _pk_id=e96ada05-9ddc-493b-876b-8154ca9c4789.1526095593.20.1527508885.1527508660.; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhcTdWajFtaXRldVdhWVAvOUZYcVdPYklIdm95OD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=05/28/2018 20:21:25; c_m_expire=2018-05-28 20:21:25"
    print(stringToDict(cookie))

