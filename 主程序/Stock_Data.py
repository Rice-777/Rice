import requests
from bs4 import BeautifulSoup
import re

url_1 = "http://quote.eastmoney.com/stock_list.html"
r_1 = requests.get(url_1)
r_1.encoding = r_1.apparent_encoding
soup_1 = BeautifulSoup(r_1.text, "html.parser")
tags = soup_1.find_all("a")
titlelist = []
for tag in tags:
    try:
        link = tag.attrs['href']
        titlelist.append(re.findall(pattern=r"\d{6}", string=link)[0])
    except:
        continue

dictionary = {}
path = "C://Users/Rice/Desktop/Stock_Data.txt"
keylist = ["流通市值", "总市值", "流通股本", "总股本"]
for title in titlelist:
    url_2 = "http://stock.quote.stockstar.com/" + title + ".shtml"
    r_2 = requests.get(url_2)
    r_2.encoding = r_2.apparent_encoding
    soup_2 = BeautifulSoup(r_2.text, "html.parser")
    table = soup_2.find("table", attrs={"border": "0"})
    if table:
        value_taglist = table.find_all("span")
        for i in range(len(keylist)):
            valuelist = value_taglist[i].text
            dictionary.update({keylist[i]: valuelist})
        with open(path, "a", encoding="utf-8", errors="ignore") as f:
            f.write("股票代码 : " + title + str(dictionary) + "\n")
            print("OK + 1")
print("全部爬取完毕")
