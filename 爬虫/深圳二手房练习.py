import requests
from lxml import etree
import csv
import time
import random
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
pre_url = 'https://shenzhen.qfang.com/sale/f'
cookie='acw_tc=b7d6989915744122554692165eb7cac9fe873bb3045d3d03967cf40bca; sid=85f9d38f-485c-4ea7-ab04-464e37ca6806; cookieId=9d292516-c67c-4026-a7f5-0d20934391e7; qchatid=e73274f6-3be4-4afb-a56f-33a0e3f80c52; language=SIMPLIFIED; JSESSIONID=aaaslb39uF1k4dma5tn6w; CITY_NAME=SHENZHEN; WINDOW_DEVICE_PIXEL_RATIO=1; Hm_lvt_4d7fad96f5f1077431b1e8d8d8b0f1ab=1574412259; Hm_lvt_de678bd934b065f76f05705d4e7b662c=1574412260; _ga=GA1.3.142651490.1574412260; _gid=GA1.3.224440949.1574412260; sec_tc=AQAAAAIGITkwaAwAdZffePnsQud9jBDO; acw_sc__v2=5dd7e2939ffbb678c1538efe6647fd88ac3fb2fd; Hm_lpvt_4d7fad96f5f1077431b1e8d8d8b0f1ab=1574429340; _dc_gtm_UA-47416713-1=1; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1574429343'
    

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


def data_writer(item):
    with open('e:\VSCodeCodeFIle\深圳二手房.csv', 'a+',encoding='utf-8', newline='') as csvfile:
        mywriter = csv.writer(csvfile)
        mywriter.writerow(item)


def spider(url):
    selector = download(url)
    house_list = selector.xpath("/html/body/div[5]/div/div[1]/div[4]/ul/li")
    for house in house_list:
        apartment = house.xpath("div[2]/div[1]/a/text()")[0]
        houselayout = house.xpath("div[2]/div[2]/p[1]/text()")[0]
        area = house.xpath("div[2]/div[2]/p[2]/text()")[0]
        region = house.xpath("div[2]/div[3]/div[1]/a[1]/text()")[0]
        totalprice = house.xpath("div[3]/p[1]/span[1]/text()")[0]
        item = [apartment, houselayout, area, region, totalprice]
        data_writer(item)


if __name__ =='__main__':
    for i in range(1, 11):  # 爬取前10页
        spider(pre_url + str(i))
