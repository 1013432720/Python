import requests
from lxml import etree
import re
import csv
# 网页url
url ="http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316"
# HTTP请求头
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
# 下载网页
response = requests.get(url, headers = headers)
# 构建selector
selector = etree.HTML(response.content.decode())
# xpath采集内容
movies_script = selector.xpath('/html/body/script[3]/text()')[0]
# 打印内容
print(movies_script)

# 获取“今日电影”所在字符串
movies = re.search(r'"movies":\[.*?\]',movies_script).group()
print(movies)
# 获取“今日电影”列表（详细）
moviesList = re.findall(r'{.*?}',movies)
print(moviesList)

# 创建列名
fieldsname = ["movieTitleCn","movieTitleEn","director","runtime"]
# 写csv文件
with open('movieToday.csv','w',newline='') as csv_movieToday:
        csv_writer = csv.writer(csv_movieToday)	 # 创建csv writer对象
        csv_writer.writerow(fieldsname)		 # 写入列名
        for movie in moviesList:
            movie_dict = eval(movie)		 # 获取今日电影（字典）
            movieTitleCn = movie_dict.get("movieTitleCn")
            movieTitleEn = movie_dict.get("movieTitleEn")
            director = movie_dict.get("director")     
            runtime = movie_dict.get("runtime")      
            csv_writer.writerow([movieTitleCn,movieTitleEn,director,runtime])		