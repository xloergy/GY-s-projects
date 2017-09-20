import urllib.request
import re

# 网址
year="2050"
city="wuhan"
url = "http://www.tianqihoubao.com/lishi/"+city+"/month/"+year
pattern = re.compile('<a.*?/lishi/'+city+'/'+year+'.*?>(.*?)</a>.*?<td>.*?</td>.*?<td>(.*?)</td>',re.S)
for month in [ '01', '02','03','04','05','06','07','08','09','10','11','12']:
    desturl=url+str(month)+".html"
# 请求
    request = urllib.request.Request(desturl)
# 爬取结果
    response = urllib.request.urlopen(request)
    data = response.read()
# 设置解码方式
    data = data.decode('GBK')
# 打印结果
    items = re.findall(pattern,data)

    if len(items):
        for item in items:
            maxandmintemp=item[1].split("/")
            f = open("C:/Program Files/WeatherInfo/result-"+city+"-"+year+".txt", "a+")
            print(item[0].strip(),maxandmintemp[0].strip(),maxandmintemp[1].strip(),file=f)
    else:
        print("未查询到"+year+"年"+month+"月天气状况")

# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())