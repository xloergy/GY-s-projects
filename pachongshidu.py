import urllib.request
import re

# 网址
url = "http://www.weather.com.cn/weather40d/101271701.shtml"
pattern = re.compile('<span.*?nowday.*?>(.*?)</span>.*?<span.*?max.*?>(.*?)</span>.*?<span.*?min.*?>(.*?)</span>'
                     +'.*?<span.*?tubiao.*?>(.*?)</span>',re.S)

desturl=url
# 请求
request = urllib.request.Request(desturl)

# 爬取结果
response = urllib.request.urlopen(request)
data = response.read()
# 设置解码方式
data = data.decode('UTF-8')

# 打印结果
items = re.findall(pattern,data)

if len(items):
    for item in items:
        min=item[3].split("/")
        print(item[0],item[2],min,item[3])
else:
    print("list is null")

# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())