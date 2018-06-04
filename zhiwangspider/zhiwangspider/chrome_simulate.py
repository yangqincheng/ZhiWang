import pytesseract
from PIL import Image
from selenium import webdriver
import re
from zhiwangspider.settings import dict_cookies
import time
def checkCode(img_path='check_code.png'):
    '''
    调用接口请求验证码，保存到本地，识别验证，检查识别的验证码对不对。
    '''
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"
    # Include the above line, if you don't have tesseract executable in your PATH
    # Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

    # 用Image模块打开上一步保存的验证码
    image = Image.open(img_path)#.convert('L')
    # 转为灰度图片
    image = image.convert('L')
    # 二值化
    table = []
    for i in range(256):
        if i < 70:
            table.append(0)
        else:
            table.append(1)
    image_bi = image.point(table, '1')
    image_bi = image_bi.convert('L')

    tessdata_dir_config = r'--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
    # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # It's important to include double quotes around the dir path.

    # image_bi.show()# 展示图像
    # 识别验证码，设置模式-psm 7，以及字符白名单
    checkCode = pytesseract.image_to_string(image_bi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 7', lang='eng')

    # 打印出验证码
    print("验证码：", checkCode)
    return checkCode

def try_checkCode(driver,box):
    # 比较好理解、截图并保存到这个路径
    driver.get_screenshot_as_file('screenshot.png')
    # 打开刚刚保存的图片
    im = Image.open('screenshot.png')
    # 设置要裁剪的区域（验证码所在的区域）,可以通过画图软件观察
    # 截图，生成只有验证码的图片
    region = im.crop(box)
    # 保存到本地路径
    region.save("check_code.png")

    check_code = checkCode()
    check_code = re.sub('\W','',check_code) #[^a-zA-Z0-0]

    driver.find_element_by_xpath('//input[@id="CheckCode"]').send_keys(check_code) #输入验证码
    #通过submit()或者click() 来操作
    driver.find_element_by_xpath('/html/body/p[1]/input[2]').click()# 点击提交按钮
    time.sleep(0.5)# 需sleep，等待加载
    #/html/body/text()
    print(driver.find_element_by_xpath('/html/body').text)
    if '错误' in driver.find_element_by_xpath('/html/body').text:
        print('验证码错误，程序重试！')
        driver.find_element_by_xpath('//input[@id="CheckCode"]').click()  # 输入验证码
        box = (751, 124, 846, 159)
        time.sleep(0.5) #等待页面加载
        return try_checkCode(driver,box)
    else:
        print("____",driver.current_url)
        # driver.quit()
        return driver.current_url

def return_link(url):
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    for name,value in dict_cookies.items(): #增加cookie
        driver.add_cookie({'name':name,'value':value})
    box = (751, 71, 846, 103) #无错误时验证码的位置,left, top, right, bottom
    return try_checkCode(driver,box)


def click_fifty(url):
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    for name, value in dict_cookies.items():
        driver.add_cookie({'name': name, 'value': value})
    driver.find_element_by_xpath('//*[@id="id_grid_display_num"]/a[3]/font').click()# 点击提交按钮
    return driver.current_url

