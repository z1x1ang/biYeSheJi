# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "zixiang"  
#FileName: *.py
#Time:2021/3/9  
#Version:3.6.5  
#====#====#====#====  
import requests
import re
import csv
# from bs4 import BeautifulSoup
from lxml import etree
def China():
    url="http://www.sy72.com/covid/index.asp?s1=0&s2=0"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    r=tree.xpath('//tr[@id="cx"]/td[3]/span/text()')
    r.insert(0,"中国")
    f = open("y_iQing4.csv", "a", newline='')
    writer = csv.writer(f)
    writer.writerow(r)
    f.close()
    print(r)

def world():
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse("world.html", parser=parser)
    c=tree.xpath('//div[@class="world-muall"]/ul/li/a/text()')
    r=tree.xpath('//div[@class="world-muall"]/ul/li/a/@href')
    head="http://www.sy72.com"
    for i in range(0,len(c)):
        # print(c[i],head+r[i])
        # print(r[i])
        # 日本，马提尼克，
        if r[i] != "/world/world2.html" and r[i]!="/world/world211.html" and r[i]!="/world/world191.html" and r[i]!="/world/world261.html" :
            # print("ok",head+r[i])
            countWorld(head+r[i])


def countWorld(str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    page_text = requests.get(url=str, headers=headers)
    page_text = page_text.text.encode("latin1").decode("utf-8")
    # print(page_text)
    # 内容分析
    # parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(page_text)
    # print(page_text)
    # list1=[]
    list2=[]
    r = tree.xpath('//div[@class="world"]/ul/li/a/text()')
    country=tree.xpath('//p[@id="world-mux"]/text()')
    # print(country[0])
    list2.append(country[0])
    for i in range(1,len(r)):
         b=re.split(r"\s",r[i])
         try:
            list2.append(re.findall('\d+',b[1])[0])
         except:
            print(country[0])
    print(list2)
    f=open("y_iQing.csv","a",newline='')
    writer=csv.writer(f)
    writer.writerow(list2)
    f.close()
if __name__ == '__main__':
    # 实例化好了一个etree对象
    # parser = etree.HTMLParser(encoding="utf-8")
    # tree = etree.parse("covid19.html", parser=parser)
    # r=tree.xpath('//tr[@id="cx"]/td[1]/span/text()')
    world()
    China()