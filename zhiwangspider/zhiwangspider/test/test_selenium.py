from selenium import webdriver

driver = webdriver.PhantomJS()  # 获取浏览器对象
driver.get('http://www.baidu.com/')
print(driver.page_source)
