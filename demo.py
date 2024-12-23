import requests
import js2py
import datetime
from open_cv import cal_loc
import base64
import re
from bs4 import BeautifulSoup

session = requests.session()

def get_p1():
    # url = "https://pass.ujs.edu.cn/cas/login?service=http%3A%2F%2Fehall.ujs.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.ujs.edu.cn%2Fnew%2Findex.html"
    url = "https://webvpn.ujs.edu.cn/https/77726476706e69737468656265737421e0f6528f69256243300d8db9d6562d/cas/login?service=https%3A%2F%2Fwebvpn.ujs.edu.cn%2Flogin%3Fcas_login%3Dtrue"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36"
    }
    response = session.get(url, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(response.text,'html.parser')
    dllt = soup.find('input',{'name':'dllt'})['value']
    lt = soup.find('input', {'name': 'lt'})['value']
    execution = soup.find('input', {'name': 'execution'})['value']
    eventId = soup.find('input', {'name': '_eventId'})['value']
    rmShown = soup.find('input', {'name': 'rmShown'})['value']
    # 找到所有 <script> 标签
    script_tags = soup.find_all('script')

    # 正则匹配 secure 和 pwdDefaultEncryptSalt 的值
    for script in script_tags:
        # 转换为文本并查找变量
        script_content = script.string
        if script_content:
            match = re.search(r'var\s+pwdDefaultEncryptSalt\s*=\s*"([^"]+)"', script_content)
            if match:
                pwdDefaultEncryptSalt = match.group(1)
                get_passwd(pwdDefaultEncryptSalt,dllt,lt,eventId,execution,rmShown)


def get_passwd(p1,dllt,lt,eventId,execution,rmShown):
    with open('node1.js', 'r') as file:
        js_code = file.read()
    # 执行 JavaScript 代码
    context = js2py.EvalJs()
    context.len1 = 16
    context.len2 = 64
    context.execute(js_code)
    result_16 = context.rds(context.len1)
    # result_16 = '7AnjaEeCssQxMiXz'
    result_64 = context.rds(context.len2) + 'lzw20021003'
    # result_64 = 'wQNdhpedChRaEZx5WfzmTdYZYZkitiQpBfjMA4rEyt2tp8Q3sJ5My3wWNBx6Npkp1'
    file.close()

    with open('node.js', 'r') as f:
        js_code1 = f.read()
    context = js2py.EvalJs()
    context.data = result_64
    context.p1 = p1
    context.iv0 = result_16
    f.close()
    context.execute(js_code1)
    password = context.gas(context.data, context.p1, context.iv0)
    get_sign(password,dllt,lt,eventId,execution,rmShown)
    # return password


def get_sign(password,dllt,lt,eventId,execution,rmShown):
    # url = "https://pass.ujs.edu.cn/cas/sliderCaptcha.do"
    url = "https://webvpn.ujs.edu.cn/https/77726476706e69737468656265737421e0f6528f69256243300d8db9d6562d/cas/sliderCaptcha.do?vpn-12-o2-pass.ujs.edu.cn"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36"
    }
    # 获取当前时间
    now = datetime.datetime.now()
    # 转换为毫秒级的 Unix 时间戳
    timestamp = int(now.timestamp() * 1000)
    data = {
        "_": timestamp
    }
    response = session.get(url, headers=headers, params=data)
    bigImage = response.json()['bigImage']
    smallImage = response.json()['smallImage']
    # 解码Base64字符串
    bigImageimage_data = base64.b64decode(bigImage)
    smallImageimage_data = base64.b64decode(smallImage)

    # 保存图像到文件
    with open("bigimage.jpg", "wb") as image_file:
        image_file.write(bigImageimage_data)

    with open("smallimage.jpg", "wb") as image_file:
        image_file.write(smallImageimage_data)

    a = int(cal_loc('bigimage.jpg', 'smallimage.jpg') / 2.08)
    data2 = {
        "canvasLength": 280,
        "moveLength": a
    }
    # url1 = "https://pass.ujs.edu.cn/cas/verifySliderImageCode.do"
    url1 = "https://webvpn.ujs.edu.cn/https/77726476706e69737468656265737421e0f6528f69256243300d8db9d6562d/cas/verifySliderImageCode.do?vpn-12-o2-pass.ujs.edu.cn"
    response1 = session.get(url1, headers=headers, params=data2)
    sign = response1.json()['sign']
    login(sign,password,dllt,lt,eventId,execution,rmShown)

def login(sign,password,dllt,lt,eventId,execution,rmShown):
    # url = 'https://pass.ujs.edu.cn/cas/login?service=http%3A%2F%2Fehall.ujs.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.ujs.edu.cn%2Fnew%2Findex.html'
    url = "https://webvpn.ujs.edu.cn/https/77726476706e69737468656265737421e0f6528f69256243300d8db9d6562d/cas/login?service=https%3A%2F%2Fwebvpn.ujs.edu.cn%2Flogin%3Fcas_login%3Dtrue"
    url2 = "https://webvpn.ujs.edu.cn/http/77726476706e69737468656265737421f7ee4cd2323a7b1e7b0c9ce29b5b/"
    # url2 = 'http://ehall.ujs.edu.cn/jsonp/userDesktopInfo.json'
    data = {
        'username': '3200601054',
        'password': password,
        "lt": lt,
        'dllt': dllt,
        'execution': execution,
        '_eventId': eventId,
        'rmShown': rmShown,
        'sign': sign
    }
    # print(data)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36"
    }
    response = session.post(url,headers=headers,data=data)

    cookies = session.cookies.get_dict()
    cookie_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
        "Cookie": "; ".join([f"{key}={value}" for key, value in cookies.items()]),
        "Referer": "https://webvpn.ujs.edu.cn/https/77726476706e69737468656265737421e0f6528f69256243300d8db9d6562d/cas/login?service=https%3A%2F%2Fwebvpn.ujs.edu.cn%2Flogin%3Fcas_login%3Dtrue"

    }

    with open('cookie.txt','w',encoding='utf-8') as f:
        f.write("; ".join([f"{key}={value}" for key, value in cookies.items()]))
    now = datetime.datetime.now()
    timestamp = int(now.timestamp() * 1000)
    data = {
        "_": timestamp
    }
    # print(data)
    # print(cookie_header)

    response1 = session.get(url2,headers=cookie_header)
    pattern = r'<label for="type1">(.+?)</label>'
    match = re.search(pattern, response1.text)

    if match:
        print("找到的文本:", match.group(1))
    else:
        print("未找到“在校学生”文本")
    return cookie_header
    # print(response1.text)

if __name__ == '__main__':
    passwd = get_p1()
