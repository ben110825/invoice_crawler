# coding=utf-8
import requests
from bs4 import BeautifulSoup

list = ['特別獎', '特獎', '頭獎', '頭獎', '頭獎', '增開六獎']

# 發票中獎號碼網址
url_lists = ['https://invoice.etax.nat.gov.tw/',
             'https://invoice.etax.nat.gov.tw/lastNumber.html']

for url in url_lists:
    list_number = []
    j = 0
    # 對url發出請求
    response = requests.get(url)
    response.encoding = "utf-8"

    # 使用BeautifulSoup解析 HTML 程式碼
    soup = BeautifulSoup(response.text, 'html.parser')

    # 取得當次標題
    title = soup.find("a", "etw-on")

    # 取得當次發票中獎號
    result = soup.find_all(
        "span", 'font-weight-bold')

    temp = ''
    for i in result:
        st = temp+i.get_text()
        if(len(list_number) == 5):
            list_number.append(st)
            break
        if(len(st) == 8):
            list_number.append(st)
            temp = ''
        else:
            temp = st

    print(title.text)
    for i in list_number:
        print('>>{0}:{1}'.format(list[j], i))
        j += 1
