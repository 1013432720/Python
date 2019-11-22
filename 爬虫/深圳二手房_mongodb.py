import requests
from lxml import etree
import csv
import time
import random
import pymongo
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
pre_url = 'https://shenzhen.qfang.com/sale/f'
cookie='acw_tc=7abe401b15743356219817284efcee513b2cafa642ee43397c25525598; sid=811898de-637b-4198-b918-f0a8920c8cc8; \
    qchatid=9564b3a3-78e5-4b73-b460-fc4ce333eea2; language=SIMPLIFIED; CITY_NAME=SHENZHEN; WINDOW_DEVICE_PIXEL_RATIO=1.2000000476837158;\
    _ga=GA1.3.335701767.1574335628; _gid=GA1.3.447669710.1574335628; \
    JSESSIONID=aaaU9TSb5wA21hbRfun6w; Hm_lvt_4d7fad96f5f1077431b1e8d8d8b0f1ab=1574335628,1574410100,1574429315; \
    Hm_lvt_de678bd934b065f76f05705d4e7b662c=1574335628,1574410100,1574429316; cookieId=74c5d571-61d2-4000-bbeb-d978b2e2da5c; \
    sec_tc=AQAAACp18DejhwkAdZffeEUTl1srpiqs; acw_sc__v2=5dd7f1da55b0173a89a438b6de5a8db5c74ba859; _dc_gtm_UA-47416713-1=1;\
    Hm_lpvt_4d7fad96f5f1077431b1e8d8d8b0f1ab=1574433253; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1574433254'
    
Client=pymongo.MongoClient('localhost', 27017)
db=Client['ShenZhenErShouFang']
col=db['info']
def writer_mogo(item):
    col.insert_one(dict(item))
    return item

def download(url):
    html = requests.get(url,headers=headers,cookies=cookie_dict(cookie))
    time.sleep(random.randint(3,7))		#尝试随机等待时间
    return etree.HTML(html.content.decode())

def cookie_dict(cookie):
    cookies = {}
    for k_v in cookie.split(';'):   #根据；分割
        k,v = k_v.split('=',1)  #以=为分割符分成两个
        cookies[k.strip()]=v.replace('"','')    #去除首尾空格
    return cookies


#def data_writer(item):
#    with open('e:\VSCodeCodeFIle\深圳二手房.csv', 'a+',encoding='utf-8', newline='') as csvfile:
#        mywriter = csv.writer(csvfile)
#        mywriter.writerow(item)


def spider(url):
    selector = download(url)
    house_list = selector.xpath("/html/body/div[5]/div/div[1]/div[4]/ul/li")
    for house in house_list:
        item={}
        item['apartment'] = house.xpath("div[2]/div[1]/a/text()")[0]
        item['houselayout'] = house.xpath("div[2]/div[2]/p[1]/text()")[0]
        item['area'] = house.xpath("div[2]/div[2]/p[2]/text()")[0]
        item['region'] = house.xpath("div[2]/div[3]/div[1]/a[1]/text()")[0]
        item['totalprice'] = house.xpath("div[3]/p[1]/span[1]/text()")[0]
        #data_writer(item)
        writer_mogo(item)


if __name__ =='__main__':
    for i in range(1, 11):  # 爬取前10页
        spider(pre_url + str(i))
