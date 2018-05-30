import requests
import pytesseract
from zhiwangspider.settings import DEFAULT_REQUEST_HEADERS
from lxml import etree
from PIL import Image

def checkCode(failed_page_url):
    '''
    调用接口请求验证码，保存到本地，识别验证，检查识别的验证码对不对。
    '''
    # 获取网址的路径
    # //*[@id="CheckCodeImg"]
    html=requests.get(failed_page_url, headers=DEFAULT_REQUEST_HEADERS).text
    selector=etree.HTML(html)
    img_url='http://kns.cnki.net'+selector.xpath('//img[@id="CheckCodeImg"]/@src')[0]
    print(img_url)
    # 发送请求
    response = requests.request("GET", img_url, verify=False)
    # 接口返回的数据以二进制的方式展示
    img = response.content

    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"
    # Include the above line, if you don't have tesseract executable in your PATH
    # Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

    # print(pytesseract.image_to_string(Image.open('test.png')))
    # print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))


    # 选择保存的路径和图片格式
    with open('check_code.jpg', 'wb') as f:
        # 保存
        f.write(img)
    # 用Image模块打开上一步保存的验证码
    image = Image.open('check_code.jpg')
    #改为RGB模式
    image = image.convert('RGB')

    tessdata_dir_config = r'--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
    # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # It's important to include double quotes around the dir path.


    checkCode = pytesseract.image_to_string(image, config='tessedit_char_whitelist=0123456789ABCDEFGHIJKLMN -psm 6')

    # 识别验证码
    # checkCode = pytesseract.image_to_string(image,lang='fra')
    # 打印出验证码
    print("验证码：", checkCode)
    return checkCode

url="http://kns.cnki.net/kns/brief/vericode.aspx?rurl=%2fkns%2fbrief%2fbrief.aspx%3fcurpage%3d17%26RecordsPerPage%3d20%26QueryID%3d9%26ID%3d%26turnpage%3d1%26tpagemode%3dL%26dbPrefix%3dSCDB%26Fields%3d%26DisplayMode%3dlistmode%26PageName%3dASP.brief_result_aspx"
checkCode(url)